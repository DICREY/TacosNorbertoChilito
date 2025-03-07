import customtkinter as ctk
from src.views.vars import *
from src.views.SearchBar import SearchBar
from src.models.pedidos import Pedido

class Pedidos(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=blanco)  # Fondo blanco
        # Configuración de la apariencia


        # Frame principal
        self.main_frame = ctk.CTkFrame(self, fg_color=blanco)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame de arriba (dividido en un grid)
        self.top_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent",height=50)
        self.top_frame.pack(fill="x", padx=10, pady=10)
        self.top_frame.pack_propagate(False)  # Evitar que los hijos afecten el tamaño


        # Configurar el grid en el frame de arriba
        self.top_frame.grid_columnconfigure( 0, weight=1)
        self.top_frame.grid_columnconfigure((1,2,3,4,5,6), weight=1)
        self.top_frame.grid_columnconfigure( 5, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)

        # Agregar widgets al frame de arriba
        self.fechaF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=10,fg_color=fondAma)
        self.fechaF.grid(row=0, column=0, sticky="nsew")
        self.fechaL = ctk.CTkLabel(self.fechaF, text="Fecha", text_color=btnCafe,font=letter2,anchor="w", fg_color="transparent",bg_color="transparent",)
        self.fechaL.pack(side="left",pady=5,padx=15)

        self.clienteF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=10,fg_color=fondAma)
        self.clienteF.grid(row=0, column=1, sticky="nsew")
        self.clienteL = ctk.CTkLabel(self.clienteF, text="Cliente", text_color=btnCafe, font=letter2,anchor="w", fg_color="transparent", bg_color="transparent")
        self.clienteL.pack(side="left",pady=5,padx=20)

        self.celF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=10,fg_color=fondAma)
        self.celF.grid(row=0, column=2, sticky="nsew")
        self.celL = ctk.CTkLabel(self.celF, text="Celular", font=letter2, text_color=btnCafe, anchor="w", fg_color="transparent", bg_color="transparent")
        self.celL.pack(side="left",pady=5,padx=10)

        self.estadoF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=10,fg_color=fondAma)
        self.estadoF.grid(row=0, column=3, sticky="nsew")
        self.estadoL = ctk.CTkLabel(self.estadoF, text="Estado", font=letter2, text_color=btnCafe, anchor="w", fg_color="transparent", bg_color="transparent")
        self.estadoL.pack(side="left",pady=5,padx=10)

        self.paisF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=10,fg_color=fondAma)
        self.paisF.grid(row=0, column=4, sticky="nsew")
        self.paisL = ctk.CTkLabel(self.paisF, text="Pais", font=letter2,
        text_color=btnCafe, anchor="w", fg_color="transparent", bg_color="transparent")
        self.paisL.pack(side="left",pady=5,padx=10)

        self.obserF = ctk.CTkFrame(self.top_frame,height=50,border_color=btnCafe,corner_radius=10,fg_color=fondAma)
        self.obserF.grid(row=0, column=5, sticky="nsew")
        self.obserL = ctk.CTkLabel(self.obserF, text="Observación", text_color=btnCafe, font=letter2,anchor="w", fg_color="transparent", bg_color="transparent")
        self.obserL.pack(side="left",pady=5,padx=10)

        # Frame de abajo (scrollable)
        self.bottom_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color=blanco)
        self.bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Configurar el grid en el frame de abajo
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure((1,2,3,4), weight=2)
        self.bottom_frame.grid_columnconfigure(5, weight=1)

        # Agregar widgets al frame de abajo (scrollable)
        order = Pedido()
        pedido = order.buscar_pedidos_pendientes()
        if pedido:
            row = 0
            for i in pedido:
                column = 0
                for p in i:
                    self.label = ctk.CTkLabel(self.bottom_frame, font=letter,text=f"{p}")
                    self.label.grid(row=row, column=column, padx=10, pady=5,sticky="w")
                    column += 1
                row += 1
                print(i)

class PedidosSearchBar(SearchBar):
    def __init__(self, master, texto,**kwargs):
        super().__init__(master,texto,**kwargs)    
        
        self.option.configure(values=["Cliente", "Fecha","Valor", "Estado"])
        self.option.set("Cliente")
        
