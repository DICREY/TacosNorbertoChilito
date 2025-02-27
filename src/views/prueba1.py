import customtkinter as ctk
from src.views.vars import *
from PIL import Image
import os

#Declaracion Ventana
ventana = ctk.CTk()
ventana._set_appearance_mode("system")  # Modo inicial
ventana.title("Hola pe causa")
ventana.geometry("1280x720")
ventana.resizable(width=True,height =True)



#Validacion de usuario de prueba

def validar():
    usInp = userInput.get()
    psInp = pswInput.get()
    
    if (user==usInp and psw == psInp):
        print("pe")
    else:
        print("datos incorrectos")


#frame de la izquierda, funciona como una caja HTML y abajo su contenido
frame1= ctk.CTkFrame(master=ventana)
frame1.configure(width=600,
                height=200,
                border_width=0,
                fg_color=fondAma,
                corner_radius=0
                )
frame1.pack(side="left",expand=False, fill="both")

logo = ctk.CTkImage(light_image=Image.open("assets/logo.png"),size=(400,300))

logoIn=ctk.CTkLabel(frame1, text="", image=logo, width=200, height=200)
logoIn.place(relx=0.5, rely=0.45, anchor="center")

titleLog= ctk.CTkLabel(frame1, text="T.C.N.S. Demo version 0.1", font=('Helvetica',25,'bold'),text_color=btnCafe)
titleLog.place(relx=0.5, rely=0.7, anchor="center")

#Frame de la derecha

frame2 = ctk.CTkFrame(master=ventana)
frame2.configure(width=300,
                height=720,
                border_width=0,         
                fg_color=fondoGr,
                corner_radius=0
                )
frame2.pack(side="right",expand=True, fill="both")

title = ctk.CTkLabel(frame2,
                     text="Login",
                     font=title_letter,
                     text_color=btnCafe)
title.place(relx=0.5,rely=0.26,anchor="center")


titleUser = ctk.CTkLabel(frame2,
                     text="Nombre Usuario",
                     font=letter,
                     text_color=btnCafe)
titleUser.place(relx=0.35,rely=0.356,anchor="w")


titlePsw = ctk.CTkLabel(frame2,
                     text="Contraseña",
                     font=letter,
                     text_color=btnCafe)
titlePsw.place(relx=0.35,rely=0.456,anchor="w")

userInput = ctk.CTkEntry(frame2,
                         placeholder_text="Usuario",
                         border_width=0,
                         height=40,
                         font=letter,
                         fg_color=blanco)
userInput.place(relx=0.5,rely=0.4, anchor="center", relwidth=0.3)

pswInput = ctk.CTkEntry(frame2,
                         placeholder_text="Contraseña",
                         placeholder_text_color=gris,
                         font=letter,
                         border_width=0,
                         height=40,
                         fg_color=blanco)
pswInput.place(relx=0.5,rely=0.5, anchor="center", relwidth=0.3)

btnLog = ctk.CTkButton(frame2,
                       text="Ingresar",
                       height=40,
                       font=letter,
                       fg_color=btnCafe,
                       hover_color=btnHoover,
                       command=validar)
btnLog.place(relx=0.5,rely=0.6, anchor="center", relwidth=0.3)


ventana.mainloop()