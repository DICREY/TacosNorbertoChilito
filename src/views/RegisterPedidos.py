import customtkinter as ctk
from src.views.vars import *

class RegisterPedido(ctk.CTkFrame):
    def __init__(self, master, texto, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=blanco)  # Fondo blanco


        # Frame para los campos de entrada
        self.dataFrame = ctk.CTkFrame(self, fg_color=blanco, corner_radius=0)
        self.dataFrame.pack(side="left", fill="both", expand=True, padx=20, pady=20, ipadx=20)
        
        # Configurar el sistema de grid en el frame dataFrame
        self.dataFrame.grid_columnconfigure((0,1,2), weight=1)  # Columna 0 (labels)
        self.dataFrame.grid_rowconfigure((0, 1, 2, 3), weight=1)  # Filas
        
        # Boton atras
        self.btnAtras= ctk.CTkButton(self.dataFrame, fg_color=btnCafe,height=40, hover_color=btnHoover,text="Atras")
        self.btnAtras.grid(row=3, column=1)
        
        self.btnContinuar= ctk.CTkButton(self.dataFrame, fg_color=fondAma,height=40,text_color=blanco, hover_color=fondAma2,text="Continuar")
        self.btnContinuar.grid(row=3, column=2)


        self.clienteFrame = ctk.CTkFrame(self.dataFrame, fg_color=blanco)
        self.clienteFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.clienteTit = ctk.CTkLabel(self.clienteFrame, text="Cliente", font=letter2,fg_color="transparent", anchor="w")
        self.clienteTit.pack(side="top", fill="x")
        self.clienteInp = ctk.CTkEntry(self.clienteFrame, fg_color=grisEntry,height=30, placeholder_text="Cliente")
        self.clienteInp.pack(side="top", fill="both", expand=True)
                
        # Frame para el producto
        self.productoFrame = ctk.CTkFrame(self.dataFrame, fg_color=blanco)
        self.productoFrame.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)
        self.productoTit = ctk.CTkLabel(self.productoFrame, text="Producto", font=letter2, fg_color="transparent", anchor="w")
        self.productoTit.pack(side="top", fill="x")
        self.productoInp = ctk.CTkEntry(self.productoFrame, fg_color=grisEntry, height=30, placeholder_text="Producto")
        self.productoInp.pack(side="top", fill="both", expand=True)

        # Frame para las observaciones
        self.obserFrame = ctk.CTkFrame(self.dataFrame, fg_color=blanco)
        self.obserFrame.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)
        self.obserTit = ctk.CTkLabel(self.obserFrame, text="Observaciones", font=letter2, fg_color="transparent", anchor="w")
        self.obserTit.pack(side="top", fill="x")
        self.obserInp = ctk.CTkTextbox(self.obserFrame, fg_color=grisEntry)
        self.obserInp.pack(side="top", fill="both", expand=True)
        
        self.fechaFrame = ctk.CTkFrame(self.dataFrame, fg_color=grisEntry)
        self.fechaFrame.grid(row=1, rowspan=2, column=2, sticky="nswe", padx=10)
        
        self.desFrame = ctk.CTkFrame(self.dataFrame, fg_color=grisEntry)
        self.desFrame.grid(row=2, column=0, sticky="nswe", padx=10)