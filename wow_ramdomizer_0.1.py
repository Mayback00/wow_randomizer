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
        self.razas = ['Humano', 'Elfo_de_la_noche', 'Enano', 'Gnomo', 'Orco', 'Trol', 'No-muerto', 'Tauren', 'Elfo_de_sangre', 'Elfo_nato_nocturno', 'Draenei', 'Draenei_temple_luz', 'Goblin', 'Kultiriano', 'Pandaren', 'Mecagnomo', 'Orco_maghar', 'Tauren_alta_montana', 'Trol_zandalary', 'Drakthyr', 'Vulpira', 'Enano_roca_negra', 'Huargen', 'Elfo_del_vacio']
        self.generos = ['Masculino', 'Femenino']
        self.clases = ['Guerrero', 'Paladin', 'Cazador', 'Picaro', 'Sacerdote', 'Dk', 'Chaman', 'Mago', 'Brujo', 'Monje', 'Druida', 'Evocador', 'Dh']

        # Cargar imágenes de razas, géneros y clases
        self.imagenes_razas = [ImageTk.PhotoImage(Image.open(f'imagenes/imagen_raza_{raza.lower()}.png').resize((134, 131), resample=Image.LANCZOS)) for raza in self.razas]
        self.imagenes_generos = [ImageTk.PhotoImage(Image.open(f'imagenes/imagen_genero_{genero.lower()}.png').resize((134, 131), resample=Image.LANCZOS)) for genero in self.generos]
        self.imagenes_clases = [ImageTk.PhotoImage(Image.open(f'imagenes/imagen_clase_{clase.lower()}.png').resize((134, 131), resample=Image.LANCZOS)) for clase in self.clases]

        # Crear etiquetas e imágenes
        self.imagen_raza = ttk.Label(root, image=None)
        self.imagen_raza.grid(row=0, column=0, pady=(self.root.winfo_reqheight() * 0.1, 0), padx=(0, 0), sticky='n')

        self.imagen_genero = ttk.Label(root, image=None)
        self.imagen_genero.grid(row=1, column=0, pady=0, padx=(0, 0), sticky='n')

        self.imagen_clase = ttk.Label(root, image=None)
        self.imagen_clase.grid(row=2, column=0, pady=(0, 0), padx=(0, 0), sticky='n')

        # Botón de generación aleatoria
        self.boton_generar = ttk.Button(root, text="Generar Personaje", command=self.generar_personaje, style='TButton')

        # Obtener el 20% del borde superior
        base_20_percent = int(self.root.winfo_reqheight() * 0.5)

        # Configurar el botón en la base centrado
        self.boton_generar.place(relx=0.5, rely=1, anchor='s', y=-base_20_percent)

        # Establecer tamaño inicial
        self.root.geometry("405x720")
        # Vincular la función de ajuste al cambio de tamaño
        self.root.bind("<Configure>", self.on_configure)
        self.resize_flag = False

    def on_configure(self, event):
        # Check the flag to determine whether to adjust the size
        if self.resize_flag:
            # Ajustar la imagen de fondo al tamaño de la ventana
            ancho, altura = 405, 720
            nueva_fondo = Image.open("fondo.jpg").resize((ancho, altura), resample=Image.LANCZOS)
            nueva_fondo = ImageTk.PhotoImage(nueva_fondo)
            self.label_fondo.configure(image=nueva_fondo)
            self.label_fondo.image = nueva_fondo

            # Configurar la geometría de la ventana y deshabilitar la capacidad de cambiar tamaño
            self.root.geometry(f"{ancho}x{altura}")
            self.root.resizable(width=False, height=False)

            # Configurar el tamaño de la cuadrícula para las imágenes
            ancho_imagen = 134
            altura_imagen = 134
            margen_entre_imagenes = (altura - 3 * altura_imagen) // 2  # Margen entre las secciones

            # Configurar la cuadrícula para centrar verticalmente las imágenes
            self.root.grid_rowconfigure(0, minsize=altura_imagen, weight=1)
            self.root.grid_rowconfigure(1, minsize=margen_entre_imagenes, weight=0)
            self.root.grid_rowconfigure(2, minsize=altura_imagen, weight=1)

            # Centrar las imágenes horizontalmente en la cuadrícula
            self.imagen_raza.grid_configure(pady=(0, 15))
            self.imagen_genero.grid_configure(pady=(0, 0))
            self.imagen_clase.grid_configure(pady=(15, 0))

            # Ajustar solo el botón al 20% de la base
            base_20_percent = int(self.root.winfo_reqheight() * 0.2)
            self.boton_generar.place(relx=0.5, rely=1, anchor='s', y=-base_20_percent)

            # Set the flag to False to prevent further adjustments
            self.resize_flag = False

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

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=2)

        # Ajustar el espacio vertical
        self.imagen_raza.grid_configure(column=0, sticky='n')
        self.imagen_genero.grid_configure(column=0, sticky='n')
        self.imagen_clase.grid_configure(column=0, sticky='n')

if __name__ == "__main__":
    root = tk.Tk()
    app = WoWCharacterGenerator(root)
    root.mainloop()
