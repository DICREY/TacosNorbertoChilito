import customtkinter as ctk
from src.views.vars import *

class RegisterPersona(ctk.CTkFrame):
    def __init__(self, master, texto, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=blanco)  # Fondo blanco


        # Frame para los campos de entrada
        self.dataFrame = ctk.CTkFrame(self, fg_color=blanco, corner_radius=0)
        self.dataFrame.pack(side="left", fill="both", expand=True, padx=20, pady=20, ipadx=20)
        
        # Configurar el sistema de grid en el frame dataFrame
        self.dataFrame.grid_columnconfigure(0, weight=1)  # Columna 0 (labels)
        self.dataFrame.grid_columnconfigure(1, weight=1)  # Columna 1 (entradas)
        self.dataFrame.grid_columnconfigure(2, weight=1)  
        self.dataFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)  # Filas

        # Título del formulario
        self.titulo = ctk.CTkLabel(self.dataFrame, text=f"Datos {texto}", font=title_letter)
        self.titulo.grid(row=0, column=1, columnspan=1, pady=10, sticky="s")

        # Campos de entrada organizados en un grid
        self.nombreInp = self.create_entry("Nombre", self.dataFrame, row=1)
        self.tipoDoc = self.create_entry("TipoDoc", self.dataFrame, row=2)
        self.DocInp = self.create_entry("Documento", self.dataFrame, row=3)
        self.celInp = self.create_entry("Celular", self.dataFrame, row=4)
        self.emailInp = self.create_entry("Correo Electronico", self.dataFrame, row=5)
        self.dirInp = self.create_entry("Dirección", self.dataFrame, row=6)
        self.cityInp = self.create_entry("Ciudad", self.dataFrame, row=7)
        self.barrioInp = self.create_entry("Barrio", self.dataFrame, row=8)
        self.paisInp = self.create_entry("País", self.dataFrame, row=9)


        # Botones
        self.btnLimpiar = self.create_button("Limpiar", self.dataFrame, fg_color=btnCafe, hover_color=btnHoover, row=10, col=1)
        self.btnRegister = self.create_button(f"Registrar {texto}", self.dataFrame, fg_color=btnCafe, hover_color=btnHoover, row=10, col=2)
        self.btnAtras= self.create_button("Atras", self.dataFrame, fg_color=btnCafe, hover_color=btnHoover, row=10, col=0)

    def create_entry(self, label_text, parent, row):
        label = ctk.CTkLabel(parent, text=label_text, font=letter)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="e")

        entry = ctk.CTkEntry(parent, height=30, fg_color=fondoGr, border_width=0)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        
        return entry

    def create_button(self, text, parent, fg_color, hover_color, row, col):
        button = ctk.CTkButton(parent, text=text, height=40, corner_radius=10,
                               fg_color=fg_color, hover_color=hover_color, font=letter)
        button.grid(row=row, column=col, pady=10, sticky="s")
        return button
    
class RegisterCliente(RegisterPersona):
    def __init__(self, master, texto, **kwargs):
        super().__init__(master, texto,**kwargs)


class RegisterProveedor(RegisterPersona):
    def __init__(self, master, texto, **kwargs):
        super().__init__(master, texto,**kwargs)
        
        
class RegisterEmpleado(RegisterPersona):
    def __init__(self, master, texto, **kwargs):
        super().__init__(master, texto,**kwargs)

