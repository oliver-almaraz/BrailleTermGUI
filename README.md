# BrailleTermGUI

Esta es la versión con interfaz gráfica de [BrailleTerm](https://github.com/oliver-almaraz/BrailleTerm).
Este programa es parte de un proyecto sin fines de lucro, se trata en general de un curso gratuito para
aprender signografía básica del braille en español destinado a usuarios videntes. Algo
peculiar de esta aplicación es que pasé cada letra braille a un dibujo con texto en lugar de usar los
signos Unicode, esto ayuda a que los signos braille se vean más grandes y se puedan cambiar de fuente.
Tal vez el solo diccionario con todas las letras y números te sirva para otro fin.
Próximos proyectos incluyen un curso de **musicografía** braille con su respectiva aplicación.

Mi finalidad era crear un programa simple que funcionara en casi cualquier plataforma, así que al inicio me
enfoqué en crear un [script que se ejecutara desde la terminal](https://github.com/oliver-almaraz/BrailleTerm) (de ahí el nombre del programa, 'BrailleTerm').
Sin embargo, no consideré que, al estar escrito en Pyton (3.8), los usuarios de Windows tendrían que descargar el intérprete.

Estando consciente de que la mayoría de los participantes del curso al que está dedicado este programa
usarían Windows, me tomé el tiempo para hacer esta versión con una **interfaz gráfica** con Tkinter y lo
empaqueté como un binario (.exe) para Windows y como un ejecutable para Linux.

## Cómo usarlo en Windows

Ve a la sección de [releases](https://github.com/oliver-almaraz/BrailleTermGUI/releases) y busca la versión para Windows.
Descarga el fichero comprimido que termina en **.zip**, ábrelo y dale doble click al ejecutable (**.exe**) ¡así de fácil!
El programa es *portable*, así que no es necesario instalarlo.

## Cómo usarlo en Linux (x64)

Ve a la sección de [releases](https://github.com/oliver-almaraz/BrailleTermGUI/releases) y busca la versión para Linux.
Descarga el fichero comprimido **BrailleTerm_LinuxGUI.tar.gz** y extrae la carpeta que contiene.
Asegúrate de que el ejecutable (dentro de la carpeta) tenga permisos de ejecución y dale doble click.
¡Listo! Si requieres una versión para Linux 32 bit contáctame.

También puedes ejecutar directamente el script Python, pero el módulo necesario **Tkinter** no está instalado
por defecto en Linux, así que deberás instalarlo primero (el método cambia para cada distro). Después, ve con el explorador
de archivos que use tu entorno de escritorio (Nautilus, Thunar, Dolphin, etc.) a la carpeta que extrajiste del *tar.gz*,
da click derecho en un lugar vacío y elige *terminal* o *abrir terminal aquí*.
Finalmente, escribe en la terminal:
>$ python3 nombre_del_archivo.py

**Nota:** es importante que el *working directory* de la terminal sea la carpeta del programa, o los íconos, imágenes y archivos
de texto no se mostrarán correctamente. Por otro lado, los documentos de texto que se incluyen en el directorio principal
(*Intrucciones.txt* y *Leeme.txt*) usan la codificación ANSI, que se ve bien desde Windows, pero en Linux podría dar problemas.
**Si los acentos y otros caractereres no se visualizan correctamente** al seleccionar las opciones de *ayuda* del menú superior,
extrae los archivos de texto que se encuentran el la carpeta comprimida **Archivos_txt_Linux.tar.gz** y reemplaza los documentos
*Instrucciones.txt* y *Leeme.txt* del directorio principal por esos.

## Android

Actualmente estoy trabajando en una versión para Android. Mientras tanto, es posible utilizar la versión original de BrailleTerm
para terminal en Android (descargando un intérprete Python desde la Play Store). Para más información, ve al [repositorio
dedicado a la versión de BrailleTerm para terminal](https://github.com/oliver-almaraz/BrailleTerm/blob/master/README.md#tambi%C3%A9n-se-puede-ejecutar-en-android).

## MacOS

Si no sabes cómo ejecutar el código fuente, puedo empaquetar el programa en un archivo **.app** para ser utilizado en MacOS. Si lo requieres, contáctame.

#### Para ejecutar el script.py desde la terminal
El intérprete Python que viene instalado por defecto en MacOS es problemático, así que si quieres ejecutar el código fuente
(desde la terminal o desde un editor) te sugiero descargar un paquete de instalación actualizado del sitio oficial de Python
(la sintaxis de BrailleTerm requiere Python 3.7 o superior).
Después, descomprime la carpeta del código, abre una terminal, y cambia el *working directory* a la carpeta en la que se enuentra.
(Si no estás acostumbrado a usar la terminal, te sugiero seguir este método: [Cómo abrir terminal con una carpeta específica en Mac OS](https://www.solvetic.com/tutoriales/article/6463-como-abrir-terminal-con-una-carpeta-especifica-en-mac-os/))
Por último, escribe en la terminal:
>$ python3 nombre_del_archivo.py

**Nota:** es importante que el *working directory* de la terminal sea la carpeta del programa, o los íconos, imágenes y archivos
de texto no se mostrarán correctamente.

Cualquier contribución es bienvenida:

#### Oliver Almaraz (México)
<oliver.almaraz@gmail.com>

## Capturas de pantalla:

### Windows 10

<img src="https://user-images.githubusercontent.com/69062188/89375504-64fcca80-d6b3-11ea-827f-0228bb504414.jpg" width="90%"></img> 



### Manjaro Linux

<img src="https://user-images.githubusercontent.com/69062188/89375507-6a5a1500-d6b3-11ea-9b93-d10d8a63b669.png" width="90%"></img> 
