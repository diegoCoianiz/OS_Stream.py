from io import open
import os
from os import strerror

clear = lambda : os.system("cls")
clear()

###########################################################################################################
                                                # READ/ GET FILE
###########################################################################################################

def readLineParameter(x):
    try:
        counter = 0
        stream = open('new.txt', "rt")
        char = stream.read(1)
        while char != '':
            print(char, end='')
            counter += 1
            char = stream.read(x) #read recupera de a (x) cantidad de nuevos caracteres por cada iteracion
        print("\n\nCaracteres en el archivo:", counter)
    except IOError as e:
        print("Se produjo un error de E/S:", strerror(e.errno))

def readLineNoParameter():
    try:
        character_counter = line_counter = 0
        stream = open('new.txt', "rt")
        line = stream.readline()
        while line != '':
            line_counter += 1
            for char in line:
                print(char, end='')
                character_counter += 1
            line = stream.readline()
        stream.close()
        print("\n\nCaracteres en el archivo:", character_counter)
        print("Líneas en el archivo:     ", line_counter)
    except IOError as e:
        print("Se produjo un error de E/S:", strerror(e.errno))

def readLines():
    try:
        character_counter = line_counter = 0
        stream = open('new.txt', "rt")
        lines = stream.readlines(13) # devuelve el tamaño máximo del búfer de entrada aceptado
        print(lines)
        while len(lines) != 0:
            for line in lines:
                line_counter += 1
                for char in line:
                    print(char, end='')
                    character_counter += 1
            lines = stream.readlines() #devuelve el siguiente elemento, si *, necesariamente retorna vacio
            print(lines)
        stream.close()
        print("\n\nCaracteres en el archivo:", character_counter)
        print("Líneas en el archivo:     ", line_counter)
    except IOError as e:
        print("Se produjo un error de E/S:", strerror(e.errno))

def openIterable():
    try:
        character_counter = line_counter = 0
        for line in open('new.txt', "rt"): # en modo texto = es una instancia de la clase iterable.
            line_counter += 1
            for char in line:
                print(char, end='')
                character_counter += 1
        # invoca automáticamente a close() cuando cualquiera de las lecturas del archivo llega al final.
        print("\n\nCaracteres en el archivo: ", character_counter)
        print("Líneas en el archivo:     ", line_counter)
    except IOError as e:
        print("Se produjo un error de E/S:", strerror(e.errno))

###########################################################################################################
                                                # WRITE/CREATE/UPDATE FILE
###########################################################################################################

def write(new:bool):
    try:
        if new:
            file = open('newOne.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
        else:
            file = open('new.txt', 'wt') # se opera sobre el documento de siempre

        for i in range(10):
            s = "línea #" + str(i+1) + "\n"
            for char in s:
                file.write(char)
        file.close()
    except IOError as e:
        print("Se produjo un error de E/S:", strerror(e.errno))


###########################################################################################################
                                                # BYTEARRAY CREATE
###########################################################################################################

def byteArrayCreate():
    data = bytearray(10)
    for i in range(len(data)):
        data[i] = 10 + i

    try:
        binary_file = open('file.bin', 'wb')
        binary_file.write(data)
        binary_file.close()
    except IOError as e:
        print("Se produjo un error de E/S:", strerror(e.errno))

# Ingresa aquí el código que lee los bytes del stream :
# 
# 

###########################################################################################################
                                                # BYTEARRAY READ/GET
###########################################################################################################

def byteArrayReadInto():
    data = bytearray(10)

    try:
        binary_file = open('file.bin', 'rb')
        binary_file.readinto(data)
        binary_file.close()

        for b in data:
            print(hex(b), end=' ')
    except IOError as e:
        print("Se produjo un error de E/S:", strerror(e.errno))


# Ingresa aquí el código que lee los bytes del stream :
## 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0

def byteArrayRead():
    try:
        binary_file = open('file.bin', 'rb')
        data = bytearray(binary_file.read(5))
        binary_file.close()

        for b in data:
            print(hex(b), end=' ')

    except IOError as e:
        print("Se produjo un error de E/S:", strerror(e.errno))

###########################################################################################################
                                                # COPY FILES
###########################################################################################################


def copyFiles():

    source_file_name = input("Ingresa el nombre del archivo fuente: ")
    try:
        source_file = open(source_file_name, 'rb')
    except IOError as e:
        print("No se puede abrir archivo fuente: ", strerror(e.errno))
        exit(e.errno)	

    destination_file_name = input("Ingresa el nombre del archivo destino: ")
    try:
        destination_file = open(destination_file_name, 'wb')
    except Exception as e:
        print("No se puede crear el archivo de destino:", strerror(e.errno))
        source_file.close()
        exit(e.errno)	

    buffer = bytearray(65536)
    total  = 0
    try:
        readin = source_file.readinto(buffer)
        while readin > 0:
            written = destination_file.write(buffer[:readin])
            total += written
            readin = source_file.readinto(buffer)
    except IOError as e:
        print("No se puede crear el archivo de destino: ", strerror(e.errno))
        exit(e.errno)	
        
    print(total,'byte(s) escritos con éxito')
    source_file.close()
    destination_file.close()

copyFiles()
