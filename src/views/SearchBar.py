import customtkinter as ctk
import tkinter as tk
from src.views.vars import *

class SearchBar (ctk.CTkFrame):
    def __init__(self, master, text,**kwargs):
        super().__init__(master,**kwargs)
        
        self.input = ctk.CTkEntry(self,
                                placeholder_text=text,
                                border_width=0,
                                height=30,
                                width=200,
                                font=letter,
                                fg_color=gris)
        self.input.pack(side="left", fill="x", pady=5, padx=10)
        
        
        self.option = ctk.CTkComboBox(self, values=["Cedula", "Nombre","Telefono","Email"])
        self.option.pack(side="left", fill="x",pady=5,padx=10)
        
        self.btnSearch = ctk.CTkButton(self,
                            text="Buscar",
                            height=30,
                            font=letter,
                            fg_color=btnCafe,
                            hover_color=btnHoover)
        self.btnSearch.pack(side="left", fill="x", pady=5, padx=10)
        

        self.btnSearch = ctk.CTkButton(self,
                            text="+Registrar",
                            height=30,
                            font=letter,
                            fg_color=btnCafe,
                            hover_color=btnHoover)
        self.btnSearch.pack(side="right", fill="x", pady=5, padx=10)
        