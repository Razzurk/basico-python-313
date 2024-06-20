# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   [x] 1. O aluno deverá digitar 3 notas através do teclado
#   [x] 2. Seu programa deverá calcular a média das notas    
#   [x] 3. A partir da média, verificar qual situação o aluno se encontra 
# conforme notas abaixo:
#       3.1 nota > 70 - aprovado
#       3.2 nota < 40 - reprovado
#       3.3 nota entre 40 e 70 - exame/recuperação
#   [x] 4. Não será permitido médias acima de 100 e abaixo de zero
#   [x] 5. Caso isso ocorrá o aluno deverá ser informado sobre um erro de digitação
#   [x] 6. Mostrar na tela para o aluno a situação final baseado na nota digitada.
print("---------☻ Resultado Final ☻----------")
nota1 = int(input("Digite sua primeira nota:"))
nota2 = int(input("Digite sua segunda nota:"))
nota3 = int(input("Digite sua terceira nota:"))

media_nota = (nota2+nota2+nota3)/3
media_nota = round(media_nota,2)

if media_nota >= 70 and media_nota <= 100:
    print(f"Sua media foi de {media_nota}, Parabens: voce foi aprovado")
elif media_nota < 40 and media_nota >= 0:
    print(f"Sua media foi de {media_nota}, Você foi reprovado")
elif media_nota >= 40 and media_nota < 70:
    print(f"Sua media foi de {media_nota}, Exame/Recuperação")
else:
    print("Medias de nota invalida")