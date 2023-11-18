# 16. Escreva um algoritmo para ler a hora de
# início e a hora de fim de um jogo de Xadrez
# (considere apenas horas inteiras, sem os
# minutos) e calcule a duração do jogo em
# horas, sabendo-se que o tempo máximo de
# duração do jogo é de 24 horas e que o jogo
# pode iniciar em um dia e terminar no dia
# seguinte

inicio = int(input("Qual a hora de inicio do jogo?: "))
fim = int(input("Qual a hora do fim do jogo?: "))

duracao = fim - inicio

if inicio >= fim:
    duracao = (24 - inicio) + fim

print(f"A partida durou {duracao} horas")