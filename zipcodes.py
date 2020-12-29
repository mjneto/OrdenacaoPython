import random
import os

def randomzipcode():
    path = "zipcodes.txt"
    path2 = "vetor.txt"
    x = []
    aux = []

    if os.path.getsize(path) and os.path.exists(path) > 0:
        arquivo_zip = open(path, 'r')
        for line in arquivo_zip:
            x.append(line)
        print("Quantos elementos?\n1 - 1000\n2 - 5000\n3 - 10000\n4 - Tudo (22302)")
        flag = int(input(">> "))
        if flag == 4: j = len(x)
        elif flag == 3: j = 10000
        elif flag == 2: j = 5000
        elif flag == 1: j = 1000
        else:
            print("Erro")
            exit(1)
        for i in range(0,j):
            aux.append(random.choice(x))
        arquivo_vetor = open(path2, 'w')
        for i in aux:
            arquivo_vetor.write(str(i))

randomzipcode()