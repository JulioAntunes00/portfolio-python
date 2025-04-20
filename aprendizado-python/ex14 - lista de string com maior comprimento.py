#Crie um loop for que percorra uma lista de strings e imprima a string de maior comprimento.

lista = ["maçã", "banana", "abacaxi", "laranja", "morango"]

maior_lista = ""

for s in lista:
    if len(s) > len(maior_lista):
        maior_lista = s

print(f"O nome de maior comprimento é: {maior_lista}")