# Programa que mostra qual palavra da lista é a mais longa

lista = ["maçã", "banana", "abacaxi", "laranja", "morango"]

# Começa com uma string vazia
maior_lista = ""

# Vai comparando o tamanho de cada palavra
for s in lista:
    if len(s) > len(maior_lista):
        maior_lista = s

# Mostra qual foi a maior
print(f"O nome de maior comprimento é: {maior_lista}")
