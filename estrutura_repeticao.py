# ESTRUTURAS DE REPETIÇÃO

#frutas = ["pera","maçã","banana","melancia","laranja", "abacate", "abacaxi", "limão"]

# Estrutura de Repetição FOR------------------------------------------------------------------------

#for i in range(8):
#   print(i,"--", frutas[i])

#for i in range(3,6):
#    print(i, " ", frutas[i])

#for exemplooo in range(15):
#   print(exemplooo)

#for fruta in frutas:
 #   print(fruta)

#tamanho_listas_frutas = len(frutas)
#print(tamanho_listas_frutas)

#for i in range(len(frutas)):
#    print(i, "  ", frutas [i])

#Estrutura de repetição WHILE -----------------------------------------------------------------------

#contador = 0
#while contador <= 50:
#    print(contador)
#    contador = contador + 1

#valor = 0
#resultado = 0
#multiplo= 9

#while valor <= 10:
#    print(f"{multiplo} x {valor} = {resultado}" )
#    valor += 1
#    resultado += multiplo

nota = int(input("Digite sua nota"))

while nota< 0 or nota >100:
    print("sua nota deve estar entre 0 e 100, digite novamente")
    nota = int(input("Digite sua nota:"))