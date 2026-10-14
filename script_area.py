import sys

#Verificando se foram fornecidos dois argumentos na linha de comando
if len(sys.argv) != 3:
    print("Erro: digite dois números inteiros positivos")
    sys.exit(1)

#Capturando os argumentos fornecidos na linha de comando

arg1 = sys.argv[1]
arg2 = sys.argv[2]

#Verificando se os argumentos fornecidos são inteiros positivos
if not (arg1.isdigit() and arg2.isdigit()):
    print("Erro: informe apenas números inteiros positivos")
    sys.exit(1)

#Convertendo os valores válidos para o tipo inteiro (int)

a = int(arg1)
b = int(arg2)

#Verificando se os valores estão dentro do intervalo permitido (maiores que zero e menores que 500)
if a <= 0 or b <= 0 or a >= 500 or b >= 500:
    print("Erro: os valores a e b devem ser maiores que 0 e menores que 500")
    sys.exit(1)

#Calculando a área
A = (a * b) / 2

#Exibindo o resultado conforme solicitado na questão)
print(f"A área do triangulo retângulo com lados a={a} e b={b}, é {A}")
