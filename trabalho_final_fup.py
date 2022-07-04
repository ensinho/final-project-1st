# <<<<<<<<<<<<<<<<<<<<<<< Enzo >>>>>>>>>>>>>>>>>>>>>>>>>>>

# função para reniciar o programa
import sys
import os


def restart_program():

    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

# <--- função principal, de adicionar peças --->


def arq_abrir(quantidade):

    arquivo = open("Armario", "a", encoding="utf-8")

    for i in range(quantidade):
        ler_ids = open("Ids", "r")

        id = ler_ids.read()
        print(id)

        ler_ids.close()

        tag = int(input("Qual o ID do item? "))

        ids = open("Ids", "a", encoding="utf-8")
        ids.write(f"Id: [{tag}] ")
        ids.close()

        tipo = input(f"Qual o tipo do item [{tag}] ? ")

        sexo = input("Qual o gênero deste item ?  ")

        tamanho = input("Qual o tamanho do item?")
        while tamanho != "p" and tamanho != "m" and tamanho != "g":
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
            f"Id:[{tag}] | tipo:[{tipo}] | sexo:[{sexo}] | tamanho:[{tamanho}] | cor:[{color}] | data de compra:[{date}] | status:[{stats}] | valor:[{price}] | estilo:[{estilo}]\n")

    arquivo.close()


# <--- função de remoção de linhas --->

def remov_linha(num_linhas):
    arquivo = open("Armario", "r")

    linhasr = arquivo.readlines()

    arquivo.close()

    del(linhasr[num_linhas-1])

    arquivo = open("Armario", "w")
    arquivo.writelines(linhasr)

# <--- função de alteração das linhas --->


def alterar_linhas(num_linhas, novo):
    arquivo = open("Armario", "r")

    linhas = arquivo.readlines()

    arquivo.close()

    linhas.insert(num_linhas-1, novo)

    del(linhas[num_linhas])

    linhas.remove(None)

    arquivo = open("Armario", "w")
    arquivo.writelines(linhas)

# <--- adição dos elementos em um arquivo --->


opcoes = [" < ------- Á R M A R I O ------- >", "Digite [1] para adicionar novas peças! ", "Digite [2] para visualizar suas peças. ",
          "Digite [3] para alterar alguma peça.", "Digite [4] para remover alguma peça. ", "Digite [5] para sair."]

for o in range(6):
    print(opcoes[o])


while True:
    iniciar = int(input("Qual ação ira ser tomada? "))

    if iniciar > 5 or iniciar < 1:
        print("Entrada inválida! Tente novamente com outro número. ")
    else:
        break


if iniciar == 1:

    quantidade = int(input("Quantos itens serão adicionados? "))
    while quantidade <= 0:
        print("Entrada Inválida, tente novamente!")
        quantidade = int(input("Quantos itens serão adicionados? "))

    teste = arq_abrir(quantidade)

    while True:
        continuar = input("Deseja adicionar uma outra peça? ")
        if continuar == "sim":
            teste1 = arq_abrir(1)
        elif continuar == "nao":
            fechar = input("Dseja fechar o programa? ")
            if fechar == "nao":
                restart_program()
            else:
                exit()

if iniciar == 2:
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


if iniciar == 3:
    item = int(input("Qual linha você deseja alterar? "))
    novo = arq_abrir(1)

    alteraçao = alterar_linhas(item, novo)

    alt_novo = input("Deseja alterar alguma outra peça? ")

    if alt_novo == "sim":
        item1 = int(input("Qual linha você deseja alterar? "))
        novo1 = arq_abrir(1)
        alteraçao1 = alterar_linhas(item1, novo1)

    else:
        fim = input("Deseja sair do guarda-roupa? ")
        if fim == "sim":
            exit()
        else:
            restart_program()

if iniciar == 4:
    onde = int(input("Qual linha você deseja remover? "))
    remoçao = remov_linha(onde)

    remov_novo = input("Deseja remover outra linha? ")
    if remov_novo == "sim":
        onde1 = int(input("Qual linha você deseja remover? "))
        remoçao1 = remov_linha(onde1)
    else:
        fim = input("Deseja sair do guarda-roupa? ")
        if fim == "sim":
            exit()
        else:
            restart_program()

if iniciar == 5:
    exit()


# <<<<<<<<<<<<<<<<<<<<<<< Bruno >>>>>>>>>>>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<<<<<<<<<<< Julia >>>>>>>>>>>>>>>>>>>>>>>>>>>
