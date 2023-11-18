# 12. Escreva um algoritmo para ler o
# número total de eleitores de um
# município, o número de votos brancos,
# nulos e válidos. Calcular e escrever o
# percentual que cada um representa em
# relação ao total de eleitores.

votos_brancos = int(input("Quantos votos brancos?: "))
votos_nulos = int(input("Quantos votos brancos?: "))
votos_validos = int(input("Quantos votos brancos?: "))

total = votos_brancos + votos_nulos + votos_validos

percent_brancos = (votos_brancos/total)*100
percent_nulos = (votos_nulos/total)*100
percent_validos = (votos_validos/total)*100

print(f"A porcentagem de Votos Brancos é {percent_brancos:.1f}%")
print(f"A porcentagem de Votos Nulos é {percent_nulos:.1f}%")
print(f"A porcentagem de Votos Validos é {percent_validos:.1f}%")