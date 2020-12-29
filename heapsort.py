import criarvetor
import time

def heapify(a, n, i):
    maior = i
    Dir = 2 * i + 1
    Esq = 2 * i + 2

    if Esq < n and a[maior] < a[Esq]:
        maior = Esq
    if Dir < n and a[maior] < a[Dir]:
        maior = Dir
    if maior != i:
        a[i], a[maior] = a[maior], a[i]
        heapify(a, n, maior)

def heapsort(a, n):
    for i in range(n//2-1, -1, -1):
        heapify(a, n, i)
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i , 0)

vetor = []
vetor = criarvetor.arquivo_vetor(vetor)

print("\nVetor original:", vetor)
print("\nO vetor deve ser:\n1 - desordenado\n2 - ordenado (crescente)\n3 - ordenado (decrescente)")
flag = int(input())
if flag == 2:
    vetor.sort()
    print("\nVetor crescente:", vetor)
elif flag == 3:
    vetor.sort(reverse=True)
    print("\nVetor decrescente:", vetor)
inicio = time.time()
heapsort(vetor, len(vetor))
fim = time.time()

print("\nVetor ordenado:", vetor)
print("Tempo de execução:", (fim - inicio)*1000, "ms")