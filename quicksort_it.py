import random
import criarvetor
import time

def particao (a, p, r):
    i = p - 1
    x = a[r]

    a[r], a[len(a)-1] = a[len(a)-1], a[r]
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return (i+1)

def quicksort (a, p, r):
    tamanho = r - p + 1
    pilha = [0] * (tamanho)
    topo = -1
    topo = topo + 1
    pilha[topo] = 1
    topo = topo + 1
    pilha[topo] = r
    
    while topo >= 0:
        r = pilha[topo]
        topo = topo - 1
        p = pilha[topo]
        topo = topo - 1
        q = particao(a, p, r)
        if q-1 > p:
            topo = topo - 1
            pilha[topo] = 1
            topo = topo + 1
            pilha[topo] = q - 1
        if q+1 < r:
            topo = topo + 1
            pilha[topo] = topo + 1
            topo = topo + 1
            pilha[topo] = r

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
print("\nO pivo deve ser:\n1 - Aleatório\n2 - Elemento do meio")
flag = int(input(">"))
if flag == 2:
    r = int(len(vetor)/2)
    print("\nA posição escolhida foi", r, "= [", vetor[r-1],"]")
    inicio = time.time()
    quicksort(vetor, 0, r - 1)
    fim = time.time()
elif flag == 1:
    r = random.randrange(0, len(vetor))
    print("\nA posição escolhida foi", r+1, "= [", vetor[r],"]")
    
    inicio = time.time()
    quicksort(vetor, 0, r)
    fim = time.time()

print("\nVetor ordenado:", vetor)
print("Tempo de execução:", (fim - inicio)*1000, "ms")
