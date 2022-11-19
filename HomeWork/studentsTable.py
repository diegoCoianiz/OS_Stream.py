###########################################################################################################
                                                # SECOND WORK #
###########################################################################################################

#Escenario 
# El profesor Jekyll dirige clases con estudiantes y regularmente toma notas en un archivo de texto. 
# Cada línea del archivo contiene 3 elementos: el nombre del alumno, el apellido del alumno y el número de 
# puntos que el alumno recibió durante ciertas clases.
# Los elementos están separados con espacios en blanco. Cada estudiante puede aparecer más de una vez dentro 
# del archivo del profesor Jekyll.
# El archivo puede tener el siguiente aspecto:

# John	Smith	5
# Anna	Boleyn	4.5
# John	Smith	2
# Anna	Boleyn	11
# Andrew	Cox	1.5

# Tu tarea es escribir un programa que:

# Pida al usuario el nombre del archivo del profesor Jekyll.
# Lea el contenido del archivo y cuenta la suma de los puntos recibidos por cada estudiante.
# Imprima un informe simple (pero ordenado), como este:
# Andrew Cox 	 1.5
# Anna Boleyn 	 15.5
# John Smith 	 7.0

# Nota:
# Tu programa debe estar completamente protegido contra todas las fallas posibles: la inexistencia del archivo, el vacío del archivo o cualquier falla en los datos de entrada; encontrar cualquier error de datos debería causar la terminación inmediata del programa, y lo erróneo deberá presentarse al usuario.
# Implementa y usa tu propia jerarquía de excepciones: la presentamos en el editor; la segunda excepción se debe generar cuando se detecta una línea incorrecta y la tercera cuando el archivo fuente existe pero está vacío.
# Tip: Emplea un diccionario para almacenar los datos de los estudiantes.

class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    # Escribe tu código aquí.
    pass


class FileEmpty(StudentsDataException):
    # Escribe tu código aquí.
    pass