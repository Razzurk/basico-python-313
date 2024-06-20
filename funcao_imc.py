# Modulo de calculo do IMC

def calcularIMC(altura,peso):
    
    imc = peso / (altura ** 2)

    return imc

# Modulo mensagem ao usuario do IMC
def imprimirIMC(imc):
    print(f"Olá usuario, seu IMC é {imc}!!!")

# modulo de mensagem de boas vindas

def imprimirBoasVindas():
    print("*********** SISTEMA DE CALCULO DO IMC ****************")
    print("Olá, seja bem vindo ao sistema de calculo do IMC")

# Modulo principal
def main():
    imprimirBoasVindas()

    resultado = calcularIMC(1.70,65)
    resultado = round(resultado,2)

    imprimirIMC(resultado)


if __name__ == "__main__":
    main()