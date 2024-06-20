# Desafio 03
# Desenvolver um programa para uma loja de lanches(MAC)
# Requisitos:
# - O Usuario vai receber uma mensagem de boas vindas
# - O Sistema irá pedir qual seria a opçãode lanche (nº1, ...)
# - O Sistema ira retornar o nome lanche e o valor dele
# - Usar pelo menos 4 Opções de lanche
# - Para resolver usar listas

lista_de_lanches = "BigMac", "Cheddar", "Quarteirão", "Big Tasty"
lista_de_precos = [29.99, 27.90, 18.50, 35.60]
print("-----------Bem vindo ao MAC SENAI----------")
opcao = int(input("Digite sua opcao de lanche (1 a 4):"))

print("Seu lanche escolhido foi ", lista_de_lanches[opcao - 1])
print("O valor do lanche é R$", lista_de_precos[opcao - 1])