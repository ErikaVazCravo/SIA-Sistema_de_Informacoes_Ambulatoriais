# Automação que irá emitir somente o relatório: Sintético de procedimentos por unidade / físico 
# Iremos utilizar també o arquivo txt onde constam os números de CNES e Nomes dos Estabelecimentos (mesmo utilizado em 01 - Relatórios para prestadores.py)

import pyautogui
import time
import re


# Define o caminho do arquivo contendo os CNES e nomes dos estabelecimentos
caminho_arquivo = r"coloque o caminho aqui"


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

# Pressiona "right" 5 vezes para navegar até "Operador"
for _ in range(5):
    pyautogui.press("right")
    time.sleep(0.3)

# Pressiona "Enter" para abrir o menu Operador
pyautogui.press("enter")
time.sleep(1)

# Pressiona "Down" 8 vezes para chegar em "Relatórios Gerenciais"
pyautogui.press("down", presses=8, interval=0.3)

# Pressiona "Enter" para selecionar a opção
pyautogui.press("enter")



# Relatório a ser emitido é
# Sintético de procedimentos por unidade / físico

# Selecionando o relatório sintético de procedimentos por unidade / físico
pyautogui.press("down", presses=2, interval=0.3)
pyautogui.press("enter")

# Loop para processar cada CNES na lista
for cnes in lista_cnes:

    time.sleep(1)  # Aguarda para evitar falhas
    pyautogui.press("enter", presses=2)

    # Digita o CNES
    pyautogui.write(cnes)
    pyautogui.write(cnes)

    # Pular os campos que não serão preenchidos
    pyautogui.press("enter", presses=16, interval=0.3)

    # Escolher o tipo de impressão (emissão de relatório) 
    pyautogui.press("right")
    pyautogui.press("enter")
    pyautogui.write("Proc/Fis_"+cnes)
    pyautogui.press("enter", presses=2, interval=0.3)

    # Selecionando o relatório intético de procedimentos por unidade / físico
    pyautogui.press("down", presses=2, interval=0.3)

    # Pressiona "Enter" para selecionar a opção
    pyautogui.press("enter")

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



