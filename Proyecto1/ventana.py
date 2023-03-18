import sys
import tkinter as tk
from tkinter import messagebox, Menu
from tkinter.filedialog import askopenfile, asksaveasfilename

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        # Ventana principal
        self.geometry("600x500")
        self.title("Menú principal")
        self.iconbitmap("img/flor.ico")
        # Hacer que la ventana no pueda cambiar su tamaño
        self.resizable(0, 0)
        self.crear_menu()
        self.campo_texto = tk.Text(self)
        # Atributo de archivo (ruta)
        self.archivo = None
        # Atributo para saber si ya se abrió un archivo anteriormente
        self.archivo_activo = False
        #Creación de componentes
        self.crear_componentes()

    # Crear el componente de scroll y configurar el cuadro de texto
    def crear_componentes(self):
        scroll = tk.Scrollbar(self)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.campo_texto.pack(side=tk.LEFT, fill=tk.Y)
        scroll.config(command=self.campo_texto.yview)
        self.campo_texto.config(yscrollcommand=scroll.set)

    def crear_menu(self):
        # Crear el menú principal
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
        # Abrir archivo para edición (lectura-escritura)
        # askopenfile (explorador para abrir archivo)
        self.archivo_activo = askopenfile(mode="r+")
        # Verificar si se seleccionó un archivo a abrir
        if not self.archivo_activo:
            return
        # Abrir el archivo en modo lectura/escritura como un recurso
        with open(self.archivo_activo.name, "r+") as self.archivo:
            # Eliminar el texto anterior (desde la primera línea hasta la última)
            self.campo_texto.delete(1.0, tk.END)
            # Leer el contenido del archivo y guardarlo en la variable texto
            texto = self.archivo.read()
            # Insertar el contenido del archivo (desde la primera línea)
            self.campo_texto.insert(1.0, texto)
            # Cambiar el título de la app
            self.title(f"*Editor - {self.archivo.name}")

    def guardar(self):
        # Si ya se abrió anteriormente un archivo se va a sobreescribe
        if self.archivo_activo:
            # Abrir el archivo en modo escritura como un recurso
            with open(self.archivo_activo.name, "w") as self.archivo:
                # Leer el contenido del cuadro de texto por completo
                texto = self.campo_texto.get(1.0, tk.END)
                # Escribir el contenido del cuadro de texto en el mismo archivo
                self.archivo.write(texto)
                # Cambiar el título de la app
                self.title(f"Editor - {self.archivo.name}")
        else:
            self.guardar_como()

    def guardar_como(self):
        # Guardar el archivo actual como un nuevo archivo
        # Configuración respecto a la extensión del archivo
        self.archivo = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        # Verificar si se va a guardar un archivo
        if not self.archivo:
            return
        # Abrir el archivo en modo escritura como un recurso
        with open(self.archivo, "w") as self.archivo:
            #Leer el contenido del cuadro de texto por completo
            texto = self.campo_texto.get(1.0, tk.END)
            #Escribir el contenido en el nuevo archivo
            self.archivo.write(texto)
            # Cambiar el título de la app
            self.title(f"Editor - {self.archivo.name}")
            #Indicar que ya se abrió un archivo
            self.archivo_activo = self.archivo
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