import time  # Importamos la librería para medir tiempo

#Funcion de ordenamiento de menor a mayor.
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
#Busqueda Binaria.
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio  # Lo encontró, devuelve la posición
        elif objetivo < lista[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return -1  # No lo encontró

#  Programa principal 
print("Ingresá 20 números enteros separados por coma (ej: 5,2,9,1,3,...)")
entrada = input(" ")
numeros = [int(x.strip()) for x in entrada.split(",")]

# Validación 20 numeros.
if len(numeros) != 20:
    print("⚠️ Debés ingresar exactamente 20 números.")
    exit()
    
#Tiempo que tarda en ordenar. 
inicio_orden = time.perf_counter()
ordenada = bubble_sort(numeros.copy())
fin_orden = time.perf_counter()
tiempo_orden = fin_orden - inicio_orden

# Ordenar la lista
ordenada = bubble_sort(numeros.copy())
print("📋 Lista ordenada de menor a mayor:", ordenada)
print(f"⏱️ Tiempo de ordenamiento: {tiempo_orden:.9f} segundos")

# Buscar número
buscado = int(input("🔎 Ingresá un número que quieras buscar: "))
posicion = busqueda_binaria(ordenada, buscado)

# Medir tiempo de búsqueda
inicio_busqueda = time.perf_counter()
posicion = busqueda_binaria(ordenada, buscado)

fin_busqueda = time.perf_counter()
tiempo_busqueda = fin_busqueda - inicio_busqueda

if posicion != -1:
    print(f"✅ El número {buscado} está en la posición {posicion} de la lista ordenada.")
else:
    print(f"❌ El número {buscado} no se encuentra en la lista.")
    
print(f"⏱️ Tiempo de búsqueda: {tiempo_busqueda:.9f} segundos")
