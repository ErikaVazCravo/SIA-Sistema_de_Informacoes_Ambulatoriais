# Essa automação tem o objetivo de imprimir o espelho de APAC que é apresentado n SIA, a partir da relação de números de APACs que
# constam no arquivo 04 - Lista de números de APACs.txt

import pyautogui
import time
import re

# Define o caminho do arquivo
caminho_arquivo = r"04 - Lista de números de APACs.txt"

# Marca o início do processamento
inicio = time.time()

# Lista para armazenar os números das APACs
lista_apac = []

# Abre o arquivo e lê as linhas
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Percorre cada linha em busca dos números das APACs
for linha in linhas:
    lista_apac.append(linha)  # Adiciona à lista

# Exibe os CNES extraídos
#print("Lista de CNES extraídos:")
#print(lista_cnes)

# Aguarda um tempo para você selecionar manualmente a janela do sistema
print('Selecione o programa')
time.sleep(3)

# Pressiona "right" 2 vezes para navegar até "Produção"
pyautogui.press("right", presses=2, interval=0.3)

# Pressiona "Enter" para abrir o menu Produção
pyautogui.press("enter")
time.sleep(0.3)

# Pressiona "Down" 6 vezes para chegar em "Pesquisa / Exclusão de APAC"
pyautogui.press("down", presses=6, interval=0.3)

# Pressiona "Enter" para selecionar a opção
pyautogui.press("enter")



# Loop para processar cada APAC na lista
for apac in lista_apac:

    time.sleep(0.3)  # Aguarda para evitar falhas
    pyautogui.press("enter", presses=3, interval=0.3)

    # Digita o número da APAC
    pyautogui.write(apac)
    
    # Pular os campos que não serão preenchidos
    pyautogui.press("enter", presses=9, interval=0.3)

    # Escolher o tipo de impressão (emissão de relatório) 
    pyautogui.press("F7")
    pyautogui.press("right")
    pyautogui.press("enter")
    pyautogui.write(apac)
    pyautogui.press("enter", interval=0.3)
    pyautogui.press("esc", interval=0.3)


print('APACs emitidas')



# Marca o fim do processamento
fim = time.time()

# Calcula o tempo total e exibe em minutos e segundos
tempo_total = fim - inicio
minutos = int(tempo_total // 60)
segundos = int(tempo_total % 60)

print(f"\nProcesso concluído em {minutos} minutos e {segundos} segundos!")



