# 8. Faça um código que receba 4 números e realize a soma deles e a média entre eles. e mostre os resultados.
soma = 0
for x in range(1,5):
    num = float(input("Qual o numero?: "))
    soma += num
media = soma/x
print(f"A média é {media}")
print(f"A soma é {soma}")
