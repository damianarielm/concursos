candidatos = [4] * 3 + [3] * 3 + [1] * 3
total = 6

def es_solucion(eleccion_actual):
    return sum(eleccion_actual) == total

def elegir_candidato():
    return max(candidatos)

def es_factible(eleccion):
    return sum(eleccion) <= total
