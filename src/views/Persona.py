import customtkinter as ctk
import tkinter as tk
from src.views.vars import *

class Persona (ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Frame principal para los títulos
        self.titleFrame = ctk.CTkFrame(self, height=40, fg_color=blanco)
        self.titleFrame.pack(side="top", fill="x", padx=10, pady=10)
        self.titleFrame.pack_propagate(False)  # Evitar que los hijos afecten el tamaño

        # Configurar el grid en el titleFrame
        self.titleFrame.grid_columnconfigure((0,1, 2, 3), weight=3)
        self.titleFrame.grid_columnconfigure(4, weight=1)
        self.titleFrame.grid_rowconfigure(0, weight=1)

        # Frames internos con grid
        self.nomBox = ctk.CTkFrame(self.titleFrame, height=40, fg_color=fondAma)
        self.nomBox.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.ccBox = ctk.CTkFrame(self.titleFrame, height=40, fg_color=fondAma)
        self.ccBox.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.dirBox = ctk.CTkFrame(self.titleFrame, height=40, fg_color=fondAma)
        self.dirBox.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        self.emailBox = ctk.CTkFrame(self.titleFrame, height=40, fg_color=fondAma)
        self.emailBox.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
        
        self.nadaF = ctk.CTkFrame(self.titleFrame,height=50,border_color=btnCafe,corner_radius=0,fg_color=blanco)
        self.nadaF.grid(row=0, column=4, sticky="nsew")

        # Frame de abajo (scrollable)
        self.datosFrame = ctk.CTkScrollableFrame(self, fg_color=blanco)
        self.datosFrame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # Configurar el grid en el frame de abajo
        self.datosFrame.grid_columnconfigure(0, weight=1)
        self.datosFrame.grid_columnconfigure((1, 2, 3), weight=2)
        
        for i in range (1,12):
            self.frameN = ctk.CTkFrame(self.datosFrame,height=30,fg_color=fondAma)
            self.frameN.pack(side="top", fill="x", pady=10)
        
        
    
    