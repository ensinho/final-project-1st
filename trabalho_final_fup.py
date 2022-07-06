# <<<<<<<<<<<<<<<<<<<<<<< Enzo >>>>>>>>>>>>>>>>>>>>>>>>>>>

# <--- função principal, de adicionar peças --->


def arq_abrir(quantidade):

    # abre o arquivo na função de adicionar coisas, além do encoding que permite let "ç" e acentos ortograficos
    arquivo = open("Armario", "a", encoding="utf-8")

    # repetira o processo de adição com base na quantidade de peças à serem adicionadas
    for i in range(quantidade):

        # le o arquivo dos IDS e salva eles
        ler_ids = open("Ids", "r")

        # printa na tela todos os IDS ja utilizados nas peças
        id = ler_ids.read()
        print(id)

        # fecha o arquivo
        ler_ids.close()

        # aqui recebe o ID do item
        tag = int(input("Qual o ID do item? "))

        # abre o arquivo IDS para introduzir o ID recebido na tag e salva la
        ids = open("Ids", "a", encoding="utf-8")
        # escrevendo o Id
        ids.write(f"Id: [{tag}] ")
        # fechando o arquivo, seguindo com o codigo
        ids.close()

        # recebendo o tipo/padrao do item
        padrao = input(f"Qual o tipo do item [{tag}] ? ")
        # transforma a string em minuscula
        tipo = padrao.lower()
        # se nao atender às pendencias estabelecidas no trabalho, pede novamente ate inserir certo
        while tipo != "superior" and tipo != "inferior" and tipo != "calçado":
            print("Deve ser algum superior, inferior ou calçado! ")
            tipo = input(f"Qual o tipo do item [{tag}] ? ")

        # mesmo processo para o gênero do item
        genero = input("Qual o gênero deste item ?  ")
        # transforma em minusculo
        sexo = genero.lower()
        # confere se atende aos requisitos, se nao , pede novamente
        while sexo != "masculino" and sexo != "feminino" and sexo != "unissex":
            print("Entrada de gênero inválida! ")
            sexo = input("Qual o gênero deste item ?  ")

        # mesmo processo para o tamanho do item
        tam = input("Qual o tamanho do item?")
        # transforma em minuscula
        tamanho = tam.lower()
        # confere os requisitos, se nao, pede novamente
        while tamanho != "p" and tamanho != "m" and tamanho != "g":
            tamanho = input("Qual o tamanho do item?")

        # recebe a cor
        color = input("Qual a cor ?")
        color = color.lower()

        # estilos ainda nao concluidos, porem
        estile = input("Qual o estilo da peça? ")
        estilo = estile.lower()
        # ler de uma biblioteca de estilos para tratar
        # aqui, uma tentativa de tratar com uma biblioteca externa de estilos
        estilos = open("Estilos", "r")

        # le e armazena o conteudo
        tipos = estilos.read()

        estilos.close()

        # se o estlo recebido nao estiver na biblioteca ja existente dos estilos
        # confere se deseja ser adicionado um novo estilo, se nao, pede novamente
        while estile not in tipos:
            resposta = input("Estilo inexistente! Deseja cadastrar um novo? ")
            if resposta == "sim":
                # aqui onde seria adicionado um sistema de cadastro de novo estilo
                # nao mexi com isso ainda, mexeremos em conjunto depois
                print("Estilo cadastrado")
            else:
                estile = input("Qual o estilo da peça? ")

        # recebe a data do item
        date = int(input(("Qual a data de compra deste item? ")))

        # recebe o status sobre aquele item
        status = input("Qual o status desse item? [Venda] [Doação] [Manter] ")
        stats = status.lower()

        # tratamento do status, caso receba manter, o preço será 0 pois nao vai ser vendido
        if stats == "manter":
            price = 0
        # se for vendido, recebe o preço digitado pelo usuario
        elif stats == "venda":
            price = int(input("Qual o preço deste item?"))
        # se for doação, aqui sera introduzido o sistema de doaçao, logo nao tendo preço tambem
        else:
            price = "0 - Doacao"
            # aqui onde conferimos sobre as doaçoes da menina julia

        # aqui escreve no arquivo todas as informaçoes, bem bonitinhas
        arquivo.write(
            f"Id:[{tag}] | tipo:[{tipo}] | sexo:[{sexo}] | tamanho:[{tamanho}] | cor:[{color}] | data de compra:[{date}] | status:[{stats}] | valor:[{price}] | estilo:[{estile}]\n")

    arquivo.close()


# <--- função de remoção de linhas --->

def remov_linha(num_linhas):
    # abre o arquivo, na função leitura
    arquivo = open("Armario", "r")

    # le ele, transformando o conteudo em uma lista, atribuindo a uma variavel
    linhasr = arquivo.readlines()

    # fecha o arquivo
    arquivo.close()

    # deleta a informação do cabide desejado
    del(linhasr[num_linhas-1])

    # abre o arquivo novamente, escrevendo a lista nele
    arquivo = open("Armario", "w")
    arquivo.writelines(linhasr)

# <--- função de alteração das linhas --->


def alterar_linhas(num_linhas, novo):
    # abre o arquivo, na função leitura
    arquivo = open("Armario", "r")

    # le eles, transformando em uma lista
    linhas = arquivo.readlines()

    # fecha o arquivo
    arquivo.close()

    # na linha inserida -1, pois é uma lista, se adiciona a nova informaçao
    linhas.insert(num_linhas-1, novo)

    # enquanto deleta a antiga, que tomava aquela posição
    del(linhas[num_linhas])

    # removendo o none que fica na lista
    linhas.remove(None)

    # abre o arquivo novamente e escreve a lista nele
    arquivo = open("Armario", "w")
    arquivo.writelines(linhas)


# função do menu
def menu():

    # as possiveis ações para serem tomadas
    opcoes = [" < ------- Á R M A R I O ------- >", "Digite [1] para adicionar novas peças! ", "Digite [2] para visualizar suas peças. ",
              "Digite [3] para alterar alguma peça.", "Digite [4] para remover alguma peça. ", "Digite [5] para sair."]

    # menu bonitinho
    for o in range(6):
        print(opcoes[o])

    # tratamento para garantir a ação certa
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
        # tratamento para garantir uma quantidade válida de itens
        while quantidade <= 0:
            print("Entrada Inválida, tente novamente!")
            quantidade = int(input("Quantos itens serão adicionados? "))

        # chama a função com base na quantidade
        teste = arq_abrir(quantidade)

        # checando se nao deseja adicionar outra peça, se sim repetindo o processo
        while True:
            continuar = input("Deseja adicionar uma outra peça? ")
            if continuar == "sim":
                teste1 = arq_abrir(1)

            # senao, conferindo se deseja fechar o programa ou tomar outra ação
            elif continuar == "nao":
                fechar = input("Dseja fechar o programa? ")
                if fechar == "nao":
                    menu()
                else:
                    exit()

    # visualizar as peças
    if iniciar == 2:
        # <----- Leitura dos dados inseridos no arquivo ----->

        # abre o arquivo
        arquivo = open("Armario", "r")

        # le o conteudo, e o transforma em uma lista
        conteudo = arquivo.readlines()
        for i in range(len(conteudo)):
            print(conteudo[i])

        arquivo.close()

        # confere se nao ha outra ação na fila
        fim = input("Deseja sair do guarda-roupa? ")
        if fim == "sim":
            exit()
        else:
            menu()

    # alterar peças
    if iniciar == 3:
        # insere as informaçoes da alteração
        item = int(input("Qual Cabide você deseja alterar? "))
        novo = arq_abrir(1)

        # altera a peça, com o chamado da função
        alteraçao = alterar_linhas(item, novo)

        # confere se nao deseja alterar outra peça
        alt_novo = input("Deseja alterar alguma outra peça? ")

        # aplica a condicional para repetir o processo ou sair
        if alt_novo == "sim":
            item1 = int(input("Qual Cabide você deseja alterar? "))
            novo1 = arq_abrir(1)
            alteraçao1 = alterar_linhas(item1, novo1)

        # aqui confere se deseja sair ou tomar outra ação
        else:
            fim = input("Deseja sair do guarda-roupa? ")
            if fim == "sim":
                exit()
            else:
                menu()

    # remover peças
    if iniciar == 4:
        # confere o local da remoção
        onde = int(input("Qual Cabide você deseja remover? "))
        # remove de fato
        remoçao = remov_linha(onde)

        # confere se deseja remover outro item
        remov_novo = input("Deseja remover outro cabide ? ")

        # condicional para repetir o processo ou sair
        if remov_novo == "sim":
            onde1 = int(input("Qual Cabide você deseja remover? "))
            remoçao1 = remov_linha(onde1)

        # confere se irá sair ou tomar outra ação
        else:
            fim = input("Deseja sair do guarda-roupa? ")
            if fim == "sim":
                exit()
            else:
                menu()

    # fechar o programa
    if iniciar == 5:
        exit()

# <---------- programa principal ---------->


# chama a função do menu, abrindo ele na tela
menu()


# <<<<<<<<<<<<<<<<<<<<<<< Bruno >>>>>>>>>>>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<<<<<<<<<<< Julia >>>>>>>>>>>>>>>>>>>>>>>>>>>
