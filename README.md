# BrailleTermGUI

Este programa es parte de un proyecto sin fines de lucro, se trata en general de un curso gratuito para
aprender signografía básica del braille en español destinado a usuarios videntes. Algo
peculiar de esta aplicación es que pasé cada letra braille a un dibujo con texto en lugar de usar los
signos Unicode, esto ayuda a que los signos braille se vean más grandes y se puedan cambiar de fuente.
Tal vez el solo diccionario con todas las letras y números te sirva para otro fin.
Próximos proyectos incluyen un curso de **musicografía** braille con su respectiva aplicación.

Mi finalidad era crear un programa simple que funcionara en casi cualquier plataforma, así que al inicio me
enfoqué en crear un script que se ejecutara desde la terminal sin complicaciones (de ahí el nombre del
programa, 'BrailleTerm'). Sin embargo, no consideré que, al estar escrito en Pyton (3.8), los usuarios de
Windows tendrían que descargar el intérprete.

Estando consciente de que la mayoría de los participantes del curso al que está dedicado este programa
usarían Windows, me tomé el tiempo para hacer esta versión con una interfaz gráfica con Tkinter y lo
empaqueté como un binario (.exe) para Windows y como un ejecutable para Linux.

## Cómo usarlo en Windows

Ve a la sección de [releases](https://github.com/oliver-almaraz/BrailleTermGUI/releases) y busca la versión para Windows.
Descarga el fichero comprimido que termina en **.zip**, ábrelo y dale doble click ¡así de fácil!
El programa es *portable*, así que no es necesario instalarlo.

## Cómo usarlo en Linux (x64)

Ve a la sección de [releases](https://github.com/oliver-almaraz/BrailleTermGUI/releases) y busca la versión para Linux.
Descarga el fichero comprimido que termina en **.tar.gz** y extrae la carpeta que contiene.
Asegúrate de que el ejecutable (dentro de la carpeta) tenga permisos de ejecución y dale doble click.
¡Listo! Si requieres una versión para Linux 32 bit contáctame.

Nota: también puedes ejecutar directamente el script Python, pero el módulo necesario **Tkinter** no está instalado
por defecto en Linux, deberás ibstalarlo primero. Después, escribe en la terminal:
>$ python3 /ruta/del/archivo.py

## Android

Actualmente estoy trabajando en una versión para Android. Mientras tanto es posible utilizar la versión de BrailleTerm
para terminal en Android (descargando un intérprete Python desde la Play Store). Para más información, ve al repositorio
dedicado a la versión de BrailleTerm para terminal.

Cualquier contribución es bienvenida:

#### Oliver Almaraz (México)
oliver.almaraz@gmail.com

## Screenshots:

### Windows 10

<img src="https://user-images.githubusercontent.com/69062188/89375504-64fcca80-d6b3-11ea-827f-0228bb504414.jpg" width="90%"></img> 



### Manjaro Linux

<img src="https://user-images.githubusercontent.com/69062188/89375507-6a5a1500-d6b3-11ea-9b93-d10d8a63b669.png" width="90%"></img> 
