import csv
import random
from turtle import color
# usamos diferentes listas nos parâmetros para garantir a funcionalidade do programa mesmo com variáveis diferentes dentro do programa principal

# F1 Adicionar estilos disponíveis a uma lista de opções a ser exibida


def listar_estilos(estilos_listados):
    estilos_listados = []
    arquivo = open("teste.csv", 'r', encoding="utf8")
    for linha in csv.DictReader(arquivo):
        if linha['ESTILO'] not in estilos_listados:
            estilos_listados.append(linha['ESTILO'])
    arquivo.close()
    return estilos_listados

# F2 Função CONTADOR peças de estilos


def conta_pecas(styles):
    conta = {}
    arquivo = open("teste.csv", 'r', encoding="utf8")
    # criar um dicionario vazio com os estilos disponiveis
    for style in styles:
        conta[style] = 0
    for linha in csv.DictReader(arquivo):
        for i in range(len(styles)):
            if linha['ESTILO'] == styles[i]:
                conta[styles[i]] += 1
    arquivo.close()
    return conta

# F3 montar o meu próprio estilo selecionando por ID


def montar_proprio_estilo(calçado, inferior, superior):
    estilo_custom = []
    arquivo = open("teste.csv", 'r', encoding="utf8")
    # separando e selecionando o itens para compor a lista com o look personalizado
    for linha in csv.DictReader(arquivo):
        if linha['ID'] == calçado:
            estilo_custom.append(linha)
        if linha['ID'] == inferior:
            estilo_custom.append(linha)
        if linha['ID'] == superior:
            estilo_custom.append(linha)
    arquivo.close()
    return estilo_custom

#F4 #----- Exibir/imprimir estilos disponíveis ------#


def exibir_estilos(dicionario_contador_pecas):
    print("\033[1;36;47m-\033[m"*44)
    print(
        f'\033[1;36;47mTemos {len(dicionario_contador_pecas)} estilos disponíveis, veja quais são: \033[m')
    print("\033[1;36;47m-\033[m"*44)
    for chave in sorted(dicionario_contador_pecas, key=dicionario_contador_pecas.get):
        print(f'{chave} - {dicionario_contador_pecas[chave]} peças')

# F5 - Preencher o dicionario de tendências (trending, ou seja, quantas vezes o estilo foi selecionado) com os estilos disponíveis no arquivo e o contador de seleção zerado


def conta_sel_estilos(styles):
    contaestilos = {}
    arquivo = open("teste.csv", 'r', encoding="utf8")
    # criar um dicionario vazio com os estilos disponiveis
    for style in styles:
        contaestilos[style] = 0
    # criar um dicionario vazio com os estilos disponiveis
    arquivo.close()
    return contaestilos

# função selecionar


def selecionar_estilos():

    estilos = []
    estilos = listar_estilos(estilos)  # todos os estilos do Documento
    contador = conta_pecas(estilos)
    trending = conta_sel_estilos(estilos)

    #----- Selecionar o estilo e filtrar má intenção de resposta -----#
    exibir_estilos(contador)
    arquivo = open("teste.csv", 'r', encoding="utf8")
    while True:
        print("\033[1;36;47m-\033[m"*36)
        selecionado = input(
            "\033[1;36;47mQual estilo você deseja selecionar? \033[m").strip()
        selecionado = selecionado.upper()
        print("\033[1;36;47m-\033[m"*36)

        if selecionado in estilos:
            select = estilos.index(selecionado)
            for linha in csv.DictReader(arquivo):
                # imprimir peças disponíveis para estilo selecionado
                if linha['ESTILO'] == estilos[select]:
                    print(linha['ID'], linha['TIPO'], linha['PADRÃO'], linha['COR'], linha['SITUAÇÃO'],
                          linha['PREÇO'], linha['ESTILO'], linha['DATA DE AQUISIÇÃO'], "\n")
            break
        else:
            print("\033[1;31;47mO estilo selecionado não está disponível.\033[m")
        resposta = input(
            f'\033[1;36;47mPrecisa ver os estilos disponíveis e a quantidade de looks possível novamente? s/n \033[m').strip()
        resposta = resposta.upper()
        if resposta == 'S' or resposta == "SIM":
            exibir_estilos(contador)

    # Seleção por ID: quais peças você deseja selecionar para montar seu estilo?
    # não precisa converter para inteiro, porque o código da peça no arquivo está como string, apesar de ser um número

    # preciso tratar essas entradas
        while True:
            # preciso tratar essas entradas
            calçado = input(
                "\033[1;36;47mInforme o ID do calçado escolhido: \033").strip()
            inferior = input(
                "\033[1;36;47mInforme o ID do inferior escolhido: \033").strip()
            superior = input(
                "\033[1;36;47mInforme o ID do superior escolhido: \033").strip()

            meu_estilo = montar_proprio_estilo(calçado, inferior, superior)

            # recebe nome do estilo e monta o look do dia
            print("\033[1;36;47m-\033[m"*36)
            print(
                f"O seu estilo para hoje é {meu_estilo[0]['ESTILO']}: \n + {meu_estilo[0]['TIPO']} {meu_estilo[0]['COR']}\n + {meu_estilo[1]['TIPO']} {meu_estilo[1]['COR']}\n + {meu_estilo[2]['TIPO']} {meu_estilo[2]['COR']}")
            print("\033[1;36;47m-\033[m"*36)
            confirmation = input(
                f'\033[1;36;47mEra esse estilo que você queria? s/n\033[m')
            confirmation = confirmation.upper()
            if confirmation == "SIM" or confirmation == 'S':
                trending[selecionado] += 1
                print(
                    f'\033[1;36;47mO estilo {selecionado} foi selecionado {trending[selecionado]} vez(es)\033[m')

                # PONTO DE SAÍDA DA SELEÇÃO DE ESTILO E VOLTA AO MENU INICIAL
                break
            else:
                print("\033[1;31;47mSelecione novamente\033[m")
        arquivo.close()

        fim = input("Deseja sair do guarda-roupa? ")
        if fim == "sim":
            exit()
        else:
            menu()

# <--- função principal, de adicionar peças --->


def arq_abrir(quantidade):

    estilos = ['CLÁSSICO', 'VINTAGE', 'RETRO', 'STREET', 'CASUAL',
               'GLAM', 'COMFY', 'HIPSTER', 'ESPORTIVO', 'INDIE']

    # abre o arquivo na função de adicionar coisas, além do encoding que permite let "ç" e acentos ortograficos
    arquivo = open('teste22.csv', mode='a+', encoding="utf-8")

    escrever = csv.writer(arquivo, lineterminator='\n')

    # datas vão com a função data_aleatoria()
    d_doacao = ['SHALOM', 'LAR TORRES DE MELO', 'IPREDE']
    d_venda = ['PARTICULAR', 'MARIA', 'JOÃO', 'JOSÉ', 'VALERIA']

    # Dicionário que vai receber o conteúdo de cada linha vinculada às colunas
    registro = {}

    # repetira o processo de adição com base na quantidade de peças à serem adicionadas
    for i in range(quantidade):

        linha = []  # a linha vai ser zerada a cada loop
    tag = int(input("Qual o ID do item? "))
    registro['ID'] = tag

    # recebimento do tipo do item.
    padrao = input(f"Qual o tipo do item  ? ")
    tipo = padrao.upper()
    # se nao atender às pendencias estabelecidas no trabalho, pede novamente ate inserir certo
    while tipo != "SUPERIOR" and tipo != "INFERIOR" and tipo != "CALÇADO":
        print("Deve ser algum superior, inferior ou calçado! ")
        tipo = input(f"Qual o tipo do item  ? ")
    registro['TIPO'] = padrao

    # recebimento do tamanho do item.
    tam = input("Qual o tamanho do item?")
    tamanho = tam.upper()
    # confere os requisitos, se nao, pede novamente
    while tamanho != "P" and tamanho != "M" and tamanho != "G":
        tamanho = input("Qual o tamanho do item?")
    registro['TAMANHO'] = tam

    # recebimento do sexo do item
    genero = input("Qual o gênero deste item ?  ")
    # transforma em minusculo
    sexo = genero.upper()
    # confere se atende aos requisitos, se nao , pede novamente
    while sexo != "MASCULINO" and sexo != "FEMININO" and sexo != "UNISSEX":
        print("Entrada de gênero inválida! ")
        sexo = input("Qual o gênero deste item ?  ")
    registro['PADRAO'] = genero

    # recebimendo de cor
    coloral = input("Qual a cor ?")
    color = coloral.upper()
    registro['Cor'] = color

    # recebimento do estilo
    estilo = input("Qual o estilo da peça? ")
    style = estilo.upper()
    if style in estilos:
        registro['ESTILO'] = style
    else:
        resposta = input("Estilo inexistente! Deseja cadastrar um novo? ")
        if resposta == "sim":
            print("Estilo cadastrado")
        else:
            style = input("Qual o novo estilo da peça? ")
            registro['ESTILO'] = style

    # recebimendo da data
    date = input("Qual a data de compra deste item? - Utilize dd/mm/aaaa :")
    # tratamento da data
    while len(date) < 10 or len(date) > 10:
        print("Formato de data inválido! Tente novamente utilizando dd/mm/aa ")
        date = input(("Qual a data de compra deste item? "))
    registro['DATA DE AQUISIÇÃO'] = date
    tempo = time(date)

    # recebimento do status
    status = input("Qual o status desse item? [Venda] [Doação] [Manter] ")
    stats = status.upper()

    # Vai acrescentando os registros desejados e em seguida adicionar os valores a linha
    if stats == "MANTER":
        linha.append(registro['ID'])
        linha.append(registro['TIPO'])
        linha.append(registro['TAMANHO'])
        linha.append(registro['PADRAO'])
        linha.append(registro['Cor'])
        linha.append(registro['Situacao'])
        linha.append(registro['preco'])
        linha.append(registro['ESTILO'])
        linha.append(registro['DATA DE AQUISIÇÃO'])
        linha.append(registro['DATA DE VENDA/DOAÇÃO'])
        linha.append(registro['DESTINO DA DOAÇÃO'])
        linha.append(registro['DESTINO DA VENDA'])
        # depois de criar uma lista com cada elemento na ordem do cabeçalho, adicionar a lista como linha no CSV
        escrever.writerow(linha)
        price = ' '
        registro['DATA DE VENDA/DOAÇÃO'] = ' '

    # se for vendido, recebe o preço digitado pelo usuario
    elif stats == "VENDA":
        price = int(input("Qual o preço de venda do item? "))
        arquivo_venda(tag, tipo, sexo, tamanho, color, date, price)

    # se for doação, aqui sera introduzido o sistema de doaçao, logo nao tendo preço tambem
    else:
        destino = random.choice(d_doacao)
        arquivo_doação(tag, tipo, sexo, tamanho, color, date, tempo, destino)
        price = " "
        registro['Situacao'] = status
        registro['preco'] = price

    # recebimendo dos locais de doação
    registro['DESTINO DA DOAÇÃO'] = random.choice(d_doacao)
    registro['DESTINO DA VENDA'] = random.choice(d_venda)

    # depois de criar uma lista com cada elemento na ordem do cabeçalho, adicionar a lista como linha no CSV
    escrever.writerow(linha)

    retomada = input("Deseja adicionar outra peça? ")
    if retomada == "sim":
        arq_abrir(1)
    else:
        fechar = input("Dseja fechar o programa? ")
        if fechar == "nao":
            menu()
        else:
            exit()

    arquivo.close()


# <--- função de remoção de linhas --->

# AJEITAR FUNÇÃO REMOVER LINHAS DO CSV <<<<<<<<<<<<<
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


# AJEITAR FUNÇÃO ALTERAR LINHAS DO CSV <<<<<<<<<<<<<<<
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


# Com essa função, escreveremos em um arquivo, no formato CSV, as informações das peças destinadas à venda
# Os parâmetros são as variáveis que irão receber os dados informados pelo usuário

def arquivo_venda(tag, tipo, sexo, tamanho, color, date, price):
    peça = [{'ID': tag, 'TIPO': tipo, 'SEXO': sexo, 'TAMANHO': tamanho, 'COR': color,
             'DATA DE AQUISIÇÃO': date, 'PREÇO': price}]  # lista com dicionários
    # abrir o arquivo #'as file1' é para nos referirmos ao arquivo como file1  #com o with open, não precisaremos usar a função close()
    with open('Venda.csv', 'w', encoding='utf-8') as file1:
        fields = ['ID', 'TIPO', 'SEXO', 'TAMANHO', 'COR',
                  'DATA DE AQUISIÇÃO', 'PREÇO']  # campos
        # o DictWriter vai permitir que os dados sejam escritos direitinho no arquivo
        csv_writer = csv.DictWriter(file1, fieldnames=fields)
        csv_writer.writeheader()  # escrita do cabeçalho (header)
        for info in peça:
            # escrevemos as {informações(info) = dicionários} da {peça = lista} no arquivo
            csv_writer.writerow(info)

# ---------------------------------------------------------------------------------------------------------------------------
# Com essa função, escreveremos em um arquivo, no formato CSV, as informações das peças destinadas à doação
# Não temos o preço como parâmetro
# O parâmetro destino e tempo são adicionados


def arquivo_doação(tag, tipo, sexo, tamanho, color, date, destino, tempo):
    peça = [{'ID': tag, 'TIPO': tipo, 'SEXO': sexo, 'TAMANHO': tamanho,
             'COR': color, 'DATA DE AQUISIÇÃO': date, 'DESTINO': destino, 'TEMPO': tempo}]
    # abrir o arquivo #'as file2' é para nos referirmos ao arquivo como file2
    with open('Doação.csv', 'w', encoding='utf-8') as file2:
        fields = ['ID', 'TIPO', 'SEXO', 'TAMANHO', 'COR',
                  'DATA DE AQUISIÇÃO', 'DESTINO', 'TEMPO']  # campos
        csv_writer = csv.DictWriter(file2, fieldnames=fields)
        csv_writer.writeheader()  # cabeçalho
        for info in peça:
            csv_writer.writerow(info)
# ---------------------------------------------------------------------------------------------------------------------------

# essa função deve vir antes
# a função 'tempo' vai nos ajudar a ordenar as peças por data (+ recente até o + antigo) na hora de listar as peças para doação


def time(date):
    data = ''
    for caractere in date:  # exemplo: 04/09/2022
        if caractere != '/':
            data += caractere  # 04092022
    time = data[4:] + data[2] + data[3] + data[0] + data[1]  # 20220904
    # --> Qual o objetivo disso? --> Quanto maior for o número (tempo), mais recente é
    return time
    # Exemplos: Estamos no dia 06/07/2022. A peça 1 foi adquirida em 04/09/2021 e a peça 2, em 05/06/2020. 20210904 é maior que 20200605, portanto, é mais recente. #eu peguei essa ideia ouvindo uma conversa hueheuheuh
# ---------------------------------------------------------------------------------------------------------------------------

# função para listar as peças destinadas à venda em ordem crescente de preço


def ordenar_por_preço():
    with open('Venda.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        # man explicar isso está além das minhas capacidades mas depois eu escrevo direitinho
        sorted_file = sorted(csv_reader, key=lambda k: k['price'])
        for linha in sorted_file:
            print(linha)
# ---------------------------------------------------------------------------------------------------------------

# função para listas as peças destinadas à doação de acordo com a data (mais recente para o mais antigo)
# por ser decrescente, usamos reverse=True


def ordenar_por_data():
    with open('Doação.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        sorted_file = sorted(
            csv_reader, key=lambda k: k['tempo'], reverse=True)
    return sorted_file

# função do menu


def menu():
    # as possiveis ações para serem tomadas
    opcoes = [" < --------- Á R M A R I O --------- >", "Digite [1] para adicionar novas peças! ", "Digite [2] para visualizar suas peças. ", "Digite [3] para ver as peças a serem vendidas.",
              "Digite [4] para ver as peças a serem doadas.", "Digite [5] para selecionar estilo e montar look.", "Digite [6] para alterar alguma peça.", "Digite [7] para remover alguma peça. ", "Digite [8] para sair."]

    # menu bonitinho
    for o in range(9):
        print(opcoes[o])

    # tratamento para garantir a ação certa
    while True:
        iniciar = int(
            input("Utilizando os digitos do menu. Qual ação irá ser tomada?  "))

        if iniciar > 7 or iniciar < 1:
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
        arq_abrir(quantidade)

        # checando se nao deseja adicionar outra peça, se sim repetindo o processo
        while True:
            continuar = input("Deseja adicionar uma outra peça? ")
            if continuar == "sim":
                arq_abrir(1)

            # senao, conferindo se deseja fechar o programa ou tomar outra ação
            elif continuar == "nao":
                fechar = input("Dseja fechar o programa? ")
                if fechar == "nao":
                    menu()
                else:
                    exit()

    # visualizar as peças
    # ajustes cairiam bem <<<
    if iniciar == 2:

        # abre o arquivo
        arquivo = open('teste22.csv', 'r', encoding='utf-8')

        for linha in csv.reader(arquivo):
            print(linha['DESTINO DA DOAÇÃO'], linha['ID'], linha['TIPO'], linha['PADRÃO'], linha['COR'],
                  linha['SITUAÇÃO'], linha['PREÇO'], linha['ESTILO'], linha['DATA DE AQUISIÇÃO'], "\n")

        arquivo.close()

        # confere se nao ha outra ação na fila
        fim = input("Deseja sair do guarda-roupa? ")
        if fim == "sim":
            exit()
        else:
            menu()

    # ver as peças vendidas
    if iniciar == 3:
        ordenar_por_preço()

    # ver as peças doadas
    if iniciar == 4:
        ordenar_por_data()

    # selecionar estilos
    if iniciar == 5:
        selecionar_estilos()

    # alterar peças
    if iniciar == 6:
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
    if iniciar == 7:
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
    if iniciar == 8:
        exit()

# <---------- programa principal ---------->


# chama a função do menu, abrindo ele na tela


# RESOLVER A APARIÇÃO INDESEJADA DO CABEÇALHO REPETIDAS VEZES

arquivo = open('teste22.csv', mode='a+', encoding="utf-8")

fields = ['ID', 'TIPO', 'TAMANHO', 'PADRÃO', 'COR', 'SITUAÇÃO', 'PREÇO', 'ESTILO',
          'DATA DE AQUISIÇÃO', 'DATA DE VENDA/DOAÇÃO', 'DESTINO DA DOAÇÃO', 'DESTINO DA VENDA']
with open('teste22.csv', 'a', encoding='utf-8') as file1:
    escrever = csv.writer(arquivo, lineterminator='\n')
    fields = ['ID', 'TIPO', 'TAMANHO', 'PADRÃO', 'COR', 'SITUAÇÃO', 'PREÇO', 'ESTILO',
                    'DATA DE AQUISIÇÃO', 'DATA DE VENDA/DOAÇÃO', 'DESTINO DA DOAÇÃO', 'DESTINO DA VENDA']
    # o DictWriter vai permitir que os dados sejam escritos direitinho no arquivo
    csv_writer = csv.DictWriter(file1, fieldnames=fields)
    csv_writer.writeheader()  # escrita do cabeçalho (header)


menu()


# <<<<<<<<<<<<<<<<<<<<<<< Bruno >>>>>>>>>>>>>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<<<<<<<<<<< Julia >>>>>>>>>>>>>>>>>>>>>>>>>>>
