import csv  # primeiramente temos que importar a biblioteca hehe

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

# ---------------------------------------------------------------------------------------------------------------


def mostrar_peças_doadas(sorted_file):  # NÃO DEU CERTO
    csv_reader = csv.DictReader(sorted_file)
    del csv_reader['TEMPO']
    for linha in csv_reader:
        print(linha)


#ignorar - testes
'''for i in range(3):
    tag = int(input('tag'))
    tipo = input('tipo')
    sexo = input('sexo')
    tamanho = input('tamanho')
    color = input('cor')
    date = input('data')
    stats = input('venda ou doação')
    destino = input('destino')
    tempo = time(date)
    arquivo_doação(tag, tipo, sexo, tamanho, color, date, destino, tempo)


sorted_file = ordenar_por_data() 
mostrar_peças_doadas(sorted_file)'''
