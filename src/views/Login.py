import customtkinter as ctk
from vars import *
from PIL import Image
import os

#Declaracion Ventana


class Login(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        #Declaracion Ventana
        self._set_appearance_mode("system")  # Modo inicial
        self.title("Hola pe causa")
        self.geometry("1280x720")
        self.resizable(width=True,height =True)
        self.frameLogo()
        self.frameData()
    
    def frameLogo(self):
        #frame de la izquierda, funciona como una caja HTML y abajo su contenido
        self.frame1= ctk.CTkFrame(master=self)
        self.frame1.configure(width=600,
                        height=200,
                        border_width=0,
                        fg_color=fondAma,
                        corner_radius=0
                        )
        self.frame1.pack(side="left",expand=False, fill="both")

        logo = ctk.CTkImage(light_image=Image.open("assets/logo.png"),size=(400,300))

        logoIn=ctk.CTkLabel(self.frame1, text="", image=logo, width=200, height=200)
        logoIn.place(relx=0.5, rely=0.45, anchor="center")

        titleLog= ctk.CTkLabel(self.frame1, text="T.C.N.S. Demo version 0.1", font=('Helvetica',25,'bold'),text_color=btnCafe)
        titleLog.place(relx=0.5, rely=0.7, anchor="center")
    
    def frameData(self):
        #Frame de la derecha
        self.frame2 = ctk.CTkFrame(master=self)
        self.frame2.configure(width=300,
                        height=720,
                        border_width=0,         
                        fg_color=fondoGr,
                        corner_radius=0
                        )
        self.frame2.pack(side="right",expand=True, fill="both")

        title = ctk.CTkLabel(self.frame2,
                            text="Login",
                            font=title_letter,
                            text_color=btnCafe)
        title.place(relx=0.5,rely=0.26,anchor="center")


        titleUser = ctk.CTkLabel(self.frame2,
                            text="Nombre Usuario",
                            font=letter,
                            text_color=btnCafe)
        titleUser.place(relx=0.35,rely=0.356,anchor="w")


        titlePsw = ctk.CTkLabel(self.frame2,
                            text="Contraseña",
                            font=letter,
                            text_color=btnCafe)
        titlePsw.place(relx=0.35,rely=0.456,anchor="w")

        self.userInput = ctk.CTkEntry(self.frame2,
                                placeholder_text="Usuario",
                                border_width=0,
                                height=40,
                                font=letter,
                                fg_color=blanco)
        self.userInput.place(relx=0.5,rely=0.4, anchor="center", relwidth=0.3)

        self.pswInput = ctk.CTkEntry(self.frame2,
                                placeholder_text="Contraseña",
                                placeholder_text_color=gris,
                                font=letter,
                                border_width=0,
                                height=40,
                                fg_color=blanco)
        self.pswInput.place(relx=0.5,rely=0.5, anchor="center", relwidth=0.3)

        btnLog = ctk.CTkButton(self.frame2,
                            text="Ingresar",
                            height=40,
                            font=letter,
                            fg_color=btnCafe,
                            hover_color=btnHoover,
                            command=self.validar)
        btnLog.place(relx=0.5,rely=0.6, anchor="center", relwidth=0.3)
        
    #Validacion de usuario de prueba    
    def validar(self):
        usInp = self.userInput.get()
        psInp = self.pswInput.get()
        
        if (user==usInp and psw == psInp):
            print("pe")
        else:
            print("datos incorrectos")


login = Login()
login.mainloop()