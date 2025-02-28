import customtkinter as ctk
import tkinter as tk

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

        # Botones de navegación en la barra lateral
        self.boton_pedidos = ctk.CTkButton(self.nav_frame, text="Pedidos",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_pedidos,)
        self.boton_pedidos.pack(pady=10, padx=10, fill="x")

        self.boton_inventario = ctk.CTkButton(self.nav_frame, text="Inventario",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_inventario)
        self.boton_inventario.pack(pady=10, padx=10, fill="x")

        self.boton_clientes = ctk.CTkButton(self.nav_frame, text="Clientes",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_clientes)
        self.boton_clientes.pack(pady=10, padx=10, fill="x")

        self.boton_productos = ctk.CTkButton(self.nav_frame, text="Productos",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_productos)
        self.boton_productos.pack(pady=10, padx=10, fill="x")

        self.boton_proveedores = ctk.CTkButton(self.nav_frame, font=letter_type,text="Proveedores",fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_proveedores)
        self.boton_proveedores.pack(pady=10, padx=10, fill="x")

        self.boton_facturas = ctk.CTkButton(self.nav_frame, text="Facturas",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_facturas)
        self.boton_facturas.pack(pady=10, padx=10, fill="x")

        self.boton_control_pagos = ctk.CTkButton(self.nav_frame, text="Control Pagos",font=letter_type,fg_color=color_btn, text_color=color_text, hover_color=color_btn_hover ,command=self.mostrar_control_pagos)
        self.boton_control_pagos.pack(pady=10, padx=10, fill="x")

        # Frame para mostrar el contenido de los pedidos
        self.pedidos_frame = ctk.CTkFrame(self.main_content_frame, corner_radius=0)
        self.pedidos_frame.pack(fill="both", expand=True)

        # Ejemplo de lista de pedidos
        self.lista_pedidos = ctk.CTkLabel(self.pedidos_frame, text="Lista de Pedidos", font=letter_type)
        self.lista_pedidos.pack(pady=20)

        # Inicialmente mostrar la sección de pedidos
        self.mostrar_pedidos()

    def mostrar_pedidos(self):
        self.limpiar_contenido()
        self.lista_pedidos.pack(pady=20)

    def mostrar_inventario(self):
        self.limpiar_contenido()
        label = ctk.CTkLabel(self.main_content_frame, text="Contenido de Inventario", font=letter_type)
        label.pack(pady=20)

    def mostrar_clientes(self):
        self.limpiar_contenido()
        label = ctk.CTkLabel(self.main_content_frame, text="Contenido de Clientes", font=letter_type)
        label.pack(pady=20)

    def mostrar_productos(self):
        self.limpiar_contenido()
        label = ctk.CTkLabel(self.main_content_frame, text="Contenido de Productos", font=letter_type)
        label.pack(pady=20)

    def mostrar_proveedores(self):
        self.limpiar_contenido()
        label = ctk.CTkLabel(self.main_content_frame, text="Contenido de Proveedores", font=letter_type)
        label.pack(pady=20)

    def mostrar_facturas(self):
        self.limpiar_contenido()
        label = ctk.CTkLabel(self.main_content_frame, text="Contenido de Facturas", font=letter_type)
        label.pack(pady=20)

    def mostrar_control_pagos(self):
        self.limpiar_contenido()
        label = ctk.CTkLabel(self.main_content_frame, text="Contenido de Control de Pagos", font=letter_type)
        label.pack(pady=20)

    def limpiar_contenido(self):
        for widget in self.main_content_frame.winfo_children():
            widget.pack_forget()


# root = ctk.CTk()
# app = App(root)
# root.mainloop()