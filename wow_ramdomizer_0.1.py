import tkinter as tk
from PIL import ImageTk, Image
import random
import pygame

class WoWCharacterGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("WoW Dragonflight Character Generator")
        self.root.iconbitmap("imagenes/icono.ico")

        # Configurar la imagen de fondo
        self.fondo = ImageTk.PhotoImage(Image.open("imagenes/fondo.jpg"))
        self.label_fondo = tk.Label(root, image=self.fondo)
        self.label_fondo.place(relwidth=1, relheight=1)

        # Crear un marco para el grid de imágenes
        self.marco_imagenes = tk.Frame(root)
        self.marco_imagenes.grid(row=0, column=0, pady=(root.winfo_reqheight() * 0.1, 0), padx=(0, 0), sticky='n')

        # Razas, géneros y clases (incluyendo las opciones adicionales)
        self.razas = ['Humano', 'Elfo_de_la_noche', 'Enano', 'Gnomo', 'Orco', 'Trol', 'No-muerto', 'Tauren', 'Elfo_de_sangre', 'Elfo_nato_nocturno', 'Draenei', 'Draenei_temple_luz', 'Goblin', 'Kultiriano', 'Pandaren', 'Mecagnomo', 'Orco_maghar', 'Tauren_alta_montana', 'Trol_zandalary', 'Drakthyr', 'Vulpira', 'Enano_roca_negra', 'Huargen', 'Elfo_del_vacio', 'Facciones']
        self.generos = ['Masculino', 'Femenino', 'mf']
        self.clases = ['Guerrero', 'Paladin', 'Cazador', 'Picaro', 'Sacerdote', 'Dk', 'Chaman', 'Mago', 'Brujo', 'Monje', 'Druida', 'Evocador', 'Dh', 'Tdah']

        # Listas de opciones adicionales
        opciones_adicionales_razas = ['Facciones']
        opciones_adicionales_generos = ['Mf']
        opciones_adicionales_clases = ['Tdah']

        # Cargar imágenes de razas, géneros y clases (incluyendo las opciones adicionales)
        self.imagenes_razas = [ImageTk.PhotoImage(Image.open(f'imagenes/imagen_raza_{raza.lower()}.png').resize((134, 131), resample=Image.LANCZOS)) for raza in self.razas]
        self.imagenes_generos = [ImageTk.PhotoImage(Image.open(f'imagenes/imagen_genero_{genero.lower()}.png').resize((134, 131), resample=Image.LANCZOS)) for genero in self.generos]
        self.imagenes_clases = [ImageTk.PhotoImage(Image.open(f'imagenes/imagen_clase_{clase.lower()}.png').resize((134, 131), resample=Image.LANCZOS)) for clase in self.clases]

        # Crear etiquetas e imágenes dentro del marco
        self.imagen_raza = tk.Label(self.marco_imagenes, image=self.imagenes_razas[-1])  # Última imagen es 'Facciones'
        self.imagen_raza.grid(row=0, column=0, pady=0, padx=(0, 0), sticky='n')

        self.imagen_genero = tk.Label(self.marco_imagenes, image=self.imagenes_generos[-1])  # Última imagen es 'Mf'
        self.imagen_genero.grid(row=1, column=0, pady=0, padx=(0, 0), sticky='n')

        self.imagen_clase = tk.Label(self.marco_imagenes, image=self.imagenes_clases[-1])  # Última imagen es 'Tdah'
        self.imagen_clase.grid(row=2, column=0, pady=0, padx=(0, 0), sticky='n')

        # Cargar imagen para el label
        self.imagen_label = ImageTk.PhotoImage(file='imagenes/boton.png')
        
       # Cargar imágenes para la etiqueta (original y al hacer clic)
        self.imagen_label_original = ImageTk.PhotoImage(file='imagenes/boton.png')
        self.imagen_label_clic = ImageTk.PhotoImage(file='imagenes/boton_press.png')

        # Configurar sonido de clic
        pygame.mixer.init()
        self.sonido_clic = pygame.mixer.Sound("sounds/arcade_machine.wav")

        # Botón para generar personajes
        self.label_generar = tk.Label(root, image=self.imagen_label_original, cursor="hand2", highlightthickness=0, bd=0)
        self.label_generar.grid(row=3, column=0, pady=10)
        
        # Calculate the 20% of the height of the root window
        base_20_percent = int(root.winfo_reqheight() * 0.4)

        # Place the label centered horizontally and at 20% of the height from the bottom
        self.label_generar.place(relx=0.5, rely=1, anchor='s', y=-base_20_percent)

        # Bind the label to functions for press and release events
        self.label_generar.bind("<Button-1>", lambda event: (self.on_label_press(), self.generar_personaje()))
        self.label_generar.bind("<ButtonRelease-1>", lambda event: self.on_label_release())

        # Establecer tamaño inicial
        root.geometry("405x720")

        # Centrar el marco en la ventana
        self.marco_imagenes.place(relx=0.5, rely=0.5, anchor='center')
        
        self.timer_running = False
        self.resultado_final = None
        
    def on_label_press(self):
        self.label_generar.config(image=self.imagen_label_clic)
        self.sonido_clic.play()

    def on_label_release(self):
        if not self.timer_running:
            # Si el temporizador no está en ejecución, comienza el efecto de ruleta
            self.timer_running = True
            self.iniciar_ruleta()

    def iniciar_ruleta(self):
        # Muestra imágenes al azar durante 3 segundos antes de seleccionar el resultado final
        for _ in range(22):  # Cambiar el número de iteraciones para ajustar la duración
            raza_aleatoria = random.choice(self.razas)
            genero_aleatorio = random.choice(self.generos)
            clase_aleatoria = random.choice(self.clases)

            self.imagen_raza.configure(image=self.imagenes_razas[self.razas.index(raza_aleatoria)])
            self.imagen_genero.configure(image=self.imagenes_generos[self.generos.index(genero_aleatorio)])
            self.imagen_clase.configure(image=self.imagenes_clases[self.clases.index(clase_aleatoria)])

            self.root.update()  # Actualizar la ventana para mostrar la nueva imagen
            self.root.after(100)  # Ajustar la velocidad de cambio de imagen (en milisegundos)

        # Después de 3 segundos, seleccionar el resultado final
        self.generar_personaje()
        self.timer_running = False
        self.label_generar.config(image=self.imagen_label_original)

    def generar_personaje(self):
        # Seleccionar al azar una raza, género y clase
        razas_sin_opciones_adicionales = [raza for raza in self.razas if raza not in ['Facciones']]
        generos_sin_opciones_adicionales = [genero for genero in self.generos if genero not in ['mf']]
        clases_sin_opciones_adicionales = [clase for clase in self.clases if clase not in ['Tdah']]

        raza_aleatoria = random.choice(razas_sin_opciones_adicionales)
        genero_aleatorio = random.choice(generos_sin_opciones_adicionales)

        # Restricciones de clase según la raza
        clases_permitidas = clases_sin_opciones_adicionales.copy()

        if raza_aleatoria in ['Humano', 'Draenei_temple_luz']:
            clases_permitidas.remove('Chaman')
            clases_permitidas.remove('Druida')
            clases_permitidas.remove('Dh')
            clases_permitidas.remove('Evocador')

        elif raza_aleatoria == 'Elfo_de_sangre':
            clases_permitidas.remove('Chaman')
            clases_permitidas.remove('Druida')
            clases_permitidas.remove('Evocador')

        elif raza_aleatoria == 'Drakthyr':
            clases_permitidas.remove('Chaman')
            clases_permitidas.remove('Druida')
            clases_permitidas.remove('Guerrero')
            clases_permitidas.remove('Brujo')
            clases_permitidas.remove('Monje')
            clases_permitidas.remove('Picaro')
            clases_permitidas.remove('Cazador')
            clases_permitidas.remove('Sacerdote')
            clases_permitidas.remove('Dk')
            clases_permitidas.remove('Mago')
            clases_permitidas.remove('Dh')
            clases_permitidas.remove('Paladin')

        elif raza_aleatoria == 'Enano':
            clases_permitidas.remove('Druida')
            clases_permitidas.remove('Dh')
            clases_permitidas.remove('Evocador')

        elif raza_aleatoria == 'Elfo_de_la_noche':
            clases_permitidas.remove('Paladin')
            clases_permitidas.remove('Chaman')
            clases_permitidas.remove('Evocador')

        elif raza_aleatoria in ('Trol_zandalary', 'Tauren'):
            clases_permitidas.remove('Dh')
            clases_permitidas.remove('Evocador')

        elif raza_aleatoria in ['Gnomo', 'Mecagnomo', 'Elfo_nato_nocturno', 'Elfo_del_vacio', 'No-muerto']:
            clases_permitidas.remove('Paladin')
            clases_permitidas.remove('Druida')
            clases_permitidas.remove('Chaman')
            clases_permitidas.remove('Dh')
            clases_permitidas.remove('Evocador')

        elif raza_aleatoria in ['Draenei', 'Enano_roca_negra']:
            clases_permitidas.remove('Druida')
            clases_permitidas.remove('Dh')
            clases_permitidas.remove('Evocador')

        elif raza_aleatoria == 'Huargen':
            clases_permitidas.remove('Paladin')
            clases_permitidas.remove('Chaman')
            clases_permitidas.remove('Dh')
            clases_permitidas.remove('Evocador')

        elif raza_aleatoria in ['Orco', 'Orco_maghar', 'Goblin', 'Vulpira', 'Pandaren']:
            clases_permitidas.remove('Paladin')
            clases_permitidas.remove('Druida')
            clases_permitidas.remove('Dh')
            clases_permitidas.remove('Evocador')

        elif raza_aleatoria in ['Kultiriano', 'Trol', 'Tauren_alta_montana']:
            clases_permitidas.remove('Paladin')
            clases_permitidas.remove('Dh')
            clases_permitidas.remove('Evocador')

        # Seleccionar una clase permitida al azar
        clase_aleatoria = random.choice(clases_permitidas)

        # Mostrar las imágenes correspondientes
        self.imagen_raza.configure(image=self.imagenes_razas[self.razas.index(raza_aleatoria)])
        self.imagen_genero.configure(image=self.imagenes_generos[self.generos.index(genero_aleatorio)])
        self.imagen_clase.configure(image=self.imagenes_clases[self.clases.index(clase_aleatoria)])


if __name__ == "__main__":
    root = tk.Tk()
    app = WoWCharacterGenerator(root)
    root.mainloop()
