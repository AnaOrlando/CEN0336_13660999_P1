import sys

#Verificando  se foram passados 7 argumentos
if len(sys.argv) != 8:
    print("Erro: Forneça 7 argumentos: a sequência de DNA e as coordenadas n1 n2 n3 n4 n5 n6.")
    sys.exit(1)

#Capturando a sequência de DNA e convertendo para maiúsculas
seq_dna = sys.argv[1].strip().upper()

#Capturando os argumentos (devem ser números inteiros)
coords_args = sys.argv[2:]

#Verificando se os 6 argumentos de coordenadas contêm apenas dígitos
for arg in coords_args:
    if not arg.isdigit():
        print(f"Erro: O argumento '{arg}' não é um número inteiro válido.")
        sys.exit(1)

#Convertendo as coordenadas para o tipo inteiro
n1 = int(sys.argv[2])
n2 = int(sys.argv[3])
n3 = int(sys.argv[4])
n4 = int(sys.argv[5])
n5 = int(sys.argv[6])
n6 = int(sys.argv[7])

#Obtendo o tamanho total da sequência de DNA
tam_seq = len(seq_dna)

#Verificando se nenhuma coordenada é maior que o tamanho da sequência
if n1 > tam_seq or n2 > tam_seq or n3 > tam_seq or n4 > tam_seq or n5 > tam_seq or n6 > tam_seq:
    print(f"Erro: Nenhuma coordenada pode ser maior que o tamanho da sequência ({tam_seq} nt).")
    sys.exit(1)

#Extraindo o intron 1 (sequência entre CDS 1 e CDS 2)
intron1 = seq_dna[n2 : n3 - 1]

#Extraindo o intron 2 (sequência entre CDS 2 e CDS 3)
intron2 = seq_dna[n4 : n5 - 1]

#Verificando se o início é em GT e se o término é em AG
valido_intron1 = intron1.startswith("GT") and intron1.endswith("AG")
valido_intron2 = intron2.startswith("GT") and intron2.endswith("AG")

#Extraindo e concatenado as CDSs, se ambos os introns forem válidos
if valido_intron1 and valido_intron2:
    cds1 = seq_dna[n1 - 1 : n2]
    cds2 = seq_dna[n3 - 1 : n4]
    cds3 = seq_dna[n5 - 1 : n6]
    cdna = cds1 + cds2 + cds3
    print(cdna)
else:
    print("Erro: As sequências entre as CDSs não possuem início em GT e término em AG.")
