
#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será 
#a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número,
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
# pertence ou não a sequência

n = int(input("Informe o número: "))
soma = 0
valor1 = 1
valor2 = 1
if(n==0 or n==1):
    print(f"O número {n} pertence a sequência de Fibonacci")
else:
    while soma < n:
        soma = valor1 + valor2
        valor2 = valor1
        valor1 = soma
    if(soma==n):
        print(f"O número {n} pertence a sequência de Fibonacci")
    else:
        print(f"O número {n} NÃO pertence a sequência de Fibonacci")