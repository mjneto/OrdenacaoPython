import criarvetor
import time

def countingsort(a):
    elemento_max = int(max(a))
    elemento_min = int(min(a))
    elementos_alcance = elemento_max - elemento_min + 1
    cont_a = [0 for _ in range(elementos_alcance)]
    saida_a = [0 for _ in range(len(a))]

    for i in range(0, len(a)):
        cont_a[a[i]-elemento_min] += 1
    for i in range(1, len(cont_a)):
        cont_a[i] += cont_a[i-1]
    for i in range(len(a)-1, -1, -1):
        saida_a[cont_a[a[i]-elemento_min] - 1] = a[i]
        cont_a[a[i]-elemento_min] -= 1
    for i in range(0, len(a)):
        a[i] = saida_a[i]
    return(a)

vetor = []
vetor = criarvetor.arquivo_vetor(vetor)

print("Vetor original:", vetor)
inicio = time.time()
countingsort(vetor),
fim = time.time()
print("Vetor ordenado:", vetor)
print("Tempo de execução:", (fim - inicio)*1000, "ms")