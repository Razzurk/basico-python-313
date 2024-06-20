#   Descobrir se o triangulo é
#   Equilátero (todos os lados iguais)
#   Isoceles (dois lados iguais)
#   Escaleno (todos os lados diferentes)

ladoA = int(input("Digite o tamanho do lado A "))
ladoB = int(input("Digite o tamanho do lado B "))
ladoC = int(input("Digite o tamanho do lado C "))

if ladoA == ladoB and ladoB == ladoC:
    print("Equilatero")
elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
    print("Isoceles")
else:
    print("escaleno")