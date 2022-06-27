# <<<<<<<<<<<<<<<<<<<<<<< Enzo >>>>>>>>>>>>>>>>>>>>>>>>>>>

# <--- função para criação de matriz --->

def começo(m):
    matriz = [m*[0], m*[0], m*[0], m*[0]]

    for i in range(0, m):
        for j in range(0, m):
            matriz[i][j] = int(input(f"Digite o elemento [{i}, {j}]: "))

    return matriz


# <--- Escrita dos arquivos - paralelo à criação da função --->

def abrir_arq(x):
    arquivo = open("Tamanho_peças", "a")

    for i in range(qtd_peças):
        tamanho = input("Qual o tamanho da peça? ")
        tam = (f" Tamanho da peça [{i+1}]: {tamanho}\n")

        arquivo.write(tam)

    arquivo.close()


qtd_peças = int(input("Quantas peças vão ser adicionadas? "))
arq = abrir_arq(qtd_peças)

# <----- Leitura dos dados inseridos no arquivo ----->

arquivo = open("Tamanho_peças", "r")

conteudo = arquivo.read()
print(conteudo)

arquivo.close()

# <--- Criação de listas a partir do arquivo --->

arquivo = open("Tamanho_peças", "r")

tamanhos = arquivo.readlines()

print(tamanhos)


# <--- função de remoção de linhas --->

def remov_linha(num_linhas, nome_arq):
    arquivo = open(nome_arq, "r")

    linhas = arquivo.readlines()

    arquivo.close()

    del(linhas[num_linhas-1])

    arquivo = open(nome_arq, "w")
    arquivo.writelines(linhas)



# <<<<<<<<<<<<<<<<<<<<<<< Bruno >>>>>>>>>>>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<<<<<<<<<<< Julia >>>>>>>>>>>>>>>>>>>>>>>>>>>
