# 11. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
idade = int(input("Qual a idade?: "))
mes = int(input("Qual o mes de nascimento?: "))
dia = int(input("Qual o dia de nascimento?: "))

idade_dias = (idade * 365) + (mes * 30) + dia

print(f"A idade em dias é {idade_dias}")