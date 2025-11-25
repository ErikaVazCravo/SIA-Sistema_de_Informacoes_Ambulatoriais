# Relatório a ser emitido é
# EMISSÃO SÍNTESE DA PRODUCAO - BPA por CNES

import pyautogui
import time
import re


# Define o caminho do arquivo onde constam os números de CNES e Nomes dos Estabelecimentos
caminho_arquivo = r"coloque aqui o caminho"

# Marca o início do processamento
inicio = time.time()

# Lista para armazenar os CNES
lista_cnes = []

# Abre o arquivo e lê as linhas
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Percorre cada linha em busca dos códigos CNES
for linha in linhas:
    # Usa regex para capturar os códigos CNES (formato: números + ponto + números + traço + número)
    match = re.search(r"\d{3}\.\d{3}-\d", linha)
    if match:
        cnes = match.group()  # Pega o valor encontrado
        cnes = cnes.replace(".", "").replace("-", "")  # Remove ponto e traço
        lista_cnes.append(cnes)  # Adiciona à lista

# Exibe os CNES extraídos
#print("Lista de CNES extraídos:")
#print(lista_cnes)

# Aguarda um tempo para você selecionar manualmente a janela do sistema
print('Selecione o programa')
time.sleep(3)

# Pressiona "right" 4 vezes para navegar até "Vlr. Bruto"
for _ in range(4):
    pyautogui.press("right")
    time.sleep(0.3)

# Pressiona "Enter" para abrir o menu Operador
pyautogui.press("enter")
time.sleep(1)

# Pressiona "Down" 2 vezes para chegar em "EMISSÃO SÍNTESE DA PRODUCAO - BPA"
pyautogui.press("down", presses=2, interval=0.5)

# Pressiona "Enter" para selecionar a opção
pyautogui.press("enter")





# Relatório a ser emitido é
# EMISSÃO SÍNTESE DA PRODUCAO - BPA por CNES

# Selecionando o relatório
# Pressiona "Down" 2 vezes para chegar em "_ Um CNES"
pyautogui.press("down", presses=2, interval=0.3)


# Loop para processar cada CNES na lista
for cnes in lista_cnes:

    time.sleep(1)  # Aguarda para evitar falhas
    
    # Pressiona "Enter" para selecionar a opção
    pyautogui.press("enter")

    # Digita o CNES
    pyautogui.write(cnes)

    # Escolher o tipo de impressão (emissão de relatório) 
    pyautogui.press("right")
    pyautogui.press("enter")
    pyautogui.write("BPA_"+cnes)
    pyautogui.press("enter", interval=5)

# Sair da tela de emissão do relatório Sintético de procedimento por unidade / fisico
pyautogui.press("esc")

print('Relatórios emitidos')



# Marca o fim do processamento
fim = time.time()

# Calcula o tempo total e exibe em minutos e segundos
tempo_total = fim - inicio
minutos = int(tempo_total // 60)
segundos = int(tempo_total % 60)

print(f"\nProcesso concluído em {minutos} minutos e {segundos} segundos!")

