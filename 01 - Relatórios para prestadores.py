# Automação criada para gerar os três relatórios 
# que devem ser encaminhados para os prestadores 
# que possuem faturamento na competência.
# _ Sintético de procedimento por unidade
# _ Sintético de procedimentos por unidade / físico
# _ Sintético de CBO por unidade

# Serão gerados os 3 relatórios para cada CNES existente no arquivo txt onde constam os números de CNES e Nomes dos Estabelecimentos



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





# Como o primeiro relatório já está na primeira posição e só pressionar "Enter" para selecioná-lo
# Sintético de procedimento por unidade
pyautogui.press("enter")

# Loop para processar cada CNES na lista
for cnes in lista_cnes:

    time.sleep(1)  # Aguarda para evitar falhas
    
    pyautogui.press("enter", presses=2)

    # Digita o CNES
    pyautogui.write(cnes)
    pyautogui.write(cnes)

    # Pular os campos que não serão preenchidos
    pyautogui.press("enter", presses=17, interval=0.3)

    # Escolher o tipo de impressão (emissão de relatório) 
    pyautogui.press("right")
    pyautogui.press("enter", interval=0.3)
    pyautogui.write("Proc_"+cnes)
    pyautogui.press("enter", presses=3, interval=0.3)

# Sair da tela de emissão do relatório Sintético de procedimento por unidade
pyautogui.press("esc")




# Segundo relatório a ser emitido é
# Sintético de procedimentos por unidade / físico

# Como está selecionado o item relatórios gerenciais, precisamo clicar em enter
pyautogui.press("enter")

# Selecionando o relatório sintético de procedimentos por unidade / físico
pyautogui.press("down", presses=2, interval=0.3)

# Pressiona "Enter" para selecionar a opção
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





# Terceiro relatório a ser emitido é
# Sintético de CBO por unidade

# Como está selecionado o item relatórios gerenciais, precisamo clicar em enter
pyautogui.press("enter")

# Selecionando o relatório sintético de CBO por unidade
pyautogui.press("down", presses=8, interval=0.3)

# Pressiona "Enter" para selecionar a opção
pyautogui.press("enter")

# Loop para processar cada CNES na lista
for cnes in lista_cnes:

    time.sleep(1)  # Aguarda para evitar falhas

    pyautogui.press("enter", presses=2)

    # Digita o CNES
    pyautogui.write(cnes)
    pyautogui.write(cnes)

    # Pular os campos que não serão preenchidos
    pyautogui.press("enter", presses=15, interval=0.3)

    # Escolher o tipo de impressão (emissão de relatório) 
    pyautogui.press("right")
    pyautogui.press("enter")
    pyautogui.write("CBO_"+cnes)
    pyautogui.press("enter", interval=0.5)

    # Como está selecionado o item relatórios gerenciais, precisamo clicar em enter
    pyautogui.press("enter")

    # Selecionando o relatório sintético de CBO por unidade
    pyautogui.press("down", presses=8, interval=0.3)

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



