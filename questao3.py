# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

file = open('./dados.json',)

array_dados = json.load(file)
array_dados_sem_zeros = [dado for dado in array_dados if dado["valor"] != 0.0]

valor_minimo = float("inf")
valor_maximo = 0
soma = 0


for lista in array_dados_sem_zeros:
    valor = lista["valor"]
    
    if valor < valor_minimo:
        valor_minimo = valor
    if valor > valor_maximo:
        valor_maximo = valor

    soma += valor

media = soma/len(array_dados_sem_zeros)

print(f"O valor mínimo foi {valor_minimo}\nO valor máximo foi {valor_maximo}\nA média é de {media}")
