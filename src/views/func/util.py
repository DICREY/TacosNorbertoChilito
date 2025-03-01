def centrar_ventana(ventana,app_width,app_height):
    #win, siginifica que esta tomando los valores del sistema operativo, midiendo el largo y ancho de la pantalla
    win_width = ventana.winfo_screenwidth()
    win_height = ventana.winfo_screenheight()
    x = int((win_width/2)-(app_width/2))
    y = int((win_height/2)-(app_height/2))
    return ventana.geometry(f"{app_width}x{app_height}+{x}+{y}")
    