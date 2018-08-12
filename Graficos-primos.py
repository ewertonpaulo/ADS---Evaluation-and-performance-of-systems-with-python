import os
import csv
import matplotlib.pyplot as plt

caminho = "output-bench-primos/"
nomes_arquivos = os.listdir("output-bench-primos")
dados = []

for i in range(len(nomes_arquivos)):
    nome_arquivo = caminho+nomes_arquivos[i]
    #txt = open(nome_arquivo,'rb')

    dado = txt.readlines()
    #dado[1] = dado[1].replace("\n,","")
    lista = dado[1].split()

    for i in range(len(lista)):
        lista[i] = float(lista[i])

    dados.append(lista)

def inicio(dados):
    return dados[0]
def teste(dados):
    return dados[1]

dados.sort(key = teste)

threads = []
tempo = []
cpu = []
numero_maximo = []
time = []



for j in dados:
    threads.append(j[0])
    tempo.append(j[3])
    numero_maximo.append(j[1])
    time.append(j[3])
    cpu.append(round(j[4]*100,2))

txt.close

def thread_cpu():
    plt.plot(threads, cpu)
    plt.title('Cpu and Threads')
    plt.xlabel('Threads')
    plt.ylabel('cpu')
    plt.show()

def thread_tempo():
    
    plt.plot(numero_maximo, tempo)
    plt.title('Cargo and Threads')
    plt.xlabel('Carga')
    plt.ylabel('tempo(ms)')
    plt.show()
    
thread_tempo()






    

