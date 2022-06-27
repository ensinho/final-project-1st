# Enzo -------------------
# função para criaçao de matriz
def começo(m):
    matriz = [m*[0], m*[0], m*[0], m*[0]]
    for i in range(0, m):
        for j in range(0, m):
            matriz[i][j] = int(input(f"Digite o elemento [{i}, {j}]: "))
    return matriz

# <--- TESTE DE LEITURA E ESCRITA ARQUIVO - PARALELO À CRIAÇÃO DA FUNÇÃO --->
def abrir_arq(x):
    arquivo = open("Tamanho_peças", "a")

    for i in range(qtd_peças):
        tamanho = input("Qual o tamanho da peça? ")
        tam = (f" \n Tamanho da peça: {tamanho} ")

        arquivo.write(tam)

    arquivo.close()


qtd_peças = int(input("Quantas peças vão ser adicionadas? "))
arq = abrir_arq(qtd_peças)
print(arq)

# Bruno ------------------


# Julia ------------------
