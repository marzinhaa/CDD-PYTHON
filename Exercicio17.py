# 17.As maçãs custam R$ 1,30 cada se forem
# compradas menos de uma dúzia, e R$ 1,00
# se forem
# compradas pelo menos 12. Escreva um
# programa que leia o número de maçãs
# compradas, calcule e
# escreva o custo total da compra.

qntd = int(input("Quantas maçãs?: "))
valor = 0
if qntd < 12:
    valor += 1.30
else:
    valor += 1.00

valor_macas = qntd * valor

print(f"O preço das maçãs é {valor_macas}")