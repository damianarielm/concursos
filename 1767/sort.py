problema = [3, 5, 22, 1, 0, 2, -1, 6, 7, 11]

def es_caso_base(problema):
    return len(problema) <= 1

def dividir(problema):
    mitad = len(problema) // 2
    return problema[:mitad], problema[mitad:]

def fusionar(solucion1, solucion2):
    solucion = []

    while solucion1 and solucion2:
        if solucion1[0] <= solucion2[0]:
            solucion.append(solucion1.pop(0))
        else:
            solucion.append(solucion2.pop(0))

    """
    if solucion1:
        return solucion + solucion1
    else:
        return solucion + solucion2
    """

    return solucion + (solucion1 if solucion1 else solucion2)
