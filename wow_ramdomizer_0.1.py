import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random

class WoWCharacterGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("WoW Dragonflight Character Generator")
        self.root.iconbitmap("icono.ico")

        # Configurar la imagen de fondo
        self.fondo = ImageTk.PhotoImage(Image.open("fondo.jpg"))
        self.label_fondo = tk.Label(root, image=self.fondo)
        self.label_fondo.place(relwidth=1, relheight=1)

        # Razas, géneros y clases
        self.razas = ['Humano', 'Elfo_de_la_noche', 'Enano', 'Gnomo', 'Orco', 'Trol', 'No-muerto', 'Tauren', 'Elfo_de_sangre', 'Elfo_nato_nocturno', 'Draenei', 'Draenei_temple_luz', 'goblin', 'Kultiriano', 'Pandaren', 'Mecagnomo', 'Orco_maghar', 'Tauren_alta_montana', 'Trol_zandalary', 'Drakthyr', 'Vulpira', 'Enano_roca_negra', 'Huargen', 'Elfo_del_vacio']
        self.generos = ['Masculino', 'Femenino']
        self.clases = ['Guerrero', 'Paladin', 'Cazador', 'Picaro', 'Sacerdote', 'Dk', 'Chaman', 'Mago', 'Brujo', 'Monje', 'Druida', 'Evocador', 'Dh']

        # Cargar imágenes de razas, géneros y clases
        self.imagenes_razas = [ImageTk.PhotoImage(Image.open(f'imagenes/imagen_raza_{raza.lower()}.png')) for raza in self.razas]
        self.imagenes_generos = [ImageTk.PhotoImage(Image.open(f'imagenes/imagen_genero_{genero.lower()}.png')) for genero in self.generos]
        self.imagenes_clases = [ImageTk.PhotoImage(Image.open(f'imagenes/imagen_clase_{clase.lower()}.png')) for clase in self.clases]

        # Crear etiquetas e imágenes
        self.etiqueta_raza = ttk.Label(root, text="Raza:", font=("Helvetica", 12), background="#fff")
        self.etiqueta_genero = ttk.Label(root, text="Género:", font=("Helvetica", 12), background="#fff")
        self.etiqueta_clase = ttk.Label(root, text="Clase:", font=("Helvetica", 12), background="#fff")

        self.imagen_raza = ttk.Label(root, image=None)
        self.imagen_genero = ttk.Label(root, image=None)
        self.imagen_clase = ttk.Label(root, image=None)

        # Botón de generación aleatoria
        self.boton_generar = ttk.Button(root, text="Generar Personaje", command=self.generar_personaje, style='TButton')

        # Diseño de la cuadrícula
        self.etiqueta_raza.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.etiqueta_genero.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.etiqueta_clase.grid(row=2, column=0, padx=5, pady=5, sticky='e')

        self.imagen_raza.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.imagen_genero.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        self.imagen_clase.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        # Obtener el 20% del borde inferior
        base_20_percent = int(self.root.winfo_reqheight() * 0.8)

        # Configurar el botón en la base centrado
        self.boton_generar.place(relx=0.5, rely=1, anchor='s', y=-base_20_percent)

        # Establecer tamaño inicial
        self.root.geometry("405x720")
        # Vincular la función de ajuste al cambio de tamaño
        self.root.bind("<Configure>", self.ajustar_tamano)

    def ajustar_tamano(self, event):
        # Ajustar la imagen de fondo al tamaño de la ventana
        ancho, altura = event.width, event.height
        nueva_fondo = self.fondo.resize((ancho, altura), Image.ANTIALIAS)
        nueva_fondo = ImageTk.PhotoImage(nueva_fondo)
        self.label_fondo.configure(image=nueva_fondo)
        self.label_fondo.image = nueva_fondo

        # Centrar la ventana y mantener las proporciones
        proporciones = 405 / 720
        nuevo_ancho = int(altura * proporciones)
        self.root.geometry(f"{nuevo_ancho}x{altura}+{int((event.width - nuevo_ancho) / 2)}+0")

    def generar_personaje(self):
        # Seleccionar al azar una raza, género y clase
        raza_aleatoria = random.choice(self.razas)
        genero_aleatorio = random.choice(self.generos)

        # Restricciones de clase según la raza
        clases_permitidas = self.clases.copy()

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
