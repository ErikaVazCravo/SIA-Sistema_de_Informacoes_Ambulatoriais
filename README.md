|![DataSUS](img/Logo DataSUS.jpg)|![SIA](img/Logo SIA.jpg)|

**SIA – Faturamento Ambulatorial** 💵

O SIA é o sistema responsável pelo processamento das informações de atendimentos ambulatoriais realizados por prestadores públicos e privados contratados ou conveniados ao SUS.
As informações são captadas por meio dos seguintes instrumentos de registro:

•	APAC

•	RAAS

•	BPA-I / BPA-C

•	SISCAN

As automações desenvolvidas neste repositório têm como objetivo a otimização das atividades dentro deste sistema que, normalmente, demandariam tempo e esforço manual.

🔮 **Automatizações:**

**01 - Relatórios para prestadores**

    Automação criada para gerar os três relatórios abaixo relacionados:
    _ Sintético de procedimento por unidade;
    _ Sintético de procedimentos por unidade / físico;
    _ Sintético de CBO por unidade.
    Esses relatórios são gerados para todos os CNES existente no arquivo txt, onde constam os números de CNES e Nomes dos Estabelecimentos.

**02 - Renomeia relatórios para prestadores**

    Automação criada para renomear os arquivos gerados no 01 - Relatórios para prestadores.py  (os arquivos gerados neste código apresentam o número de CNES e não o nome do estabelecimento). 
    Aqui também é utilizado o arquivo txt onde constam os números de CNES e Nomes dos Estabelecimentos (mesmo utilizado em 01 - Relatórios para prestadores.py).

**03 - Renomeia relatorios de ocorrencias**

    Essa automação foi feita para renomear os arquivos gerados a partir do relatório de erros que o SIA emite após cada consistência (R0350 - RELATORIO DE OCORRENCIAS NA CONSISTENCIA).
    É necessário fazer a separação manual dos estabelecimentos, antes de executar esse código.

**04 - Imprime APACs**

    Essa automação tem o objetivo de gerar o espelho de APAC que é apresentado no SIA, a partir da relação de números de APACs que constam no arquivo 04 - Lista de números de APACs.txt

**04 - Lista de números de APACs.txt**

    Colocar os números de APAC, um embaixo do outro.

**05 - Relatório Sintético de procedimentos por unidade - físico**

    Automação que irá emitir somente o relatório: Sintético de procedimentos por unidade / físico.
    Aqui também é utilizado o arquivo txt onde constam os números de CNES e Nomes dos Estabelecimentos (mesmo utilizado em 01 - Relatórios para prestadores.py).

**06 - Relatório Analítico de procedimentos por unidade - físico**

    Automação que irá emitir somente o relatório: Analítico de procedimentos por unidade / físico.
    Aqui também é utilizado o arquivo txt onde constam os números de CNES e Nomes dos Estabelecimentos (mesmo utilizado em 01 - Relatórios para prestadores.py).
 
**07 - Conta Qtde Procedimentos - xlsx**

    A partir dos relatórios emitidos na automação 06 - Relatório Analítico de procedimentos por unidade - físico.py, essa automação irá gerar um arquivo xlsx onde constará os procedimentos e seus totais de cada estabelecimento.
    Aqui também é utilizado o arquivo txt onde constam os números de CNES e Nomes dos Estabelecimentos (mesmo utilizado em 01 - Relatórios para prestadores.py).
