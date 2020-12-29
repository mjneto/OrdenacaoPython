import os
import random
from datetime import datetime

def arquivo_vetor(vetor):
    path = "vetor.txt"

    if os.path.getsize(path) and os.path.exists(path) > 0:
        print("Usar vetor já escrito?\n1 - Sim\n2 - Novo Vetor")
        flag = int(input(">> "))
        if flag == 1:
            arquivo_vetor = open(path, "r")
            for i in arquivo_vetor:
                vetor.append(int(i))
            return(vetor)
        elif flag == 2:
            print("Tamanho do vetor de entrada?", end=" ")
            tam = int(input())
            random.seed(datetime.now())
            vetor = [random.randrange(1,100) for i in range(tam)]
            arquivo_vetor = open(path, 'w')
            for i in vetor:
                arquivo_vetor.write(str(i)+"\n")
            return(vetor)
        else:
            print('erro')
            exit(1)
    else:
        print("Tamanho do vetor de entrada?", end=" ")
        tam = int(input())
        random.seed(datetime.now())
        vetor = [random.randrange(1,100) for i in range(tam)]
        arquivo_vetor = open('vetor.txt', 'w')
        for i in vetor:
            arquivo_vetor.write(str(i)+"\n")
        return(vetor)
    arquivo_vetor.close()