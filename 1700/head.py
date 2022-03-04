# Representamos la ruta del archivo como una cadena y la cantidad de lineas con
# un entero.
def head(ruta: str, n: int) -> None:
    """
    Dada la 'ruta' de un archivo y un numero de lineas 'n', imprime las
    primeras 'n' lineas de dicho archivo.

    Ejemplos:

    >>> head('lorem.txt', 1)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor

    >>> head('lorem.txt', 2)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis

    >>> head('/dev/null', 4)
    """
    with open(ruta, "r") as archivo:
        for _ in range(n):
            print(archivo.readline(), end="")
