# Python-Projects
Projects created or changed by me


# "teste IA.py"

- Programa teste criado para IA
- Programa baseado em outro já feito chamado "PRISM"
- É um sistema RULE BASED
- Apriori era para ser um programa que se enquadra em Machine Learning mas está mais para Deep Learning no momento
  - Isso porque o programa gerá as regras por si próprio a partir de um dataset definido sem a necessidade de falar a tabela desejada para gerar a regra

Ainda possui alguns problemas envolvidos como:
- Colunas do dataset com valores iguais gerará problemas
- Falta validar regras acima da mais baixa

Ainda há um custo computacional alto envolvido, falta algumas revisões para melhorar essa lógica e tornar o programa completamente funcional.

Resultado final em 18/06/2021: Gera regras certas e algumas poucas erradas mesmo após algumas validações.

## Commits antigos do programa:
**https://github.com/GuilhermeSenna/InterfaceScrape/commits/main**

## Programa introdutório para IA = 14/06/2021
- Lê de um arquivo CSV
- Converte para Dict
- Lógicas de conversão para Dict, List e híbrida
- Separa por variáveis (nome, sexo) e valor das variáveis (M e F em sexo, por exemplo)
- Obtém a porcentagem de cada valor das variáveis e atribui ao dicionário
 main
 
 
 ## Modularização e retira ocorrências manualmente = 14/06/2021
- Uso de funções para proporcionar modularização ao código
- Pega todas os índices das ocorrências na lista que não correspondem a desejada.
- Retira do dicionário, permitindo uma forma de enxergar as regras
 
 ## Novo .csv para testes = 14/06/2021 (TARDE)
 
## Lógica incompleta para gerar regras = 14/06/2021
- Gera regras incompletas
- Lógica para armazenar as regras em uma lista
- Gera combinações para poder gerar as regras dinamicamente
- Retira variáveis a partir dessas combinações para a geração de regras
 
 ## Tentativas de corrigir o problema = 14/06/2021
 - Problema acima

## Outras tentativas de corrigir o problema = 15/06/2021

## Gerando regras retirando colunas manualmente = 15/06/2021 (NOITE)
- Agora funciona a remoção de regras ambiguas e inuteis
- Falta incorporar para funcionar em loop

## Loop para geração de todas as regras = 17/06/2021
- Agora foi conseguido colocar para gerar todas as regras com todas as possibilidades
- Regras repetidas e erradas (as menores)
- Falta definir a coluna do atributo que queremos para poder "ignorá-la" quando retirar ocorrências

## Validação para a menor regra = 17/06/2021
- Agora é validado das regras obtidas quais são válidas para uso
- Dessa forma será utilizado para retirar regras maiores que usam ela como subregra (logo deixam de ser válidas)

## Condicional otimizada = 17/06/2021

## Teste para validar regras intermediárias = 18/06/2021
 
