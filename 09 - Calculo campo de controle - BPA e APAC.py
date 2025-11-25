import os

# ============== PARÂMETROS ==============
pasta = r"Coloque aqui o caminho onde o arquivo está"
arquivo = os.path.join(pasta, "APTESTE1.OUT")  # Coloque aqui o nome do arquivo que será calculado o campo de controle
# ========================================

def _parse_int(s):
    try:
        return int(s.strip())
    except:
        return 0

def calcular_campo_controle(arquivo):
    soma_total = 0
    numero_apac = 0  # guardará o número da APAC da última linha tipo 14 lida

    with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
        for linha in f:
            tipo = linha[0:2]

            # ====== BPA-C e BPA-I ======
            if tipo == "02":  # BPAC
                proc = _parse_int(linha[27:36])
                qtd = _parse_int(linha[40:45])
                soma_total += proc + qtd

            elif tipo == "03":  # BPAI
                proc = _parse_int(linha[50:59])
                qtd = _parse_int(linha[89:94])
                soma_total += proc + qtd

            # ====== APAC ======
            elif tipo == "14":  # corpo da APAC
                numero_apac = _parse_int(linha[8:21])
                print ("APAC: " + str(numero_apac))
                soma_total += numero_apac

            elif tipo == "13":  # procedimento da APAC
                proc = _parse_int(linha[21:31])
                qtd = _parse_int(linha[37:44])
                print ("Proc.: " + str(proc) + ", Qtde: " + str(qtd))
                soma_total += proc + qtd

    resto = soma_total % 1111
    campo_controle = resto + 1111
    return campo_controle

# ================= EXECUÇÃO =================
if os.path.exists(arquivo):
    controle = calcular_campo_controle(arquivo)
    print(f"Campo de Controle: {controle}")
else:
    print("Arquivo não encontrado:", arquivo)
