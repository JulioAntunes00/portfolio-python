#Escreva um loop for que percorra uma lista de números e use continue para pular a impressão dos números divisíveis por 3.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numeros:
    if num % 3 == 0:
        continue
    print(num)