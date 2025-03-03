import customtkinter as ctk
import tkinter as tk
from src.views.vars import *

class RegisterPersona (ctk.CTkFrame):
    def __init__(self, master, texto,**kwargs):
        super().__init__(master,**kwargs)
        
        self.dataInput = ctk.CTkFrame(self,
                                      fg_color=blanco,
                                      corner_radius=0)
        self.dataInput.pack(side="left",fill="both",expand=True)
        
        self.typedoc = ctk.CTkLabel(self.dataInput,
                                    text="CC o NIT",)
        self.typedoc.pack(side="top",padx=10,pady=10)
        self.docInp = ctk.CTkEntry(self.dataInput,
                                   height=30,
                                   fg_color=gris)
        self.docInp.pack(side="top",padx=10,pady=10)
        
        self.nom = ctk.CTkLabel(self.dataInput,
                                    text="Nombre",)
        self.nom.pack(side="top",padx=10,pady=10)
        self.nomInp = ctk.CTkEntry(self.dataInput,
                                   height=30,
                                   fg_color=gris)
        self.nomInp.pack(side="top",padx=10,pady=10)

        self.dir = ctk.CTkLabel(self.dataInput,
                                    text="Direccion",)
        self.dir.pack(side="top",padx=10,pady=10)
        self.dirInp = ctk.CTkEntry(self.dataInput,
                                   height=30,
                                   fg_color=gris)
        self.dirInp.pack(side="top",padx=10,pady=10)

        self.tel = ctk.CTkLabel(self.dataInput,
                                    text="Telefono",)
        self.tel.pack(side="top",padx=10,pady=10)
        self.telInp = ctk.CTkEntry(self.dataInput,
                                   height=30,
                                   fg_color=gris)
        self.telInp.pack(side="top",padx=10,pady=10)

        self.city = ctk.CTkLabel(self.dataInput,
                                    text="Ciudad",)
        self.city.pack(side="top",padx=10,pady=10)
        self.cityInp = ctk.CTkEntry(self.dataInput,
                                   height=30,
                                   fg_color=gris)
        self.cityInp.pack(side="top",padx=10,pady=10)

        self.pais = ctk.CTkLabel(self.dataInput,
                                    text="Pais",)
        self.pais.pack(side="top",padx=10,pady=10)
        self.paisInp = ctk.CTkEntry(self.dataInput,
                                   height=30,
                                   fg_color=gris)
        self.paisInp.pack(side="top",padx=10,pady=10)
        
        
        self.btnInput = ctk.CTkFrame(self,
                                     fg_color=blanco,
                                     corner_radius=0,
                                     width=100)
        self.btnInput.pack(side="right", fill="both")
        
        self.btnRegister = ctk.CTkButton(self.btnInput,
                                         height=50,
                                         corner_radius=10,
                                         fg_color=btnCafe,
                                         text=f"Registrar {texto}")
        self.btnRegister.pack(side="top", fill="x")