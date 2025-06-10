import random
import time

# Generar una lista de 500 notas aleatorias entre 0 y 10 con decimales
notas = [round(random.uniform(0, 10), 2) for _ in range(500)]

# 1. Bubble Sort
def bubble_sort_desc(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:  # Para orden descendente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Copias de la lista para que ambos métodos trabajen igual
notas_burbuja = notas.copy()
notas_sorted = notas.copy()

# Tiempo con Bubble Sort
inicio_burbuja = time.time()
bubble_sort_desc(notas_burbuja)
fin_burbuja = time.time()

# Tiempo con sorted()
inicio_sorted = time.time()
notas_sorted = sorted(notas_sorted, reverse=True)
fin_sorted = time.time()

# Mostrar resultados
print("Top 10 notas ordenadas (Bubble Sort):", notas_burbuja[:10])
print("Top 10 notas ordenadas (sorted()):", notas_sorted[:10])
print(f"Tiempo Bubble Sort: {fin_burbuja - inicio_burbuja:.6f} segundos")
print(f"Tiempo sorted(): {fin_sorted - inicio_sorted:.6f} segundos")
