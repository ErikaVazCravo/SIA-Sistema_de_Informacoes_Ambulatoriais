# Dados gerados a partir do Relatório 
# ANALITICO DE PROCEDIMENTOS POR UNIDADE (RAPROCED) - 
# 1 relatório para todas as unidades por competência

import os
import re
import pandas as pd

# ---------------- CONFIGURAÇÃO ----------------
pasta_entrada = r"Coloque aqui o caminho da pasta onde estão os relatórios gerados"
pasta_saida = r"Coloque aqui a pasta de destino"
os.makedirs(pasta_saida, exist_ok=True)

# arquivo de nomes (assumido na mesma pasta de trabalho)
arquivo_mapa = os.path.join("10 - Nomes_estabelecimentos.txt")

# regex para ignorar linhas com data
regex_data = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")

# ---------------- FUNÇÕES AUXILIARES ----------------
def carregar_mapa_estabelecimentos(caminho):
    mapa = {}
    if not os.path.exists(caminho):
        print("⚠️ Arquivo de nomes não encontrado! Prosseguirei com nomes do relatório.")
        return mapa

    with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            # separa em CNES e nome (primeiro token = CNES)
            partes = linha.split(maxsplit=1)
            if len(partes) == 2:
                cnes_key = partes[0].strip()
                nome = partes[1].strip()
                mapa[cnes_key] = nome
    print(f"✅ Carregados {len(mapa)} nomes de estabelecimentos de: {caminho}")
    return mapa

# remove caracteres proibidos no Excel (\x00-\x1F)
def clean_excel_string(s):
    if isinstance(s, str):
        return re.sub(r'[\x00-\x1F]', '', s)
    return s

# Converte uma string de valor em um float, removendo pontos de milhar e garantindo 2 casas decimais.
def parse_float_from_field(s):
    if s is None:
        return 0.0
    s = s.strip()
    if not s:
        return 0.0
    # remove pontos (milhar) e espaços
    s = s.replace(".", "").replace(" ", "")
    s = s.replace(",", ".") # Substitui vírgula decimal por ponto

    try:
        # Converte para float e usa round() para garantir 2 casas decimais
        return round(float(s), 2)
    except:
        return 0.0

# ---------------- PROCESSAMENTO DE ARQUIVO ----------------
MAPA_NOMES = carregar_mapa_estabelecimentos(arquivo_mapa)

def processar_analitico(caminho):
    """
    Processa arquivo ANALÍTICO (RAPROCED) e retorna DataFrame com colunas solicitadas.
    Usa extração por posições fixas.
    """
    with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
        linhas = [ln.rstrip("\n") for ln in f]

    registros = []
    cnes_atual = ""
    estabelecimento_relatorio = ""
    
    # OBSERVAÇÃO: A função parse_float_from_field está truncando os centavos.
    # Se você precisar de centavos, precisará adaptar para usar float.

    for linha in linhas:
        if not linha:
            continue
        linha_raw = linha
        linha_strip = linha_raw.strip()

        # Filtragem de linhas irrelevantes (igual ao RAPROCQT)
        if (linha_strip.startswith("Pagina") or
            linha_strip.startswith("SMS-ARARAQ") or
            regex_data.search(linha_strip) or
            linha_strip.startswith("********") or
            linha_strip.startswith("CMP") or
            linha_strip.startswith("_ SINTETICO") or
            linha_strip.upper().startswith("CMP   PROCEDIMENTO")):
            continue

        # Identificação da Unidade (CNES e Estabelecimento) (igual ao RAPROCQT)
        if linha_strip.startswith("Unidade"):
            cnes_atual = linha_raw[8:15].strip()
            estabelecimento_relatorio = linha_raw[16:].strip()

            nome_mapa = MAPA_NOMES.get(cnes_atual)
            if nome_mapa:
                estabelecimento = nome_mapa
            else:
                estabelecimento = estabelecimento_relatorio

            estabelecimento_atual = estabelecimento
            continue

        if linha_strip.startswith("TOTAL DA UNIDADE"):
            continue

        # Extração dos Registros de Procedimento com NOVAS POSIÇÕES e NOMES
        if len(linha_raw) >= 6:
            competencia = linha_raw[0:6].strip()
            if not competencia.isdigit():
                continue

            # NOVAS POSIÇÕES (1-based positions do usuário)
            # competencia  = posição 1 a 6  -> [0:6]
            # procedimento = posição 8 a 17 -> [7:17]
            # apac         = posição 19 a 31 -> [18:31]
            # cbo          = posição 33 a 38 -> [32:38]
            # vlr_produzido = posição 40 a 53 -> [39:53] **Ajuste aqui**
            # vlr_aprovado = posição 55 a 68 -> [54:68] **Ajuste aqui**
            # situacao     = posição 70 até o final da linha -> [69:] **Ajuste aqui**
            
            procedimento = linha_raw[7:17].strip()
            apac = linha_raw[18:31].strip()
            cbo = linha_raw[32:38].strip()
            vlr_produzido_raw = linha_raw[39:53].strip()  # Posição 40 a 53
            vlr_aprovado_raw = linha_raw[54:68].strip()   # Posição 55 a 68
            situacao = linha_raw[69:].strip()             # Posição 70 até o final

            tipo = "APAC" if apac else "BPA/RAAS"
            vlr_produzido = parse_float_from_field(vlr_produzido_raw)
            vlr_aprovado = parse_float_from_field(vlr_aprovado_raw)

            registros.append({
                "Competência": competencia,
                "CNES": cnes_atual,
                "Estabelecimento": estabelecimento_atual if 'estabelecimento_atual' in locals() else estabelecimento_relatorio,
                "Tipo": tipo,
                "Procedimento": procedimento,
                "Valor Produzido": vlr_produzido, # NOME ALTERADO
                "Valor Aprovado": vlr_aprovado,   # NOME ALTERADO
            })

    df = pd.DataFrame(registros)

    # LIMPA CARACTERES ILEGAIS DO EXCEL
    df = df.applymap(clean_excel_string)

    # ✅ Converter Competência YYYYMM → MM/YYYY
    df["Competência"] = df["Competência"].astype(str).str.replace(
        r"(\d{4})(\d{2})", r"\2/\1", regex=True
    )

    # ✅ Agrupamento com NOVOS NOMES DE COLUNAS
    df = df.groupby(
        ["Competência", "CNES", "Estabelecimento", "Tipo", "Procedimento"],
        as_index=False
    ).agg({
        "Valor Produzido": "sum", # NOME ALTERADO
        "Valor Aprovado": "sum"    # NOME ALTERADO
    })

    # ✅ Garante ordem das colunas
    df = df[
        [
            "Competência",
            "CNES",
            "Estabelecimento",
            "Tipo",
            "Procedimento",
            "Valor Produzido", # NOME ALTERADO
            "Valor Aprovado",  # NOME ALTERADO
        ]
    ]

    return df


# ---------------- LOOP PRINCIPAL (apenas RAPROCED) ----------------
for nome_arquivo in os.listdir(pasta_entrada):
    caminho = os.path.join(pasta_entrada, nome_arquivo)
    if not os.path.isfile(caminho):
        continue

    # FILTRO ALTERADO para RAPROCED
    if "RAPROCED" not in nome_arquivo.upper():
        print(f"⚠️ Pulando (não RAPROCED): {nome_arquivo}")
        continue

    print(f"Processando: {nome_arquivo} ...")
    try:
        df = processar_analitico(caminho)
        # Suffix alterado para refletir que é o financeiro
        nome_saida = os.path.splitext(nome_arquivo)[0] + "_financeiro_resumido.xlsx"
        caminho_saida = os.path.join(pasta_saida, nome_saida)
        df.to_excel(caminho_saida, index=False)
        print(f"✅ Gravado: {nome_saida} (linhas: {len(df)})")
    except Exception as e:
        print(f"❌ Erro ao processar {nome_arquivo}: {e}")

print("\n🎉 Processamento concluído.")