from password import es_solucion, siguiente

intento_actual = siguiente()

while not es_solucion(intento_actual):
    print(intento_actual)
    input()
    intento_actual = siguiente(intento_actual)

print(intento_actual)
