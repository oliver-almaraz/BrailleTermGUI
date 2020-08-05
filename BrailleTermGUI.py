#### BrailleTerm #####
#Juego sencillo para repasar signografía básica braille (español).
#Escrito en Python 3.8.3.
#Creado por Oliver Almaraz el 27/jul/2020
#Última modificación 5/ago/2020
#Reportar bugs: oliver.almaraz@gmail.com

#GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox #Si no se importa en específico este módulo, en Windows da problemas.
#Módulo para generar un número aleatorio.
import random

#Definición de los diccionarios.
todas_las_filas = {
    #Primera fila (a-j // 1-10)
    1:["a","\nO ·\n· ·\n· ·\n"],2:["b","\nO ·\nO ·\n· ·\n"],3:["c","\nO O\n· ·\n· ·\n"],4:["d","\nO O\n· O\n· ·\n"],5:["e","\nO ·\n· O\n· ·\n"],6:["f","\nO O\nO ·\n· ·\n"],7:["g","\nO O\nO O\n· ·\n"],8:["h","\nO ·\nO O\n· ·\n"],9:["i","\n· O\nO ·\n· ·\n"],10:["j","\n· O\nO O\n· ·\n"],
    #Segunda fila (k-t // 11-20)
    11:["k","\nO ·\n· ·\nO ·\n"],12:["l","\nO ·\nO ·\nO ·\n"],13:["m","\nO O\n· ·\nO ·\n"],14:["n","\nO O\n· O\nO ·\n"],15:["o","\nO ·\n· O\nO ·\n"],16:["p","\nO O\nO ·\nO ·\n"],17:["q","\nO O\nO O\nO ·\n"],18:["r","\nO ·\nO O\nO ·\n"],19:["s","\n· O\nO ·\nO ·\n"],20:["t","\n· O\nO O\nO ·\n"],
    #Tercera fila (u-z // 21-26)
    21:["u","\nO ·\n· ·\nO O\n"],22:["v","\nO ·\nO ·\nO O\n"],23:["w","\n· O\nO O\n· O\n"],24:["x","\nO O\n· ·\nO O\n"],25:["y","\nO O\n· O\nO O\n"],26:["z","\nO ·\n· O\nO O\n"],
    #Signos diacríticos (27-33)
    27:["ñ","\nO O\nO O\n· O\n"],28:["a´","\nO ·\nO O\nO O\n"],29:["e´","\n· O\nO ·\nO O\n"],30:["i´","\n· O\n· ·\nO ·\n"],31:["o´","\n· O\n· ·\nO O\n"],32:["u´","\n· O\nO O\nO O\n"],33:["u¨","\nO ·\nO O\n· O\n"],
    #Puntuación (34-43)
    34:[".","\n· ·\n· ·\nO ·\n"],35:[",","\n· ·\nO ·\n· ·\n"],36:[";","\n· ·\nO ·\nO ·\n"],37:[":","\n· ·\nO O\n· ·\n"],38:["?","\n· ·\nO ·\n· O\n"],39:["!","\n· ·\nO O\nO ·\n"],40:["(","\nO ·\nO ·\n· O\n"],41:[")","\n· O\n· O\nO ·\n"],42:["-","\n· ·\n· ·\nO O\n"],43:["*","\n· ·\n· O\nO ·\n"],
    #Números (0-9 // 44-53)
    44:["1","\n· O  O ·\n· O  · ·\nO O  · ·\n"],45:["2","\n· O  O ·\n· O  O ·\nO O  · ·\n"],46:["3","\n· O  O O\n· O  · ·\nO O  · ·\n"],47:["4","\n· O  O O\n· O  · O\nO O  · ·\n"],48:["5","\n· O  O ·\n· O  · O\nO O  · ·\n"],49:["6","\n· O  O O\n· O  O ·\nO O  · ·\n"],50:["7","\n· O  O O\n· O  O O\nO O  · ·\n"],51:["8","\n· O  O ·\n· O  O O\nO O  · ·\n"],52:["9","\n· O  · O\n· O  O ·\nO O  · ·\n"],53:["0","\n· O  · O\n· O  O O\nO O  · ·\n"]
}


##### Listas vacías para ser modificadas con funciones ######
letra = "\n· ·\n· ·\n· ·\n" #Mostrar letra vacía antes de seleccionar una opción.
op=[0,0,0,0,0,0] #Los Checkbuttons modifican uno de los elementos de esta lista al ser seleccionados. De qué elementos hayan sido cambiados a 1 dependerá el rango de letras que podrá ser mostrado.
resultado=[" "] #Almacena el resultado correcto para evaluarlo o corregirlo
rango = [0,0] #El rango de 'random', se actualiza según la lista "op" con la función 'actualizar_rango'
respuesta_anterior=[0] #Lista para almacenar la última letra presentada y evitar repetirla.

###### Interfaz gráfica ##########
#Esto debe estar antes de las funciones para definir variables. Su posición gráfica se define hasta que se empaquetan (.pack())
root = Tk()
root.title("BrailleTerm")
#root.iconbitmap('@/home/oliver/Documentos/BrailleTerm_estable/LinuxGUI_Ejecutable/icono.xbm') ###No pude convertir a xbm sin perder color del logo.
try:
    root.iconbitmap('icono.ico') ##Funciona en Windows
except:
    pass
try:
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icono.png')) ##Funciona en Linux
except:
    pass
frame = Frame(root)
braille = Label(frame, text=letra)
veredicto = Label(root,text="\n\n", fg="blue")
entry = Entry(root)
##### Termina sección de la interfaz gráfica ##########

##### Funciones del juego #####
def actualizar_rango():
    """Actualiza la lista 'rango' para que sirva de referencia a 'random' en la función 'generar_nueva_letra'"""
    if op == [1,0,0,0,0,0]:
        rango[0]=1
        rango[1]=10
    elif op == [0,1,0,0,0,0]:
        #Si solo la segunda opción se seleccionó
        rango[0]=11
        rango[1]=20
    elif op == [0,0,1,0,0,0]:
        #Si solo la tercera opción se seleccionó
        rango[0]=21
        rango[1]=26
    elif op == [0,0,0,1,0,0]:
        #Si solo la cuarta opción se seleccionó
        rango[0]=27
        rango[1]=33
    elif op == [0,0,0,0,1,0]:
        #Si solo la quinta opción se seleccionó
        rango[0]=34
        rango[1]=43
    elif op == [0,0,0,0,0,1]:
        #Si solo la fila 'números' se seleccionó
        rango[0]=44
        rango[1]=53
    elif op == [1,1,0,0,0,0]:
        #Si filas 1 y 2 seleccionadas
        rango[0]=1
        rango[1]=20
    elif op == [1,1,1,0,0,0]:
        #Si filas 1, 2 y 3 seleccionadas
        rango[0]=1
        rango[1]=26
    elif op == [1,1,1,1,0,0]:
        #Si filas 1 a 4 seleccionadas
        rango[0]=1
        rango[1]=33
    elif op == [1,1,1,1,1,0]:
        #Si filas 1 a 5 seleccionadas
        rango[0]=1
        rango[1]=43
    elif op == [1,1,1,1,1,1]:
        #todas las filas seleccionadas
        rango[0]=1
        rango[1]=53
    elif op == [0,1,1,0,0,0]:
        #Si filas 2 y 3 seleccionadas
        rango[0]=11
        rango[1]=26
    elif op == [0,0,1,1,0,0]:
        #Si filas 3 y 4 seleccionadas
        rango[0]=21
        rango[1]=33
    elif op == [0,0,0,1,1,0]:
        #Si filas 4 y 5 seleccionadas
        rango[0]=27
        rango[1]=43
    elif op == [0,0,0,0,1,1]:
        #Si filas 5 y 6 seleccionadas
        rango[0]=34
        rango[1]=53
    elif op == [0,1,1,1,0,0]:
        #Si filas 2 a 4 seleccionadas
        rango[0]=11
        rango[1]=33
    elif op == [0,1,1,1,1,0]:
        #Si filas 2 a 5 seleccionadas
        rango[0]=11
        rango[1]=43
    elif op == [0,1,1,1,1,1]:
        #Si filas 2 a 6 seleccionadas
        rango[0]=11
        rango[1]=53
    elif op == [0,0,1,1,1,0]:
        #Si filas 3 a 5 seleccionadas
        rango[0]=21
        rango[1]=43
    elif op == [0,0,1,1,1,1]:
        #Si filas 3 a 6 seleccionadas
        rango[0]=21
        rango[1]=53
    elif op == [0,0,0,1,1,1]:
        #Si filas 4 a 6 seleccionadas
        rango[0]=27
        rango[1]=53
    else:
        #Opciones saltadas. Crear todas las opciones para que funciones no consecutivas para que funcionen con 'random' sería muy laborioso y no son indispensables.
        rango[0]=0
        rango[1]=0
        resultado[0]=0
        braille.config(text="\n· ·\n· ·\n· ·\n")
        messagebox.showerror(title="Opción no soportada",message="Por favor elige una o varias opciones (filas) consecutivas.")
def generar_letra_aleatoria():
    """Usa random para generar una letra aleatoria con el rango dado. También modifica las listas externas 'rango', 'respuesta_anterior' y 'resultado'."""
    num = random.randint(rango[0],rango[1])
    while num == respuesta_anterior[0]: #Este bucle evitará presentar la misma letra dos veces seguidas.
        num = random.randint(rango[0],rango[1])
    respuesta_anterior[0] = num #Se almacena la nueva letra en la lista
    letra = todas_las_filas[num][1]
    braille.config(text=letra)
    resultado[0]=todas_las_filas[num][0]
def evaluar_respuesta():
    """Evalúa la respuesta, muestra el veredicto y, si es correcta, genera una nueva letra."""
    respuesta = entry.get()
    if respuesta == resultado[0]:
        veredicto.config(text="¡Correcto!\n¿Y ahora?\n",fg="blue")
        entry.delete(0, END)
        actualizar_rango()
        generar_letra_aleatoria()
    else:
        veredicto.config(text=f"Respuesta incorrecta\nLa respuesta era '{resultado[0]}'\n", fg="red")
def select(indice):
    """Al seleccionar un Checkbutton, modifica la lista 'opcion', y si la selección es válida muestra una primera letra braille."""
    if op[indice] == 0:
        op[indice]=1
    elif op[indice] == 1:
        op[indice]=0
    veredicto.config(text="\n\n")
    actualizar_rango()
    if rango[1] > 9: #Si hay una opción válida seleccionada...
        generar_letra_aleatoria()
def siguiente_letra():
    """En caso de respuesta equivocada, el botón 'siguiente' muestra una nueva letra."""
    generar_letra_aleatoria()
    veredicto.config(text="\n\n")
    entry.delete(0, END)


###Ventanas emergentes al inicio con información del juego y cómo jugarlo
info = messagebox.showinfo('Información', message="¡Bienvenido a BrailleTerm!\n\nEste es un juego sencillo que te ayudará a repasar signografía básica braille (español).")
info2 = messagebox.showinfo('Cómo jugar', message="Elige qué signos quieres estudiar, escribe tu respuesta, presiona 'Evaluar' y sabrás si tu respuesta fue correcta. Si lo fue, una nueva letra se mostrará automáticamente.\n\nSolo se muestran letras minúsculas. En el caso de letras con tilde o diéresis, escribe primero la letra sola y luego la tilde o la diéresis.\nEjemplo: a´, u¨.\n\nEn el caso de '¿?' y de '¡!', escribe solo el signo que cierra. ")

#####Ventana Principal#####
### Menú superior 
def vertabla():
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title("BrailleTerm - Tabla de signografía básica braille")
    try:
        ventana_tabla.iconbitmap('icono.ico') ##Funciona en Windows
    except:
        pass
    try:
        ventana_tabla.tk.call('wm', 'iconphoto', ventana_tabla._w, PhotoImage(file='icono.png')) ##Funciona en Linux
    except:
        pass
    canvas = Canvas(ventana_tabla,width = 880, height = 640)      
    canvas.pack()      
    img = PhotoImage(file="tabla_braille.gif")
    canvas.create_image(20,20, anchor=NW, image=img)
    ventana_tabla.mainloop()
def como_jugar():
    comojugar = tk.Toplevel()
    comojugar.title("BrailleTerm - Instrucciones")
    try:
        comojugar.iconbitmap('icono.ico') ##Funciona en Windows
    except:
        pass
    try:
        comojugar.tk.call('wm', 'iconphoto', comojugar._w, PhotoImage(file='icono.png')) ##Funciona en Linux
    except:
        pass
    with open("Instrucciones.txt", "r") as f:
        Label(comojugar, text=f.read(), anchor=NW).pack()
        comojugar.mainloop()
def about():
    leeme = tk.Toplevel()
    leeme.title("BrailleTerm - Acerca de este programa")
    try:
        leeme.iconbitmap('icono.ico') ##Funciona en Windows
    except:
        pass
    try:
        leeme.tk.call('wm', 'iconphoto', leeme._w, PhotoImage(file='icono.png')) ##Funciona en Linux
    except:
        pass
    with open("Leeme.txt", "r") as f:
        Label(leeme, text=f.read(), anchor=NW).pack()
        leeme.mainloop()

menubar=Menu(root)
root.config(menu=menubar)
opciones=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Opciones", menu=opciones)
opciones.add_command(label="Mostrar tabla braille",command=vertabla) #Se muestra una imagen (.gif) con la tabla de la signografía básica braille.
opciones.add_separator()
opciones.add_command(label="Salir",command=root.destroy)
ayuda=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Ayuda", menu=ayuda) #Enlace a un archivo de texto (.txt) para poderlo modificar a conveniencia.
ayuda.add_command(label="Cómo jugar",command=como_jugar) #Enlace a un archivo de texto (.txt).
ayuda.add_command(label="Acerca de este juego", command=about) #Enlace a un archivo de texto (.txt).
###### Termina Menú #####

elige = Label(root, text="\n¿Qué filas quieres repasar?\n   (Elige una o varias opciones sucesivas)   \n").pack()
Checkbutton(root,text="Primera fila (letras a-j)",command=lambda:select(0)).pack() #lambda permite pasar el comando con argumentos sin que se active automáticamente.
Checkbutton(root,text="Segunda fila (letras k-t)",command=lambda:select(1)).pack()
Checkbutton(root,text="Tercera fila (letras u-z)",command=lambda:select(2)).pack()
Checkbutton(root,text="Signos diacríticos (ñ, tildes y diéresis)",command=lambda:select(3)).pack()
Checkbutton(root,text="Signos de puntuación (más usados)",command=lambda:select(4)).pack()
Checkbutton(root,text="Números (0-9)",command=lambda:select(5)).pack()
queletra = Label(root,text='\n\n¿Qué letra, número\no signo de puntuación es?').pack()
frame.pack() #Se empaquetan los elementos definidos antes de las variables
braille.pack()
try:
    braille.config(font="Courier") #La fuente funciona bien en Windows pero no viene instalada por defecto en Linux
except:
    pass
braille.config(text=letra)
veredicto.pack()
entry.pack() 
vacuum1 = Label(root)
vacuum1.pack() 
boton = Button(root, text='Evaluar', command=evaluar_respuesta)
boton.pack()
siguiente = Button(root, text="Siguiente",command=siguiente_letra)
siguiente.pack()
vacuum = Label(root)
vacuum.pack()
#### Debe ir al final ###
root.mainloop()
####### FIN DEL SCRIPT #####
