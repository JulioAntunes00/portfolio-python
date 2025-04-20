# Programa que pula os números que são divisíveis por 3

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Vai passando por cada número da lista
for num in numeros:
    # Se for divisível por 3, ele ignora e vai pro próximo
    if num % 3 == 0:
        continue
    print(num)
