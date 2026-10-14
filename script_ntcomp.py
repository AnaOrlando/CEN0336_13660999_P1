import sys

#Solicitando a sequência de DNA e convertendo as letras para maiúsculas
sequencia = input("Digite a sequência de DNA: ").strip().upper()

#Validando se a entrada não está vazia e se contém apenas os caracteres válidos, ou seja, A, T, C, G)
if not sequencia:
    print("Erro: A sequência de DNA não pode estar vazia.")
    sys.exit(1)

for caractere in sequencia:
    if caractere not in ['A', 'T', 'C', 'G']:
        print("Erro: A sequência fornecida é inválida! Utilize apenas os nucleotídeos A, T, C e G.")
        sys.exit(1)

#Inicializando os contadores para cada um dos nucleotídeos
count_a = 0
count_t = 0
count_c = 0
count_g = 0

#Utilizando um loop for para iterar sobre a sequência e realizar a contagem
for nucleotideo in sequencia:
    if nucleotideo == 'A':
        count_a += 1
    elif nucleotideo == 'T':
        count_t += 1
    elif nucleotideo == 'C':
        count_c += 1
    elif nucleotideo == 'G':
        count_g += 1

#Exibindo os resultados no formato solicitado pela questão
print(f"A: {count_a}")
print(f"T: {count_t}")
print(f"C: {count_c}")
print(f"G: {count_g}")
