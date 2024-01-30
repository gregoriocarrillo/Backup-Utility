import os
import datetime
import shutil
import time

# Se definen las rutas de los directorios
root_dir = r"C:\Users\Greg\Desktop\code\Backup-Utility\My_script\carpeta-con-archivos"
backup_dir = r"F:\respaldo-archivos"

def respaldo():
    # Se establece el formato del archivo de respaldo con la marca de tiempo
    file_name = "Respaldo-" + datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S")

    # Se crea el archivo comprimido del directorio
    shutil.make_archive(file_name, "zip", root_dir)

    # Enviar los archivos a un directorio remoto 

    # Se crea una lista temporal que contendra el archivo comprimido creado
    lista = []

    #Con el modulo os revisa en el directorio el archivo existente
    archivos = os.listdir()

    # Se crea un bucle para encontrar los archivos que coincidan con la condicion y se agrega a la lista
    for a in archivos:
        if a.startswith("Respaldo") == True:
            lista.append(a)

    # Finalmente con un nuevo bucle se mueve el archivo a la nueva ubicacion
    for i in lista:
        shutil.move(i, backup_dir)

# Con el siguiente bucle se crea la tarea repetitiva segun lo que se necesite
# En este caso se repite cada 2 minutos
while True:
    respaldo()

    # Espera un segundo antes de repetir el ciclo
    time.sleep(120)
