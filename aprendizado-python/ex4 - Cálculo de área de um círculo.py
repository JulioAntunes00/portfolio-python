#Peça ao usuário para digitar o raio de um círculo e calcule a área. A fórmula da área é A = πr², onde π = 3.14159.

raio = float(input("Digite o raio do círculo: "))
pi = 3.14159
area = pi * (raio ** 2)
print(f"A área do círculo é: {area:.2f}")
