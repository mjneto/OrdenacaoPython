import criarvetor
import time

def countingsort_r(a, exp1):
    n = len(a)
    saida = [0] * (n)
    cont = [0] * (10)

    for i in range(0, n):
        indice = (a[i] / exp1)
        cont[int(indice % 10)] += 1
    for i in range(1, 10):
        cont[i] += cont[i-1]
    i = n-1
    while i >= 0:
        indice = (a[i] / exp1)
        saida[cont[int(indice % 10)] - 1] = a[i]
        cont[int(indice % 10)] -= 1
        i -= 1
    i = 0
    for i in range(0, len(a)):
        a[i] = saida[i]

def radixsort(a):
    maximo = max(a)
    exp = 1
    while maximo / exp > 0:
        countingsort_r(vetor, exp)
        exp *= 10

vetor = []
vetor = criarvetor.arquivo_vetor(vetor)

print("Vetor original:", vetor)
inicio = time.time()
radixsort(vetor)
fim = time.time()
print("Vetor ordenado:", vetor)
print("Tempo de execução:", (fim - inicio)*1000, "ms")

