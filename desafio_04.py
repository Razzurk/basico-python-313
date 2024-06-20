
nota = int(input("Digite sua nota:"))

if nota > 70:
    print("Parabens, você foi aprovado!")
elif nota < 40:
    print("Você foi reprovado")
elif nota >= 40 and nota <= 70:
    print("Você esta de Recuperação")
else:
    print("Nota invalida")