# Automação criada para renomear os arquivos gerados no 01 - Relatórios para prestadores.py - os nomes destes arquivos constam o número de CNES dos estabelecimentos. 
# Iremos utilizar també o arquivo txt onde constam os números de CNES e Nomes dos Estabelecimentos (mesmo utilizado em 01 - Relatórios para prestadores.py)


import os
import re

# Defina o diretório onde estão os arquivos
pasta = r"Coloque aqui o caminho"

# EXTENSÃO A SER ALTERADA PARA .TXT
EXT = ".JUL"



# Define o caminho do arquivo contendo os CNES e nomes dos estabelecimentos
arquivo_tabela = r"Coloque aqui o caminho"



# Dicionário para armazenar os códigos e os respectivos nomes/razões sociais
codigo_para_nome = {}

# Lê o arquivo da tabela e extrai os códigos e nomes
with open(arquivo_tabela, "r", encoding="utf-8") as file:
    linhas = file.readlines()

for linha in linhas:
    # Expressão regular para capturar o código no formato "000.000-0"
    match = re.search(r"(\d{3}\.\d{3}-\d|\d{14})", linha)
    if match:
        codigo = match.group()  # Obtém o código encontrado
        nome = linha[:match.start()].strip()  # Obtém o nome antes do código
        codigo_para_nome[codigo.replace(".", "").replace("-", "")] = nome  # Remove caracteres do código e adiciona ao dicionário

# Percorre todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith(EXT):  # Filtra apenas arquivos com a extensão .DEZ
        caminho_antigo = os.path.join(pasta, nome_arquivo)

        # Remove a extensão antiga
        nome_base = os.path.splitext(nome_arquivo)[0]

        # Extrai o código do nome do arquivo (7 primeiros caracteres após prefixo)
        if nome_base.startswith("RCBO_"):
            codigo = nome_base[5:12]
            sufixo = " - SINTETICO DE CBO POR UNIDADE.txt"
        elif nome_base.startswith("RProc_"):
            codigo = nome_base[6:13]
            sufixo = " - SINTETICO DE PROCEDIMENTOS POR UNIDADE.txt"
        elif nome_base.startswith("RProcFis_"):
            codigo = nome_base[9:16]
            sufixo = " - SINTETICO DE PROCEDIMENTOS POR UNIDADE-FISICO.txt"
        else:
            # Caso o nome não tenha um prefixo conhecido, apenas muda a extensão
            novo_nome = nome_base + ".txt"
            caminho_novo = os.path.join(pasta, novo_nome)
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: {nome_arquivo} -> {novo_nome}")
            continue

        # Verifica se o código está na tabela e adiciona o nome correspondente
        nome_entidade = codigo_para_nome.get(codigo, "DESCONHECIDO")

        # Cria o novo nome do arquivo
        novo_nome = f"{nome_entidade}{sufixo}"
        caminho_novo = os.path.join(pasta, novo_nome)

        # Renomeia o arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_arquivo} -> {novo_nome}")

print("Renomeação concluída!")
