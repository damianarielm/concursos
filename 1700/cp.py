# Representamos las rutas de los archivos como cadenas y la cantidad de bytes
# con un entero.
def cp(ruta_org: str, ruta_dst, n: int) -> None:
    """
    Dada las rutas de los archivos origen y destino, copia como maximo 'n'
    bytes del archivo origen en la ruta destino.
    """
    with open(ruta_org, "rb") as origen:
        with open(ruta_dst, "wb") as destino:
            destino.write(origen.read(n))
