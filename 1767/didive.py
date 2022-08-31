from sort import problema, es_caso_base, dividir, fusionar

def resolver(problema):
    if es_caso_base(problema):
        return problema

    subproblema1, subproblema2 = dividir(problema)
    solucion1, solucion2 = resolver(subproblema1), resolver(subproblema2)

    return fusionar(solucion1, solucion2)

print(resolver(problema))
