# <<<<<<<<<<<<<<<<<<<<<<< Enzo >>>>>>>>>>>>>>>>>>>>>>>>>>>

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
# <--- função para criação de matriz --->


def criar_matriz(n, m):
    m1 = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(
                int(input(f"DIgite o elemento[{i}][{j}] da mat{n}x{m} ")))
        m1.append(linha)
    return m1

# <--- Escrita dos arquivos - paralelo à criação da função --->

# def abrir_arq(a):
    # arquivo = open("Tamanho_peças", "a")

    # for i in range(qtd_peças):
    # tamanho = input("Qual o tamanho da peça? ")
    # tam = (f" Tamanho da peça [{i+1}]: {tamanho}\n")

    # arquivo.write(tam)

    # arquivo.close()

# <--- criação de arquivos generalizada --->


def arq_abrir(quantidade):
    arquivo = open("Armario", "a", encoding="utf-8")
    for i in range(quantidade):
        tag = int(input("Qual o ID do item? "))
        tipo = input(f"Qual o tipo do item [{tag}] ? ")
        sexo = input("Qual o gênero deste item? ")
        tamanho = input("Qual o tamanho do item?")
        color = input("Qual a cor ?")
        estilo = input("Qual o estilo da peça? ")
        date = int(input(("Qual a data de compra deste item? ")))
        stats = input("Qual o status desse item? [Venda] [Doação] [Manter] ")
        if stats != "Venda":
            price = 0
        else:
            price = int(input("Qual o preço deste item?"))
        arquivo.write(
            f"Item || id: [{tag}] - tipo: [{tipo}] - sexo: [{sexo}] - tamanho: [{tamanho}] - cor: [{color}] - data de aquisição: [{date}] - status: [{stats}] - preço: [{price}] - estilo: [{estilo}] ")

    arquivo.close()


# qtd_peças = int(input("Quantas peças vão ser adicionadas? "))
# arq = abrir_arq(qtd_peças)'''


# <--- Criação de listas a partir do arquivo --->

# arquivo = open("Tamanho_peças", "r")

# tamanhos = arquivo.readlines()

# print(tamanhos)


# <--- função de remoção de linhas --->

def remov_linha(num_linhas):
    arquivo = open("Armario", "r")

    linhas = arquivo.readlines()

    arquivo.close()

    del(linhas[num_linhas-1])

    arquivo = open("Armario", "w")
    arquivo.writelines(linhas)

# <--- função de alteração das linhas --->


def alterar_linhas(num_linhas, novo):
    arquivo = open("Armario", "r")

    linhas = arquivo.readlines()

    arquivo.close()

    linhas.insert(num_linhas-1, novo)

    del(linhas[num_linhas-1])

    arquivo = open("Armario", "w")
    arquivo.writelines(linhas)

# <--- adição dos elementos em um arquivo --->


print(
    " < ------ Á R M A R I O ------ >   \n Digite [Adicionar] para novas peças! [Visualizar] para ver suas peças. \n [Alterar] para alterar alguma peça. [Remover] para remover alguma peça.")
iniciar = input("Deseja tomar alguma ação? ")
# essa ideia ainda nao está pronta, mas seria um menu para selecioar as açoes
if iniciar == "Adicionar":

    # nao pedir o nome do arquivo, ja incrementar num arquivo chamado Armario.
    quantidade = int(input("Quantos itens serão adicionados? "))
    teste = arq_abrir(quantidade)

if iniciar == "Visualizar":
    # <----- Leitura dos dados inseridos no arquivo ----->

    arquivo = open("Armario", "r")

    conteudo = arquivo.read()
    print(conteudo)

    arquivo.close()

    fim = input("Deseja sair do guarda-roupa? ")
    if fim == "sim":
        exit()
    else:
        restart_program()

# agumas funçoes, como essa ainda nao estao funcionando devidamente
if iniciar == "Alterar":
    item = int(input("Qual linha você deseja alterar? "))
    novo = arq_abrir(item)
    alteraçao = alterar_linhas(item, novo)
if iniciar == "Remover":
    onde = int(input("QUal linha você deseja remover? "))
    remoçao = remov_linha(onde)


# <<<<<<<<<<<<<<<<<<<<<<< Bruno >>>>>>>>>>>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<<<<<<<<<<< Julia >>>>>>>>>>>>>>>>>>>>>>>>>>>
