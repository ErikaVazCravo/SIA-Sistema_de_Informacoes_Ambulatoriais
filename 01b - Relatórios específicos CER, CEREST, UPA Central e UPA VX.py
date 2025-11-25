# Automação criada para gerar o relatório 
# SINTETICO DE REGRAS CONTRATUAIS - UNIDADE

# Será emitido somente para as unidades cujo CNES está relacionado em lista_cnes.


import pyautogui
import time

# Marca o início do processamento
inicio = time.time()

# Lista fixa de CNES - coloque aqui os números de CNES
lista_cnes = [
    "3317676",
    "9074368",
    "2064731",
    "4047184"
]

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


# ---------- Relatório: SINTETICO DE REGRAS CONTRATUAIS - UNIDADE ----------
pyautogui.press("down", presses=4, interval=0.3)
pyautogui.press("enter")

for cnes in lista_cnes:
    time.sleep(1)
    pyautogui.press("enter", presses=2)
    pyautogui.write(cnes)
    pyautogui.write(cnes)
    pyautogui.press("enter", presses=8, interval=0.3)
    pyautogui.press("right")
    pyautogui.press("enter", presses=2)
    pyautogui.press("right")
    pyautogui.press("enter")
    pyautogui.write("EGRASCONTR_" + cnes)
    pyautogui.press("enter", interval=0.5)
    pyautogui.press("enter")
    pyautogui.press("down", presses=4, interval=0.3)
    pyautogui.press("enter")


pyautogui.press("esc")

print('Relatórios emitidos')

# Marca o fim do processamento
fim = time.time()
tempo_total = fim - inicio
minutos = int(tempo_total // 60)
segundos = int(tempo_total % 60)
print(f"\nProcesso concluído em {minutos} minutos e {segundos} segundos!")
