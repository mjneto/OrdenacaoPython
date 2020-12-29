import criarvetor
import criarvetor_gna
import time

def insertionsort_b(balde):
    for i in range(1, len(balde)):
        aux = balde[i]
        j = i - 1
        while (j >= 0 and aux < balde[j]):
            balde[j+1] = balde[j]
            j = j - 1
        balde[j+1] = aux

def bucketsort(a):
    maximo = max(a)
    tamanho = maximo / len(a)
    lista_baldes = []

    for i in range(len(a)):
        lista_baldes.append([])

    for i in range(len(a)):
        j = int(a[i] / tamanho)
        if j != len(a):
            lista_baldes[j].append(a[i])
        else:
            lista_baldes[len(a) - 1].append(a[i])
    for i in range(len(a)):
        insertionsort_b(lista_baldes[i])
    saida = []
    for i in range(len(a)):
        saida = saida + lista_baldes[i]
    return saida


vetor = []
print("1 - valores uniformes distribuidos / 2 - gerar normalmente")
flag = int(input("> "))
if flag == 2: vetor = criarvetor.arquivo_vetor(vetor)
elif flag == 1: vetor = criarvetor_gna.arquivo_vetor(vetor)
else: 
    print("Erro")
    exit(1)

print("\nVetor original:", vetor)
inicio = time.time()
vetor = bucketsort(vetor)
fim = time.time()
print("\nVetor ordenado:", vetor)
print("Tempo de execução:", (fim - inicio)*1000, "ms")