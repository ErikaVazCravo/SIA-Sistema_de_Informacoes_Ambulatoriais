# Essa automação foi feita para renomear os arquivos gerados a partir do relatório de erros que o SIA emite após cada consistência
# (R0350 - RELATORIO DE OCORRENCIAS NA CONSISTENCIA).
# É necessário fazer a separação manual dos estabelecimentos


import os

# Defina o diretório onde estão os arquivos TXT - Todos os arquivos desta pasta que estiverem em txt seram renomeados
pasta = r"coloque o caminho"

competencia = "07/2025"

# Percorre todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith(".txt"):  # Filtra apenas os arquivos .txt
        caminho_antigo = os.path.join(pasta, nome_arquivo)
        
        # Remove a extensão .txt do nome original
        nome_base = os.path.splitext(nome_arquivo)[0]

        # Novo nome do arquivo com o texto adicional no final
        novo_nome = f"{nome_base} - RELATORIO DE OCORRENCIAS NA CONSISTENCIA - {competencia}.txt"
        caminho_novo = os.path.join(pasta, novo_nome)

        # Renomeia o arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_arquivo} -> {novo_nome}")

print("Renomeação concluída!")
