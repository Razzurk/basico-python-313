# desafio 01 - Calculo do IMC
# Desenvolver um programa que calcule o IMC da pessoa, sendo que:
# Requisitos:
# - Peso e altura da pessoa será digitado pelo teclado (Dica: usar input())
# - A pessoa vai se identificar através do nome(Dica: usar input())
# - Realizar o cálculo padrão do IMC (Dica: usar operadores aritmeticos e variaveis)
# - Apresentar o resultado na tela com o Nome e o valor do IMC (Dica: usar print() com formatação print() e as variaveis)

nome = input("Digite seu nome:")
altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu Peso:"))

imc = peso/(altura*altura)
imc = round(imc, 2)

print(f"Olá {nome} , seu IMC é {imc} ")
