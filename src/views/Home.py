import customtkinter as ctk
import tkinter as tk
from src.views.vars import *
from src.views.Persona import Persona
from src.views.SearchBar import SearchBar
from src.views.RegisterPersona import *
from src.views.Pedidos import *
from src.views.RegisterPedidos import *
from PIL import Image


# vars
letter_type = ("Helvetica",16,"bold")
color_white = "white"
color_btn="#FFEEAB"
color_text="#623307"
color_btn_hover="#FFFBE9"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Tienda")
        self.root.geometry("1200x600")

        # Configuración de la apariencia
        ctk.set_appearance_mode("light")

        # Crear un frame para la barra de navegación lateral
        self.nav_frame = ctk.CTkFrame(root, width=200, corner_radius=0, fg_color="#F3CC6A")
        self.nav_frame.pack(side="left", fill="y")

        # Crear un frame para el contenido principal
        self.main_content_frame = ctk.CTkFrame(root, corner_radius=0)
        self.main_content_frame.pack(side="right", fill="both", expand=True)
        
        self.up_bar()
        self.content_box()
        self.crear_btns()
        self.mostrar_persona()

    
    # Botones de navegación en la barra lateral
    def crear_btns(self):
        
        self.boton_user = ctk.CTkButton(self.nav_frame, height=50, corner_radius=50 ,font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_pedidos,)
        self.boton_user.pack(pady=20, padx=10, fill="x")
        
        self.boton_pedidos = ctk.CTkButton(self.nav_frame, text="Pedidos",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_pedidos,)
        self.boton_pedidos.pack(pady=10, padx=10, fill="x")

        self.boton_inventario = ctk.CTkButton(self.nav_frame, text="Inventario",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_inventario)
        self.boton_inventario.pack(pady=10, padx=10, fill="x")

        self.boton_clientes = ctk.CTkButton(self.nav_frame, text="Clientes",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_clientes)
        self.boton_clientes.pack(pady=10, padx=10, fill="x")

        self.boton_productos = ctk.CTkButton(self.nav_frame, text="Productos",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_productos)
        self.boton_productos.pack(pady=10, padx=10, fill="x")

        self.boton_empleados = ctk.CTkButton(self.nav_frame, font=letter_type,text="Empleados",fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_empleados)
        self.boton_empleados.pack(pady=10, padx=10, fill="x")
        
        self.boton_proveedores = ctk.CTkButton(self.nav_frame, font=letter_type,text="Proveedores",fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_proveedores)
        self.boton_proveedores.pack(pady=10, padx=10, fill="x")

        self.boton_facturas = ctk.CTkButton(self.nav_frame, text="Facturas",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_facturas)
        self.boton_facturas.pack(pady=10, padx=10, fill="x")

        self.boton_nominas = ctk.CTkButton(self.nav_frame, text="Nominas",font=letter_type, fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_facturas)
        self.boton_nominas.pack(pady=10, padx=10, fill="x")

        self.boton_control_pagos = ctk.CTkButton(self.nav_frame, text="Control Pagos",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_control_pagos)
        self.boton_control_pagos.pack(pady=10, padx=10, fill="x")
        
    
    def up_bar(self):
        self.up_bar = ctk.CTkFrame(master=self.main_content_frame)
        self.up_bar.configure(
            height=80,
            fg_color=blanco,
            corner_radius=0
        )
        self.up_bar.pack(side="top", fill="x")
        
        self.logo = ctk.CTkImage(light_image=Image.open("assets/logo.png"),size=(170,80))

        self.logoIn=ctk.CTkLabel(self.up_bar, text="", image=self.logo, width=170, height=80)
        self.logoIn.pack(side="right", padx=10,pady=10)
        
        self.pageTitle= ctk.CTkLabel(self.up_bar,
                                     text="Home",
                                     text_color=btnCafe,
                                     font=title_letter)
        self.pageTitle.pack(side="left",padx=20)    
        
        
    def change_title(self,textIn):
        self.pageTitle.configure(text=textIn)
    
        
    def content_box(self):
        self.content_box = ctk.CTkFrame(master=self.main_content_frame)
        self.content_box.configure(
            fg_color=fondoGr,
            corner_radius=0
        )
        self.content_box.pack(side="top", fill="both", expand= True)

        
    def mostrar_persona(self):
        
        self.limpiar_contenido()
        
        self.change_title("Personas")
        
        self.searchBar = SearchBar(master=self.content_box, text="Persona")
        self.searchBar.configure(height=50, fg_color=blanco)
        self.searchBar.btnRegister.configure(command=self.register_persona)
        self.searchBar.pack(side="top",padx=20,pady=10,fill="x")
        
        self.dataFrame = Persona(master=self.content_box)
        self.dataFrame.configure(fg_color=blanco)
        self.dataFrame.pack(side="top", padx=20, pady=10, fill="both", expand=True)

        
        
    def register_persona(self):
        
        self.limpiar_contenido()
        
        self.change_title("Registro Persona")    
         
        self.registerPersona = RegisterPersona(master=self.content_box, texto="Persona")
        self.registerPersona.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)
        self.registerPersona.btnAtras.configure(command=self.mostrar_persona)
    
    
    def register_cliente(self):
        self.limpiar_contenido()
        
        self.change_title("Registro Cliente")    
         
        self.registerPersona = RegisterCliente(master=self.content_box, texto="Cliente")
        self.registerPersona.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)
        self.registerPersona.btnAtras.configure(command=self.mostrar_clientes)
        
        
    def mostrar_pedidos(self):
        
        self.limpiar_contenido()
        
        self.change_title("Pedidos")
        
        self.searchBar = PedidosSearchBar(master=self.content_box,texto="Pedidos")
        self.searchBar.configure(height=50, fg_color=blanco)
        self.searchBar.btnRegister.configure(command=self.register_pedidos)
        self.searchBar.pack(side="top",padx=20,pady=5, fill="x")
        
        self.dataFrame = Pedidos(master=self.content_box)
        self.dataFrame.pack(side="top",padx=20,pady=10, fill="both", expand=True)
        

    def register_pedidos(self):
        
        self.limpiar_contenido()
        
        self.change_title("Registro Pedido")
        
        self.registerPedido= RegisterPedido(master=self.content_box, texto="Pedido")
        self.registerPedido.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.93)
        self.registerPedido.btnAtras.configure(command=self.mostrar_pedidos)
        


    def mostrar_inventario(self):
        
        self.change_title("Inventario")
        
        self.limpiar_contenido()


    def mostrar_clientes(self):
        self.limpiar_contenido()
        
        self.change_title("Clientes")
        
        self.searchBar = SearchBar(master=self.content_box, text="Persona")
        self.searchBar.configure(height=50, fg_color=blanco)
        self.searchBar.btnRegister.configure(command=self.register_cliente)
        self.searchBar.pack(side="top",padx=20,pady=10,fill="x")
        
        self.dataFrame = Persona(master=self.content_box)
        self.dataFrame.configure(height=500,width=700, fg_color=blanco)
        self.dataFrame.pack(side="top", padx=20, pady=10, fill="both", expand=True)
        
        
    def mostrar_empleados(self):
        self.limpiar_contenido()
        
        self.change_title("Empleados")
        
        self.searchBar = SearchBar(master=self.content_box, text="Persona")
        self.searchBar.configure(height=50, fg_color=blanco)
        self.searchBar.btnRegister.configure(command=self.register_empleado)
        self.searchBar.pack(side="top",padx=20,pady=10,fill="x")
        
        self.dataFrame = Persona(master=self.content_box)
        self.dataFrame.configure(height=500,width=700, fg_color=blanco)
        self.dataFrame.pack(side="top", padx=20, pady=10, fill="both", expand=True)
    
    
    def register_empleado(self):
        self.limpiar_contenido()
        
        self.change_title("Registro Empleado")    
         
        self.registerPersona = RegisterEmpleado(master=self.content_box, texto="Empleado")
        self.registerPersona.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)
        self.registerPersona.btnAtras.configure(command=self.mostrar_clientes)


    def mostrar_productos(self):
        
        self.change_title("Productos")
        
        self.limpiar_contenido()


    def mostrar_proveedores(self):
        self.limpiar_contenido()
        self.change_title("Proveedores")
        
        self.searchBar = SearchBar(master=self.content_box, text="Persona")
        self.searchBar.configure(height=50, fg_color=blanco)
        self.searchBar.btnRegister.configure(command=self.register_proveedor)
        self.searchBar.pack(side="top",padx=20,pady=10,fill="x")
        
        self.dataFrame = Persona(master=self.content_box)
        self.dataFrame.configure(height=500,width=700, fg_color=blanco)
        self.dataFrame.pack(side="top", padx=20, pady=10, fill="both", expand=True)

    def register_proveedor(self):
        self.limpiar_contenido()
        
        self.change_title("Registro Empleado")    
         
        self.registerPersona = RegisterProveedor(master=self.content_box, texto="Proveedor")
        self.registerPersona.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)
        self.registerPersona.btnAtras.configure(command=self.mostrar_proveedores)


    def mostrar_facturas(self):
        
        self.change_title("Facturas")
        
        self.limpiar_contenido()


    def mostrar_control_pagos(self):
        
        self.change_title("Control de Pagos")
        
        self.limpiar_contenido()


    def limpiar_contenido(self):
        for widget in self.content_box.winfo_children():
            widget.destroy()


# root = ctk.CTk()
# app = App(root)
# root.mainloop()