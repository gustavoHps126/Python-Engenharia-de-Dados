import json
import csv

def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
      dados_json = json.load(file)
    return dados_json

def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

def letirura_dados(path, tipo_arquvivo):
    dados = []

    if tipo_arquvivo == 'csv':
        dados = leitura_csv(path)  

    elif tipo_arquvivo == 'json':
        dados = leitura_json(path)

    return dados

def rename_columns(dados, key_mapping):
    new_dados_csv = []

    for old_dict in  dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
    new_dados_csv[0]

    return new_dados_csv

def get_columns(dados):
   return list(dados[0].keys())

path_csv = 'data_raw/dados_empresaB.csv'
path_json = 'data_raw/dados_empresaA.json'


#Iniciando a Leitura
dados_json = letirura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
print(f"Nome colunas dados json: {nome_colunas_json}")

dados_csv = letirura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
print(nome_colunas_csv)

key_mapping = {'Nome do Item': 'Nome do Produto',
             'Classificação do Produto': 'Categoria do Produto',
             'Valor em Reais (R$)': 'Preço do Produto (R$)',
             'Quantidade em Estoque': 'Quantidade em Estoque',
             'Nome da Loja': 'Filial',
             'Data da Venda': 'Data da Venda'}

#Transformação de dados

dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(nome_colunas_csv)