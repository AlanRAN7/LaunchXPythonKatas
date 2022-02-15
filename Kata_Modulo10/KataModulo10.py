# TRACEBACKS
# Es el cuerpo del texto que puede apuntar al origen 
# (y al final) de un error no controlado. Comprender
# los componentes de un traceback hará que seas más eficaz
# al corregir errores o depurar un programa que no funciona
# bien.


# Al abrir un Notebook inexistente, sucederá lo siguiente:
# >>> open("/path/to/mars.jpg")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'

#ABRIR UN ARCHIVO INEXISTENTE
# def main():
#     open("/path/to/mars.jpg")

# if __name__ == '__main__':
#     main()
#Aparecerá el siguiente mensaje:
# $ python3 open.py
# Traceback (most recent call last):
#   File "/tmp/open.py", line 5, in <module>
#     main()
#   File "/tmp/open.py", line 2, in main
#     open("/path/to/mars.jpg")
# FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'

#Try y Except de los Bloques
#Es importante enviar un mensaje con el error que se espera,
# por lo tanto es importante es factible usar los bloques de código llamados:
# "Try" y "Except"
#Ejemplo 1:
# try:
#     open("config.txt")
# except FileNotFoundError:
#     print("¡No se pudo encontrar el archivo llamado: config.txt!")
#Ejemplo 2:
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")

# if __name__ == '__main__':
#     main()

#Si configuramos el .txt a un .py tendremos lo siguiente:
# $ python config.py
# Traceback (most recent call last):
#   File "/tmp/config.py", line 9, in <module>
#     main()
#   File "/tmp/config.py", line 3, in main
#     configuration = open('config.txt')
# IsADirectoryError: [Errno 21] Is a directory: 'config.txt'

#PARA CONTROLAR TODAS LAS EXCEPCIONES POSIBLES:
# def main():
#     try:
#         configuration = open('config.txt')
#     except Exception:
#         print("Couldn't find the config.txt file!")

#PARA LOS PROBLEMAS DE DIRECTORIO
# def main():
#     try:
    #     configuration = open('config.txt')
    # except FileNotFoundError:
    #     print("Couldn't find the config.txt file!")
    # except IsADirectoryError:
    #     print("Found config.txt but it is a directory, couldn't read it")

#EN CASO DE TENER UNA SOBRECARGA PARA PODER LEER EL ARCHIVO
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")
#     except (BlockingIOError, TimeoutError):
#         print("Filesystem under heavy load, can't complete reading configuration file")
#ES IMPORTANTE TENER EXCEPCIONES ESPECIFICOS

#SI NECESITAMOS TENER LA EXCEPCIÓN ASOCIADA, DEBEMOS DE TENER LA PALABRA CLAVE "as"
#EJEMPLO:
# >>> try:
# ...     open("mars.jpg")
# ... except FileNotFoundError as err:
# ...     print("got a problem trying to read the file:", err)
# ...
# got a problem trying to read the file: [Errno 2] No such file or directory: 'mars.jpg'

#EJEMPLO DEL USO DE EXCEPCIONES:
# def water_left(astronauts, water_left, days_left):
#     daily_usage = astronauts * 11
#     total_usage = daily_usage * days_left
#     total_water_left = water_left - total_usage
#     return f"Total water left after {days_left} days is: {total_water_left} liters"

# >>> water_left(5, 100, 2)
# 'Total water left after 2 days is: -10 liters'

# def water_left(astronauts, water_left, days_left):
#     daily_usage = astronauts * 11
#     total_usage = daily_usage * days_left
#     total_water_left = water_left - total_usage
#     if total_water_left < 0:
#         raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
#     return f"Total water left after {days_left} days is: {total_water_left} liters"

#     >>> water_left(5, 100, 2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 6, in water_left
# RuntimeError: There is not enough water for 5 astronauts after 2 days!

# try:
#     water_left(5, 100, 2)
# except RuntimeError as err:
#     alert_navigation_system(err)

#     >>> water_left("3", "200", None)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in water_left
# TypeError: can't multiply sequence by non-int of type 'NoneType'

# def water_left(astronauts, water_left, days_left):
#     for argument in [astronauts, water_left, days_left]:
#         try:
#             # If argument is an int, the following operation will work
#             argument / 10
#         except TypeError:
#             # TypError will be raised only if it isn't the right type 
#             # Raise the same exception but with a better error message
#             raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
#     daily_usage = astronauts * 11
#     total_usage = daily_usage * days_left
#     total_water_left = water_left - total_usage
#     if total_water_left < 0:
#         raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
#     return f"Total water left after {days_left} days is: {total_water_left} liters"

#     >>> water_left("3", "200", None)
# Traceback (most recent call last):
#   File "<stdin>", line 5, in water_left
# TypeError: unsupported operand type(s) for /: 'str' and 'int'

# During handling of the preceding exception, another exception occurred:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 9, in water_left
# TypeError: All arguments must be of type int, but received: '3'