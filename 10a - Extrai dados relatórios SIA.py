import os
import re
import pandas as pd

# Caminhos das pastas
pasta_entrada = r"Coloque aqui o caminho onde estão os relatórios"
pasta_saida = r"caminho onde será salvo o arquivo gerado"

os.makedirs(pasta_saida, exist_ok=True)

def processar_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
        linhas = [linha.rstrip("\n") for linha in f]

    dados = []
    cnes = ""
    estabelecimento = ""
    dentro_unidade = False
    produ_total = 0
    aprov_total = 0

    for linha in linhas:
        # Detecta início de bloco
        if linha.strip().startswith("Unidade"):
            dentro_unidade = True
            cnes = linha[8:15].strip()
            estabelecimento = linha[16:51].strip()
            produ_total = 0
            aprov_total = 0
            continue

        # Detecta fim de bloco
        if dentro_unidade and linha.strip().startswith("TOTAL DA UNIDADE"):
            # Adiciona linha de total
            dados.append({
                "CNES": cnes,
                "Estabelecimento": estabelecimento,
                "Procedimento": "TOTAL DA UNIDADE",
                "Produzido": produ_total,
                "Aprovado": aprov_total
            })
            # Adiciona linha em branco separadora
            dados.append({"CNES": "", "Estabelecimento": "", "Procedimento": "", "Produzido": "", "Aprovado": ""})
            dentro_unidade = False
            continue

        # Linhas de procedimentos dentro do bloco
        if dentro_unidade and re.match(r"^\s*\d", linha):
            proc = linha[0:75].strip()
            produzido = linha[75:89].strip().replace(",", ".")
            aprovado = linha[90:104].strip().replace(",", ".")
            # Tenta converter valores numéricos
            try:
                produ_num = float(produzido)
            except ValueError:
                produ_num = 0.0
            try:
                aprov_num = float(aprovado)
            except ValueError:
                aprov_num = 0.0

            produ_total += produ_num
            aprov_total += aprov_num

            dados.append({
                "CNES": cnes,
                "Estabelecimento": estabelecimento,
                "Procedimento": proc,
                "Produzido": produ_num,
                "Aprovado": aprov_num
            })

    # Gera DataFrame
    df = pd.DataFrame(dados, columns=["CNES", "Estabelecimento", "Procedimento", "Produzido", "Aprovado"])
    return df


# Processa todos os arquivos da pasta
for nome_arquivo in os.listdir(pasta_entrada):
    caminho = os.path.join(pasta_entrada, nome_arquivo)
    if not os.path.isfile(caminho):
        continue

    df = processar_arquivo(caminho)

    # Nome do arquivo Excel
    nome_excel = os.path.splitext(nome_arquivo)[0] + ".xlsx"
    caminho_saida = os.path.join(pasta_saida, nome_excel)

    # Salva como Excel
    df.to_excel(caminho_saida, index=False)

    print(f"✅ Processado: {nome_excel}")

print("\n🎉 Todos os relatórios foram convertidos com sucesso!")
