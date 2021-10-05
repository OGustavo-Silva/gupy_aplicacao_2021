# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de 
# representação que cada estado teve dentro do valor total mensal da distribuidora.


estados_array = ["SP", "RJ", "MG", "ES", "OUTROS"]
faturamento_array = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

soma_faturamentos = 0

for valor in faturamento_array:
    soma_faturamentos += valor

porcen_total = soma_faturamentos/100

fatur_porc_array = []
for valor in faturamento_array:
    valor_porc = (valor * 100)/soma_faturamentos
    fatur_porc_array.append(valor_porc)

dict_final = dict(zip(estados_array, fatur_porc_array))

print("Relação Estado e porcentagem que cada tem do valor total:")
for dado in dict_final:
    print(dado, ":", dict_final[dado])