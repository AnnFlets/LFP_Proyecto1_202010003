import sys
import tkinter as tk
from tkinter import messagebox, Menu
from tkinter.filedialog import askopenfile, asksaveasfilename

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        # Ventana principal
        #self.geometry("300x300")
        self.title("Menú principal")
        self.iconbitmap("img/flor.ico")
        # Hacer que la ventana no pueda cambiar su tamaño
        #self.resizable(0, 0)
        self.crear_menu()
        # Configuración tamaño mínimo de la ventana (fila)
        self.rowconfigure(0, minsize=600, weight=1)
        # Configuración tamaño mínimo de la ventana (columna)
        self.columnconfigure(0,minsize=600, weight=1)

        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        # Atributo de archivo (ruta)
        self.archivo = None
        # Atributo para saber si ya se abrió un archivo anteriormente
        self.archivo_activo = False
        #Creación de componentes
        self.crear_cuadro_texto()




        #self.agregar_imagen()

    def crear_cuadro_texto(self):
        #Agregar el campo de texto
        self.campo_texto.grid(row = 0, column=0, sticky="nswe")
    def agregar_imagen(self):
        self.img = tk.PhotoImage(file="img/fondo.png")
        self.lbl_img = tk.Label(self, image=self.img)
        self.lbl_img.grid(row=2, column=0, columnspan=2)

    def crear_menu(self):
        # Configurar el menú principal
        menu_principal = Menu(self)
        # tearoff = False, para evitar que el submenú se separe de la interfaz
        submenu_archivo = Menu(menu_principal, tearoff=False)
        submenu_ayuda = Menu(menu_principal, tearoff=0)
        # Agregar opciones y separadores en el submenú "Archivo"
        submenu_archivo.add_command(label="Abrir", command=self.abrir)
        submenu_archivo.add_separator()
        submenu_archivo.add_command(label="Guardar", command=self.guardar)
        submenu_archivo.add_separator()
        submenu_archivo.add_command(label="Guardar Como", command=self.guardar_como)
        submenu_archivo.add_separator()
        submenu_archivo.add_command(label="Analizar", command=self.analizar)
        submenu_archivo.add_separator()
        submenu_archivo.add_command(label="Errores", command=self.errores)
        submenu_archivo.add_separator()
        submenu_archivo.add_command(label="Salir", command=self.salir)
        # Agregar opciones y separadores en el submenú "Ayuda"
        submenu_ayuda.add_command(label="Manual de usuario", command=self.manual_usuario)
        submenu_ayuda.add_separator()
        submenu_ayuda.add_command(label="Manual Técnico", command=self.manual_tecnico)
        submenu_ayuda.add_separator()
        submenu_ayuda.add_command(label="Temas de Ayuda", command=self.temas_ayuda)
        # Agregar los submenús al menú principal
        menu_principal.add_cascade(menu=submenu_archivo, label="Archivo")
        menu_principal.add_cascade(menu=submenu_ayuda, label="Ayuda")
        # Mostrar el menú en la ventana principal
        self.config(menu=menu_principal)

    def abrir(self):
        #Abrir archivo para edición (lectura-escritura)
        #askopenfile (explorador para abrir archivo)
        self.archivo_activo = askopenfile(mode="r+")
        # Revisar si hay un archivo
        if not self.archivo_activo:
            return
        # Abrir el archivo en modo lectura/escritura como un recurso
        with open(self.archivo_activo.name, "r+") as self.archivo:
            # Eliminar el texto anterior (desde la primera linea hasta la ultima)
            self.campo_texto.delete(1.0, tk.END)
            #Leer el contenido del archivo
            texto = self.archivo.read()
            #Insertar el contenido del archivo (desde la primera línea)
            self.campo_texto.insert(1.0, texto)
            # Cambiar el título de la app
            self.title(f"*Editor - {self.archivo.name}")

    def guardar(self):
        pass

    def guardar_como(self):
        pass

    def analizar(self):
        pass

    def errores(self):
        pass

    def salir(self):
        self.quit()
        self.destroy()
        sys.exit()

    def manual_usuario(self):
        pass

    def manual_tecnico(self):
        pass

    def temas_ayuda(self):
        mensaje = """
        INFORMACIÓN DEL DESARROLLADOR
        Universidad de San Carlos de Guatemala
        Facultad de Ingeniería
        Lenguajes Formales y de Programación B-
        Nombre: Ana Lucia Fletes Ordóñez
        Carnet: 202010003
        Correo: 3590179910101@ingenieria.usac.edu.gt
        """
        messagebox.showinfo("Temas de ayuda", mensaje)

if __name__ == '__main__':
    ventana_principal = MenuPrincipal()
    ventana_principal.mainloop()