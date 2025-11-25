# Dados gerados a partir dos relatórios - 1 relatório para todas as unidades: 
# _ SINTETICO DE PROCEDIMENTOS POR UNIDADE
# _ SINTETICO DE PROCEDIMENTOS POR UNIDADE/FISICO

import os
import re
import pandas as pd

# Pastas de entrada e saída
pasta_entrada = r"local onde estão os relatórios"
pasta_saida = r"local onde será salvo o arquivo"

os.makedirs(pasta_saida, exist_ok=True)

# Regex para detectar datas no formato dd/mm/yyyy
regex_data = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")

def processar_arquivo(caminho, tipo_relatorio):
    """
    tipo_relatorio: "quantidade" ou "valor"
    """
    with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
        linhas = [linha.rstrip("\n") for linha in f]

    dados = []

    cnes = ""
    estabelecimento = ""

    for linha in linhas:
        linha_strip = linha.strip()

        # Ignorar linhas indesejadas
        if (linha_strip.startswith("Pagina") or
            linha_strip.startswith("SMS-ARARAQ") or
            regex_data.search(linha_strip) or
            linha_strip.startswith("********") or
            linha_strip.startswith("  PROCED.")):
            continue

        # Detecta início de bloco
        if linha_strip.startswith("Unidade"):
            cnes = linha[8:15].strip()
            estabelecimento = linha[16:51].strip()

        # Detecta fim de bloco
        elif linha_strip.startswith("TOTAL DA UNIDADE"):
            total_produzido = linha[75:87].strip()
            total_aprovado = linha[88:102].strip()

            # Conversão dos números
            if tipo_relatorio == "quantidade":
                # Substitui pontos por nada (ex: 7.754 → 7754)
                total_produzido = total_produzido.replace(".", "")
                total_aprovado = total_aprovado.replace(".", "")
                try:
                    total_produzido = float(total_produzido)
                except ValueError:
                    total_produzido = 0.0
                try:
                    total_aprovado = float(total_aprovado)
                except ValueError:
                    total_aprovado = 0.0
            elif tipo_relatorio == "valor":
                # Troca pontos por nada e vírgula por ponto (ex: 995.210,80 → 995210.80)
                total_produzido = total_produzido.replace(".", "").replace(",", ".")
                total_aprovado = total_aprovado.replace(".", "").replace(",", ".")
                try:
                    total_produzido = float(total_produzido)
                except ValueError:
                    total_produzido = 0.0
                try:
                    total_aprovado = float(total_aprovado)
                except ValueError:
                    total_aprovado = 0.0

            # Adiciona linha resumida
            dados.append({
                "CNES": cnes,
                "Estabelecimento": estabelecimento,
                "Total Produzido": total_produzido,
                "Total Aprovado": total_aprovado
            })

    df = pd.DataFrame(dados, columns=["CNES", "Estabelecimento", "Total Produzido", "Total Aprovado"])
    return df


# Processa todos os arquivos da pasta
for nome_arquivo in os.listdir(pasta_entrada):
    caminho = os.path.join(pasta_entrada, nome_arquivo)
    if not os.path.isfile(caminho):
        continue

    # Detecta tipo de relatório pelo nome
    if "RSPROCQT" in nome_arquivo.upper():
        tipo = "quantidade"
    elif "RSPROCED" in nome_arquivo.upper():
        tipo = "valor"
    else:
        print(f"⚠️ Tipo de relatório não identificado, pulando: {nome_arquivo}")
        continue

    df = processar_arquivo(caminho, tipo)

    # Nome do Excel de saída
    nome_excel = os.path.splitext(nome_arquivo)[0] + "_resumido.xlsx"
    caminho_saida = os.path.join(pasta_saida, nome_excel)

    # Salva o Excel
    df.to_excel(caminho_saida, index=False)

    print(f"✅ Processado: {nome_excel}")

print("\n🎉 Todos os relatórios foram convertidos com sucesso!")
