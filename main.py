# 7. Faça um código que receba o valor da base e da altura de um triângulo e calcule sua área. usando a fórmula A =(base x Altura ) /2

base = float(input("Qual a Base do triangulo?: "))
altura = float(input("Qual a Altura do triangulo?: "))

a = (base * altura)/2

print(f"A área do triangulo é {a}")