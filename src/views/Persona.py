import customtkinter as ctk
import tkinter as tk
from src.views.vars import *

class Persona (ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.titleFrame = ctk.CTkFrame(self, height=50,fg_color=blanco)
        self.titleFrame.pack(side="top", fill="x")
        
        
        self.nomBox = ctk.CTkFrame(self.titleFrame, height=40,fg_color=fondAma)
        self.nomBox.pack(side="left", fill="x",padx=20,pady=5)
        
        self.ccBox = ctk.CTkFrame(self.titleFrame, height=40,fg_color=fondAma)
        self.ccBox.pack(side="left", fill="x",padx=20,pady=5)
        
        self.dirBox = ctk.CTkFrame(self.titleFrame, height=40,fg_color=fondAma)
        self.dirBox.pack(side="left", fill="x",padx=20,pady=5)
        
        self.emailBox = ctk.CTkFrame(self.titleFrame, height=40,fg_color=fondAma)
        self.emailBox.pack(side="left", fill="x",padx=20,pady=5)
        
        self.datosFrame = ctk.CTkScrollableFrame(self, fg_color=blanco)
        self.datosFrame.pack(side="top",fill="both",expand=True)
        
        
    
    