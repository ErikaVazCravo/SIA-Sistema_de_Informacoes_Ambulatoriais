# Emite o Relatório Analítico de Procedimentos por Unidade / Físico
# Para todos os CNES do arquivo NOMES_CNES.txt
# Os arquivos serão renomeados a partir do arquivo "10 - Nomes_estabelecimentos.txt"

import pyautogui
import time
import re
import os

# ======================= CONFIGURAÇÕES ============================

# Define o caminho do arquivo onde constam os números de CNES e Nomes dos Estabelecimentos
caminho_arquivo = r"coloque aqui o caminho"

# Lista de como quero que os estabelecimentos sejam nomeados - por exemplo: Todos as unidades que pertencem 
# à Prefeitura, acrescentei o prefixo "PREF - " ao nome, para poder separar a produção de prestadores e unidades 
# da Prefeitura
arquivo_nomes = r"10 - Nomes_estabelecimentos.txt"

# >>>>> INFORME AQUI A PASTA ONDE OS TXT SÃO GERADOS <<<<<
pasta_saida = r"coloque o caminho aqui"

# ======================= INICIO ============================
inicio = time.time()

# -------------------- LER CNES --------------------
lista_cnes = []

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    match = re.search(r"\d{3}\.\d{3}-\d", linha)
    if match:
        cnes = match.group()
        cnes = cnes.replace(".", "").replace("-", "")
        lista_cnes.append(cnes)


# -------------------- ### NOVO: LER NOME DOS ESTABELECIMENTOS --------------------
dicionario_nomes = {}

with open(arquivo_nomes, "r", encoding="utf-8") as arq:
    for linha in arq:
        linha = linha.strip()
        if not linha:
            continue

        partes = linha.split("\t")
        if len(partes) >= 2:
            cnes_ref = partes[0].strip()
            nome_est = partes[1].strip()
            dicionario_nomes[cnes_ref] = nome_est

# =============================================================
#          EXECUÇÃO NORMAL DA GERAÇÃO DOS RELATÓRIOS
# =============================================================

print('Selecione o programa')
time.sleep(3)

for _ in range(5):
    pyautogui.press("right")
    time.sleep(0.3)

pyautogui.press("enter")
time.sleep(1)

pyautogui.press("down", presses=8, interval=0.3)
pyautogui.press("enter")

pyautogui.press("down", presses=3, interval=0.3)
pyautogui.press("enter")


for cnes in lista_cnes:

    time.sleep(1)

    pyautogui.press("enter", presses=2)

    pyautogui.write(cnes)
    pyautogui.write(cnes)

    pyautogui.press("enter", presses=16, interval=0.3)

    pyautogui.press("right")
    pyautogui.press("enter")

    nome_base = f"Proc_Fis_{cnes}"
    pyautogui.write(nome_base)

    pyautogui.press("enter", presses=2, interval=0.3)

    pyautogui.press("down", presses=3, interval=0.3)
    pyautogui.press("enter")

pyautogui.press("esc")

print("Relatórios emitidos!")
time.sleep(3)

# =============================================================
#          ### NOVO: RENOMEAR ARQUIVOS GERADOS
# =============================================================

arquivos = os.listdir(pasta_saida)

for cnes in lista_cnes:

    nome_base = f"Proc_Fis_{cnes}"

    # procura arquivo existente
    encontrado = None
    for a in arquivos:
        if a.startswith(nome_base):
            encontrado = a
            break

    if encontrado:
        caminho_antigo = os.path.join(pasta_saida, encontrado)

        nome_est = dicionario_nomes.get(cnes, "SEM_NOME")  # fallback
        novo_nome = f"{nome_base} - {nome_est}.txt"
        caminho_novo = os.path.join(pasta_saida, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {encontrado} → {novo_nome}")
    else:
        print(f"⚠ Arquivo não encontrado para: {cnes}")


# ---------------------- FIM ----------------------
fim = time.time()
temp = fim - inicio
minutos = int(temp // 60)
segundos = int(temp % 60)

print(f"\nProcesso concluído em {minutos} minutos e {segundos} segundos!")
