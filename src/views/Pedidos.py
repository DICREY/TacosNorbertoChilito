import customtkinter as ctk
from src.views.vars import *
from src.views.SearchBar import SearchBar

class Pedidos(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=blanco)  # Fondo blanco
        # Configuración de la apariencia


        # Frame principal
        self.main_frame = ctk.CTkFrame(self, fg_color=blanco)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame de arriba (dividido en un grid)
        self.top_frame = ctk.CTkFrame(self.main_frame, fg_color=fondAma,height=50)
        self.top_frame.pack(fill="x", padx=10, pady=10)
        self.top_frame.pack_propagate(False)  # Evitar que los hijos afecten el tamaño


        # Configurar el grid en el frame de arriba
        self.top_frame.grid_columnconfigure( 0, weight=1)
        self.top_frame.grid_columnconfigure((1,2,3,4), weight=4)
        self.top_frame.grid_columnconfigure( 5, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)

        # Agregar widgets al frame de arriba
        self.codigoF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=0,fg_color=fondAma)
        self.codigoF.grid(row=0, column=0, sticky="nsew")
        self.codigoL = ctk.CTkLabel(self.codigoF, text="Codigo", font=letter2,anchor="w", fg_color="transparent", bg_color="transparent")
        self.codigoL.pack(side="left",pady=5,padx=10)


        self.nombreF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=0,fg_color=fondAma2)
        self.nombreF.grid(row=0, column=1, sticky="nsew")
        self.nombreL = ctk.CTkLabel(self.nombreF, text="Nombre", font=letter2,anchor="w", fg_color="transparent", bg_color="transparent")
        self.nombreL.pack(side="left",pady=5,padx=10)


        self.clienteF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=0,fg_color=fondAma)
        self.clienteF.grid(row=0, column=2, sticky="nsew")
        self.clienteL = ctk.CTkLabel(self.clienteF, text="Cliente", font=letter2,anchor="w", fg_color="transparent", bg_color="transparent")
        self.clienteL.pack(side="left",pady=5,padx=10)


        self.estadoF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=0,fg_color=fondAma2)
        self.estadoF.grid(row=0, column=3, sticky="nsew")
        self.estadoL = ctk.CTkLabel(self.estadoF, text="Estado", font=letter2,anchor="w", fg_color="transparent", bg_color="transparent")
        self.estadoL.pack(side="left",pady=5,padx=10)

        self.fechaF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=0,fg_color=fondAma)
        self.fechaF.grid(row=0, column=4, sticky="nsew")
        self.fechaL = ctk.CTkLabel(self.fechaF, text="Fecha", font=letter2,anchor="w", fg_color="transparent", bg_color="transparent")
        self.fechaL.pack(side="left",pady=5,padx=10)

        self.nadaF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=0,fg_color=fondAma)
        self.nadaF.grid(row=0, column=5, sticky="nsew")

        # Frame de abajo (scrollable)
        self.bottom_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color=blanco)
        self.bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Configurar el grid en el frame de abajo
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure((1,2,3,4), weight=2)

        # Agregar widgets al frame de abajo (scrollable)
        for i in range(20):  # Ejemplo: 20 widgets en el frame scrollable
            label = ctk.CTkLabel(self.bottom_frame, text=f"Elemento {i + 1}", font=letter)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")


class PedidosSearchBar(SearchBar):
    def __init__(self, master, texto,**kwargs):
        super().__init__(master,texto,**kwargs)    

