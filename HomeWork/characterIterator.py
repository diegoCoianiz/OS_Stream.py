###########################################################################################################
                                                # FIRST WORK #
###########################################################################################################

# Escenario
# Un archivo de texto contiene algo de texto (nada inusual) pero necesitamos saber con qué frecuencia aparece 
# cada letra en el texto. Tal análisis puede ser útil en criptografía, por lo que queremos poder hacerlo en 
# referencia al alfabeto latino.

# Tu tarea es escribir un programa que:

# Pida al usuario el nombre del archivo de entrada.
# Lea el archivo (si es posible) y cuente todas las letras latinas (las letras mayúsculas y minúsculas se tratan 
# como iguales).
# Imprima un histograma simple en orden alfabético (solo se deben presentar recuentos distintos de cero).
# Crea un archivo de prueba para tu código y verifica si tu histograma contiene resultados válidos.
# El histograma de salida se ordenará en función de la frecuencia de los caracteres (el contador más grande 
# debe presentarse primero). El histograma debe enviarse a un archivo con el mismo nombre que el de entrada, 
# pero con la extensión '.hist' (debe concatenarse con el nombre original).

# Suponiendo que el archivo de prueba contiene solo una línea con:

# abBbcC   

# El resultado esperado debería verse de la siguiente manera:
# b -> 3
# c -> 2
# a -> 1

# Tip: Creemos que un diccionario es un medio perfecto de recopilación de datos para almacenar los recuentos. 
# Las letras pueden ser las claves mientras que los contadores pueden ser los valores.
# Emplea una lambda para el ordenamiento.

###########################################################################################################