from password import primer_intento, es_solucion, siguiente

intento_actual = primer_intento()

while not es_solucion(intento_actual):
    print(intento_actual)
    intento_actual = siguiente(intento_actual)

print(intento_actual)
