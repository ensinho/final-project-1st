# <<<<<<<<<<<<<<<<<<<<<<< Enzo >>>>>>>>>>>>>>>>>>>>>>>>>>>

# função para reniciar o programa
# esta função veio apresentado problemas, pretendo remove-la em breve

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

        padrao = input(f"Qual o tipo do item [{tag}] ? ")
        tipo = padrao.lower()
        while tipo != "superior" and tipo != "inferior" and tipo != "calçado":
            print("Deve ser algum superior, inferior ou calçado! ")
            tipo = input(f"Qual o tipo do item [{tag}] ? ")

        genero = input("Qual o gênero deste item ?  ")
        sexo = genero.lower()
        while sexo != "masculino" and sexo != "feminino" and sexo != "unissex":
            print("Entrada de gênero inválida! ")
            sexo = input("Qual o gênero deste item ?  ")

        tam = input("Qual o tamanho do item?")
        tamanho = tam.lower()
        while tamanho != "p" and tamanho != "m" and tamanho != "g":
            tamanho = input("Qual o tamanho do item?")

        color = input("Qual a cor ?")
        color = color.lower()

        estile = input("Qual o estilo da peça? ")
        estilo = estile.lower()
        # ler de uma biblioteca de estilos para tratar
        # aqui, uma tentativa de tratar com uma biblioteca externa de estilos
        estilos = open("Estilos", "r")

        tipos = estilos.read()

        estilos.close()

        while estile not in tipos:
            resposta = input("Estilo inexistente! Deseja cadastrar um novo? ")
            if resposta == "sim":
                # aqui onde seria adicionado um sistema de cadastro de novo estilo
                # nao mexi com isso ainda, mexeremos em conjunto depois
                print("Estilo cadastrado")
            else:
                estile = input("Qual o estilo da peça? ")

        date = int(input(("Qual a data de compra deste item? ")))

        status = input("Qual o status desse item? [Venda] [Doação] [Manter] ")
        stats = status.lower()

        # tratamento do status
        if stats == "manter":
            price = 0
        elif stats == "venda":
            price = int(input("Qual o preço deste item?"))
        else:
            price = "DOACAO"
            # aqui onde conferimos sobre as doaçoes da menina julia

        arquivo.write(
            f"Id:[{tag}] | tipo:[{tipo}] | sexo:[{sexo}] | tamanho:[{tamanho}] | cor:[{color}] | data de compra:[{date}] | status:[{stats}] | valor:[{price}] | estilo:[{estile}]\n")

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

# <---------- programa principal ---------->


opcoes = [" < ------- Á R M A R I O ------- >", "Digite [1] para adicionar novas peças! ", "Digite [2] para visualizar suas peças. ",
          "Digite [3] para alterar alguma peça.", "Digite [4] para remover alguma peça. ", "Digite [5] para sair."]

# menu bonitinho
for o in range(6):
    print(opcoes[o])


# garantir a ação certa
while True:
    iniciar = int(
        input("Utilizando os digitos do menu. Qual ação irá ser tomada?  "))

    if iniciar > 5 or iniciar < 1:
        print("Entrada inválida! Tente novamente com outro número. ")
    else:
        break


# adicionar peças
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

# visualizar as peças
if iniciar == 2:
    # <----- Leitura dos dados inseridos no arquivo ----->

    arquivo = open("Armario", "r")

    conteudo = arquivo.readlines()
    for i in range(len(conteudo)):
        print(conteudo[i])

    arquivo.close()

    fim = input("Deseja sair do guarda-roupa? ")
    if fim == "sim":
        exit()
    else:
        restart_program()

# alterar peças
if iniciar == 3:
    item = int(input("Qual Cabide você deseja alterar? "))
    novo = arq_abrir(1)

    alteraçao = alterar_linhas(item, novo)

    alt_novo = input("Deseja alterar alguma outra peça? ")

    if alt_novo == "sim":
        item1 = int(input("Qual Cabide você deseja alterar? "))
        novo1 = arq_abrir(1)
        alteraçao1 = alterar_linhas(item1, novo1)

    else:
        fim = input("Deseja sair do guarda-roupa? ")
        if fim == "sim":
            exit()
        else:
            restart_program()

# remover peças
if iniciar == 4:
    onde = int(input("Qual Cabide você deseja remover? "))
    remoçao = remov_linha(onde)

    remov_novo = input("Deseja remover outro cabide ? ")
    if remov_novo == "sim":
        onde1 = int(input("Qual Cabide você deseja remover? "))
        remoçao1 = remov_linha(onde1)
    else:
        fim = input("Deseja sair do guarda-roupa? ")
        if fim == "sim":
            exit()
        else:
            restart_program()

# fechar o programa
if iniciar == 5:
    exit()


# <<<<<<<<<<<<<<<<<<<<<<< Bruno >>>>>>>>>>>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<<<<<<<<<<< Julia >>>>>>>>>>>>>>>>>>>>>>>>>>>
