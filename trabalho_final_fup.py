import csv
import random
# usamos diferentes listas nos parâmetros para garantir a funcionalidade do programa mesmo com variáveis diferentes dentro do programa principal


# <--- função principal, de adicionar peças --->


def arq_abrir(quantidade):

    # aqui, definimos alguns estilos base para o armario
    estilos = ['CLÁSSICO', 'VINTAGE', 'RETRO', 'STREET', 'CASUAL',
               'GLAM', 'COMFY', 'HIPSTER', 'ESPORTIVO', 'INDIE']

    # abre o arquivo na função de adicionar coisas, além do encoding que permite let "ç" e acentos ortograficos
    arquivo = open('teste22.csv', mode='a+', encoding="utf-8")

    # aqui, definimos a função de escrever no csv
    escrever = csv.writer(arquivo, lineterminator='\n')

    # aqui fornecemos os destinos de venda e de doação
    d_doacao = ['SHALOM', 'LAR TORRES DE MELO', 'IPREDE']
    d_venda = ['PARTICULAR', 'MARIA', 'JOÃO', 'JOSÉ', 'VALERIA']

    # Dicionário que vai receber o conteúdo de cada linha vinculada às colunas
    registro = {}

    # repetira o processo de adição com base na quantidade de peças à serem adicionadas
    for i in range(quantidade):

        linha = []  # a linha vai ser zerada a cada loop

        # recebimento do ID
        tag = int(input("Qual o ID do item? "))
        registro['ID'] = tag

        # recebimento do tipo do item. ( superior, inferior ou calçado )
        padrao = input("Qual o tipo do item  ? ")
        # aqui transformamos o que foi recebido em Caps Lock para melhor tratamento
        tipo = padrao.upper()
        # se nao atender às pendencias estabelecidas no trabalho, pede novamente ate inserir certo
        while tipo != "SUPERIOR" and tipo != "INFERIOR" and tipo != "CALÇADO":
            print("Deve ser algum superior, inferior ou calçado! ")
            padrao = input("Qual o tipo do item  ? ")
            tipo = padrao.upper()

        registro['TIPO'] = tipo

        # recebimento do tamanho do item.
        tam = input("Qual o tamanho do item?")
        # maiusculas, para melhor tratamento
        tamanho = tam.upper()

        # confere se atende aos tamanhos indicados pelo trabalho , se nao, pede novamente
        while tamanho != "P" and tamanho != "M" and tamanho != "G":
            tam = input("Qual o tamanho do item?")
            tamanho = tam.upper()

        registro['TAMANHO'] = tamanho

        # recebimento do sexo do item
        genero = input("Qual o gênero deste item ?  ")
        # transforma em maiuscula
        sexo = genero.upper()
        # confere se atende aos requisitos, se nao , pede novamente
        while sexo != "MASCULINO" and sexo != "FEMININO" and sexo != "UNISSEX":
            print("Entrada de gênero inválida! ")
            genero = input("Qual o gênero deste item ?  ")
            sexo = genero.upper()

        registro['PADRAO'] = sexo

        # recebimendo de cor
        coloral = input("Qual a cor ?")
        # maisculas para tratamento
        color = coloral.upper()

        registro['Cor'] = color

        # recebimento do estilo
        estilo = input("Qual o estilo da peça? ")
        style = estilo.upper()
        # se o estilo digitado, já estiver na bibilioteca, ele so recebe.
        if style in estilos:
            registro['ESTILO'] = style
        # caso nao, iniciamos o processo de adição de estilos
        else:
            resposta = input("Estilo inexistente! Deseja cadastrar um novo? ")
            if resposta == "sim":
                print("Estilo cadastrado")
            else:
                estilo = input("Qual o novo estilo da peça? ")
                style = estilo.upper()
                registro['ESTILO'] = style

        # recebimendo da data
        date = input(
            "Qual a data de compra deste item? - Utilize dd/mm/aaaa :")
        tempo = time(date)
        # tratamento da data, caso nao seja digitada no meio dd/mm/aaaa
        while len(date) < 10 or len(date) > 10:
            print("Formato de data inválido! Tente novamente utilizando dd/mm/aa ")
            date = input(("Qual a data de compra deste item? "))

        registro['DATA DE AQUISIÇÃO'] = date
        # aqui, chamamos a função da data, para poder ser tratada na venda e doação

        # recebimento do status
        status = input("Qual o status desse item? [Venda] [Doação] [Manter] ")
        stats = status.upper()

        # Vai acrescentando os registros desejados e em seguida adicionar os valores a linha, caso queira manter
        if stats == "MANTER":
            # nao terá destino algum, pois será mantida
            registro['DESTINO DA DOAÇÃO'] = " "
            registro['DESTINO DA VENDA'] = " "
            # nem preço.
            registro['preco'] = "R$0"
            registro['Situacao'] = stats
            # aqui, adicionamos nossos recebimentos dentro do guarda-roupa
            linha.append(registro['ID'])
            linha.append(registro['TIPO'])
            linha.append(registro['TAMANHO'])
            linha.append(registro['PADRAO'])
            linha.append(registro['Cor'])
            linha.append(registro['Situacao'])
            linha.append(registro['preco'])
            linha.append(registro['ESTILO'])
            linha.append(registro['DATA DE AQUISIÇÃO'])
            linha.append(registro['DESTINO DA DOAÇÃO'])
            linha.append(registro['DESTINO DA VENDA'])
            linha.append(" \n")
            # depois de criar uma lista com cada elemento na ordem do cabeçalho, adicionar a lista como linha no CSV
            escrever.writerow(linha)
            registro['DATA DE VENDA/DOAÇÃO'] = ' '

        # se for vendido, recebe o preço digitado pelo usuario
        elif stats == "VENDA":
            price = int(input("Qual o preço de venda do item? "))
            # aqui chamamos a função da venda, que arquiva e salva os dados da peça em outro repositorio
            arquivo_venda(tag, tipo, sexo, tamanho, color, date, price)

        # se for doação, aqui sera introduzido o sistema de doaçao, logo nao tendo preço tambem
        else:

            # printa os destinos de doação, para a pessoa saber onde pode doar
            print("Destinos disponíveis: ", d_doacao)

            destino = input("Qual o destino da doação? ")
            # maiusculas
            destino_f = destino.upper()

            # caso o destino inserido nao bata com a lista, pede novamente
            while destino_f not in d_doacao:
                print("Destino desconhecido!")
                destino = input("Qual o destino da doação? ")
                destino_f = destino.uper()

            # aqui, registra e salva os dados da peça que irá ser doada em um novo arquivo, assim facilitando a imagem de doação
            arquivo_doação(tag, tipo, sexo, tamanho,
                           color, date, tempo, destino_f)

            registro['Situacao'] = status
            registro['preco'] = "R$0"

    # conferir se deseja repetir o processo de adição de peças
    retomada = input("Deseja adicionar outra peça? ")
    # se sim, abre uma nova função com somente 1 peça
    if retomada == "sim":
        arq_abrir(1)
    # caso nao, pergunta se desjea fechar
    else:
        fechar = input("Dseja fechar o programa? ")
        # se nao quiser, chama a função menu novamente para continuar editando o guarda-roupa
        if fechar == "nao":
            menu()
        # se nao, fecha o programa
        else:
            print("Fechando o guarda-roupa...")
            exit()

    arquivo.close()

# F1 Adicionar estilos disponíveis a uma lista de opções a ser exibida


def listar_estilos(estilos_listados):
    estilos_listados = []
    arquivo = open("teste22.csv", 'r', encoding="utf8")
    for linha in csv.DictReader(arquivo):
        if linha['ESTILO'] not in estilos_listados:
            estilos_listados.append(linha['ESTILO'])
    arquivo.close()
    return estilos_listados

# F2 Função CONTADOR peças de estilos


def conta_pecas(styles):
    conta = {}
    arquivo = open("teste22.csv", 'r', encoding="utf8")
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
    arquivo = open("teste22.csv", 'r', encoding="utf8")
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
    arquivo = open("teste22.csv", 'r', encoding="utf8")
    # criar um dicionario vazio com os estilos disponiveis
    for style in styles:
        contaestilos[style] = 0
    # criar um dicionario vazio com os estilos disponiveis
    arquivo.close()
    return contaestilos


def selecionar_estilos():

    estilos = []
    estilos = listar_estilos(estilos)  # todos os estilos do Documento
    contador = conta_pecas(estilos)
    trending = conta_sel_estilos(estilos)

    #----- Selecionar o estilo e filtrar má intenção de resposta -----#
    exibir_estilos(contador)
    # ARQUIVO ANTERIORMENTE, ESTAVA LENDO O TESTE CRIADO POR ALEATORIEDADE
    # ATUALIZEI PARA LER O ATUAL CSV E ESTÁ DANDO ALGUNS CONFLITOS, FAVOR OLHAR
    arquivo = open("teste22.csv", 'r', encoding="utf8")
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
                # ERRO NA LINHA 280 >>>>>> KEYERROR ESTILO
                # ESTÁ DANDO ERRO NA HORA DE CONFERIR O DICT ESTILO - TALVEZ POIS ESTÁ NA FUNÇÃO ANTERIOR
                # AJEITAR ISSO <<
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
            print("Fechando o guarda-roupa...")
            exit()
        else:
            menu()

# <--- função de remoção de linhas --->
# FUNÇÃO OK


def remov_linha():

    # mostrando todas as peças, para que possa saber qual cabide tirar
    printar_itens()

    # essa lista vai armazenar todas as linhas do arquivo e é ela que vamos editar para remover uma linha
    linhas_do_arquivo = list()

    remover = input("Informe o ID da peça a ser removida: ")

    while True:
        # vamos testar se a conversão do string obtido no input é possível para inteiro. Se sim, temos um ID válido. Senão, vamos solicitar novamente
        try:
            teste = int(remover)
        # o erro esperado é o ValueError, pois não é possível converter 'CALÇADO' para um inteiro, assim vamos solicitar novamente o ID
        except ValueError:
            remover = input("Informe o ID da peça a ser removida: ")
        # quando tentarmos emular o erro e não retornar nada errado, paramos o laço e seguimos com o programa
        else:
            break

    # primeiro vamos abrir o arquivo para leitura e copiar os dados para a lista
    with open('teste22.csv', 'r', encoding="utf-8") as arquivo:
        # vamos percorrer cada linha do arquivo
        for row in csv.reader(arquivo):
            linhas_do_arquivo.append(row)
            for field in row:
                # se algum campo da linha percorrida for igual ao ID obtido pelo input e armazenado em 'remover', a linha vai ser excluída da lista editada
                if field == remover:
                    linhas_do_arquivo.remove(row)

    # com o ID identificado e excluído da lista, vamos escrever os demais elementos da lista, reescrevendo do zero o arquivo original, sem atualizar, por isso o mode é 'w'
    with open('teste22.csv', 'w', encoding="utf-8") as writeFile:
        writer = csv.writer(writeFile, lineterminator='\n')
        writer.writerows(linhas_do_arquivo)


# <--- função de alteração das linhas --->
# FUNÇÃO OK

def alterar_linhas():

    # mostrando todas as peças, para que possa saber qual cabide alterar
    printar_itens()

    # essa lista vai armazenar todas as linhas do arquivo e é ela que vamos editar para remover uma linha
    linhas_do_arquivo = list()

    remover = int(input("Informe o ID da peça a ser alterada: "))

    while True:
        # vamos testar se a conversão do string obtido no input é possível para inteiro. Se sim, temos um ID válido. Senão, vamos solicitar novamente
        try:
            teste = int(remover)
        # o erro esperado é o ValueError, pois não é possível converter 'CALÇADO' para um inteiro, assim vamos solicitar novamente o ID
        except ValueError:
            remover = input("Informe o ID da peça a ser removida: ")
        # quando tentarmos emular o erro e não retornar nada errado, paramos o laço e seguimos com o programa
        else:
            break

    # primeiro vamos abrir o arquivo para leitura e copiar os dados para a lista
    with open('teste22.csv', 'r', encoding="utf-8") as arquivo:
        # vamos percorrer cada linha do arquivo
        for row in csv.reader(arquivo):
            linhas_do_arquivo.append(row)
            for field in row:
                # se algum campo da linha percorrida for igual ao ID obtido pelo input e armazenado em 'remover', a linha vai ser excluída da lista editada
                if field == remover:
                    linhas_do_arquivo.remove(row)

    # com o ID identificado e excluído da lista, vamos escrever os demais elementos da lista, reescrevendo do zero o arquivo original, sem atualizar, por isso o mode é 'w'
    with open('teste22.csv', 'w', encoding="utf-8") as writeFile:
        writer = csv.writer(writeFile, lineterminator='\n')
        writer.writerows(linhas_do_arquivo)

    # Com essa função, escreveremos em um arquivo, no formato CSV, as informações das peças destinadas à venda
    # Os parâmetros são as variáveis que irão receber os dados informados pelo usuário

    print("Agora insira as novas informações: ")
    # chamando a função de abrir o arquivo para escrever as novas informações, da peça removida.
    arq_abrir(1)


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

# função para imprimir os itens do armario na tela, juntamente com os tipos de classes


def printar_itens():
    # aqui é o cabeçlho, que apresenta a ordem das informações da peças
    print("ID, TIPO, TAMANHO, PADRÃO, COR, SITUAÇÃO, PREÇO, ESTILO, DATA DE AQUISIÇÃO")

    # abre o arquivo
    arquivo = open('teste22.csv', 'r', encoding='utf-8')

    # dentro do for, vai recebendo cada linha do  arquivo em csv
    for linha in csv.reader(arquivo):

        # e printando esse elemento, para uma visualização mais clara com o "*" que mostra so os elementos
        print(*linha)

    # fecha o arquivo
    arquivo.close()

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
    data = ' '
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
    with open('Venda.csv', 'r+', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        # man explicar isso está além das minhas capacidades mas depois eu escrevo direitinho
        # eu consegui de fato adicionar no Venda.csv , porém , ta dando conflito com a key price
        # ve ai o que pode ser...
        sorted_file = sorted(csv_reader, key=lambda k: k['PREÇO'])
        for linha in sorted_file:
            print(*linha)
# ---------------------------------------------------------------------------------------------------------------

# função para listas as peças destinadas à doação de acordo com a data (mais recente para o mais antigo)
# por ser decrescente, usamos reverse=True


def ordenar_por_data():
    with open('Doação.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        # deu um mesmo erro aqui, no key tempo
        # favor quem puder olhar ai...
        sorted_file = sorted(
            csv_reader, key=lambda k: k['tempo'], reverse=True)
    return sorted_file

# função do menu


def menu():
    # possiveis ações para serem tomadas
    opcoes = [" < --------- Á R M A R I O --------- >", "Digite [1] para adicionar novas peças! ", "Digite [2] para visualizar suas peças. ", "Digite [3] para ver as peças a serem vendidas.",
              "Digite [4] para ver as peças a serem doadas.", "Digite [5] para selecionar estilo e montar look.", "Digite [6] para alterar alguma peça.", "Digite [7] para remover alguma peça. ", "Digite [8] para sair."]

    # imprime o menu bonitinho, com o cada opçao em cada linha
    for o in range(9):
        print(opcoes[o])

    # tratamento para garantir a ação certa
    while True:
        iniciar = int(
            input("Utilizando os digitos do menu. Qual ação irá ser tomada?  "))

        # aqui a condição de parada, vai ser somente caso o digito seja maior ou menor do que as opçoes possíveis
        if iniciar > 8 or iniciar < 1:
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

        # chama a função com base na quantidade de itens, pois assim pode adicionar multiplas peças, ou somente uma
        arq_abrir(quantidade)

        # checando se nao deseja adicionar outra peça, se sim repetindo o processo
        while True:
            continuar = input("Deseja adicionar uma outra peça? ")
            # se quiser continuar, a função é chamada novamente, porém so com uma peça
            if continuar == "sim":
                arq_abrir(1)

            # senao, conferindo se deseja fechar o programa ou tomar outra ação
            elif continuar == "nao":
                fechar = input("Dseja fechar o programa? ")
                # chamar o menu novamente e reniciar
                if fechar == "nao":
                    menu()
                # fechar o programa normalmentes
                else:
                    print("Fechando o guarda-roupa...")
                    exit()

    # visualizar as peças
    if iniciar == 2:
        printar_itens()

        # confere se nao ha outra ação na fila
        fim = input("Deseja sair do guarda-roupa? ")
        # se quiser fechar,  fecha o programa
        if fim == "sim":
            print("Fechando o guarda-roupa...")
            exit()
        # caso nao, renicia chamando a função menu novamente
        else:
            menu()

    # ver as peças vendidas
    if iniciar == 3:
        ordenar_por_preço()

    # ver as peças doadas
    if iniciar == 4:
        # salvamos o retorno da função numa variavel
        doaçao = ordenar_por_data()
        # para poder imprimir esse retorno
        print(doaçao)

    # selecionar estilos e montar o look
    if iniciar == 5:
        selecionar_estilos()

    # alterar peças
    if iniciar == 6:
        alterar_linhas()
        # aqui conferimos caso a pessoa dezeje alterar outra peça.
        alterar_novamente = input("Deseja alterar outra peça? ")
        # maiusculas para tratamento
        alterar_novamente = alterar_novamente.upper()
        # se quiser, ai chamamos a função novamente
        if alterar_novamente == "SIM":
            alterar_linhas()
        # senao, iniciamos o processo de fechamendo do guarda roupa
        else:
            fim = input("Deseja sair do guarda-roupa? ")
            if fim == "sim":
                print("Fechando o guarda-roupa...")
                exit()
            # onde se nao desejar fechar, chamamos o menu novamente
            else:
                menu()

            # remover peças
    if iniciar == 7:
        # confere o local da remoção
        #onde = int(input("Qual Cabide você deseja remover? "))
        # remove de fato
        remov_linha()

        # confere se deseja remover outro item
        remov_novo = input("Deseja remover outro cabide ? ")

        # condicional para repetir o processo ou sair
        if remov_novo == "sim":
            remov_linha()

        # confere se irá sair ou tomar outra ação
        else:
            fim = input("Deseja sair do guarda-roupa? ")
            # fechando o programa, com uma mensagem de saída
            if fim == "sim":
                print("Fechando o guarda-roupa...")
                exit()
            # chamando o menu novamente para iniciar novas ações
            else:
                menu()

    # fechar o programa
    if iniciar == 8:
        print("Fechando o guarda-roupa...")
        exit()

# <---------- programa principal ---------->


# chama a função do menu, abrindo ele na tela
menu()
