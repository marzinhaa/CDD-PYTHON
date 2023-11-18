# 15. Escreva um algoritmo para ler dois
# valores (considere que não serão lidos
# valores iguais) e escrevê-los em ordem
# crescente

num1 = int(input("Qual o 1° valor?: "))
num2 = int(input("Qual o 2° valor?: "))

if num1 > num2:
    print(f"{num2}, {num1}")
else:
    print(f"{num1}, {num2}")