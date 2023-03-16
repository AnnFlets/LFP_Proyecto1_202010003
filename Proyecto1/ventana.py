import sys
import tkinter as tk
from tkinter import messagebox, Menu

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        # Ventana principal
        self.geometry("300x300")
        self.title("Menú principal")
        self.iconbitmap("img/flor.ico")
        # Hacer que la ventana no pueda cambiar su tamaño
        self.resizable(0, 0)
        self.crear_menu()
        self.agregar_imagen()

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
        pass

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