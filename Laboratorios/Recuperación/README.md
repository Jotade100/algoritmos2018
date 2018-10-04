# Proyecto de distribución de procesos usando Docker
En esta parte del repositorio podrá apreciar dos carpetas, que corren el mismo algoritmo de ordenamiento: Merge Sort. Uno lo ejecuta de manera local e imprime el resultado en pantalla, mientras que el otro usando Docker, distribuye los procesos en pequeñas instancias y lo guarda en un archivo llamado resultado.txt, creado al terminar el proceso.

## Docker
Para usar esta fase del proyecto, se utiliza el Dockerfile. Si desea usar un archivo de texto personalizado con sus propias cadenas, reemplazar el texto.txt en la carpeta app.
Si trata de ejecutar el código de manera manual ingresando personalmente al contenedor, deberá de reemplazar las líneas de código que contienen los nombres de los archivos .txt, de origen y destino removiendo el directorio app/. ëste fue puesto para la ejecución automática desde el Dockerfile.

Si usa Docker for Windows, puede utilizar los comandos a continuación para ejecutar el programa desde Docker.
* docker volume create algoritmia1
Se crea un volumen personalizado para persistir los datos luego de su ejecución. Puede cambiarle el nombre por uno que desee.

* docker image build -t algoritmia1:0.0  ProyectoMergeSortParalelo/
Crea la imagen. Puede cambiar el nombre o la versión. La dirección que se propone es donde se encuentra el Dockerfile.

* docker container run -v algoritmia1:/app/app/ algoritmia1:0.0
Ejecuta el contenedor según Dockerfile.

* docker volume inspect algoritmia1
Sirve para ver en qué carpeta se almacenan los archivos persistidos. La dirección se encuentra en la la línea que presenta las característcias siguientes:
"Mountpoint": "/mnt/sda1/var/lib/docker/volumes/algoritmia1/_data",


* docker-machine ssh default
Lo que hace es entrar a la máquina virtual de Docker.

* sudo su - y cd /mnt/sda1/var/lib/docker/volumes/algoritmia1/_data
Sirve para acceder a la carpeta donde estarán ubicados nuestros archivos.

* more resultado.txt
Sirve para leer el archivo de resultados de manera gradual.

