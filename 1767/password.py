alfabeto = "0123456789abcdefghijklmnopqrstuvwxyz"

def es_solucion(intento):
    return intento == "abcde"

def siguiente(intento = ""):
    if intento == alfabeto[-1] * len(intento):
        return alfabeto[0] * (len(intento) + 1)
    elif intento[-1] != alfabeto[-1]:
        return intento[:-1] + alfabeto[alfabeto.find(intento[-1]) + 1]
    else:
        return siguiente(intento[:-1]) + alfabeto[0]
