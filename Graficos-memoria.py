import os
import csv
import matplotlib.pyplot as plt

caminho = "output-bench-memoria/"
nomes_arquivos = os.listdir("output-bench-memoria")
dados = []

for i in range(len(nomes_arquivos)):
    nome_arquivo = caminho+nomes_arquivos[i]
    #txt = open(nome_arquivo, 'rb')

    dado = txt.readlines()
    #dado[1] = dado[1].replace("\n","")
    lista = dado[1].split()

    for i in range(len(lista)):
        lista[i] = float(lista[i])

    dados.append(lista)

def inicio(dados):
    return dados[0]

dados.sort(key = inicio)
print(dados)

kb_memoria = [] #[0]
tamanho_array = [] #[1]
repeticos_busca = [] #[2]
start_time = [] #[3]
tempo_popular = [] #[4]
tempo_busca = [] #[5]
tempo_total = [] #[6]

for j in dados:
    kb_memoria.append(j[0])
    tamanho_array.append(j[1])
    repeticos_busca.append(j[2])
    start_time.append(j[3])
    tempo_popular.append(j[4])
    tempo_busca.append(j[5])
    tempo_total.append(j[6])

txt.close



def tempo_tamanho():
    print(tamanho_array)
    print(tempo_busca)
    plt.plot(tamanho_array,tempo_busca)
    plt.title("Total time and Array lenght")
    plt.show()

tempo_tamanho()





