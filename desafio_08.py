# As maçãs custam R$0.30	 cada	 se	 forem	 compradas	menos
# do	 que	 uma dúzia,	 e	 R$	 0.25	 se	 forem	 compradas	 
# pelo menos	 doze.	 Escreva	 um	 programa	 que	 leia	 
# o	 número de	 maçãs	 compradas,	 calcule  e escreva	 o	valor	
# total	da	compra.

print("---------Calculo de Maçãs---------")

macas = int(input("Digite a quantidade de maçãs:"))
macas_promo = macas * 0.25
macas_und = macas * 0.30

if macas >= 12:
        print(f"Suas maças custaram R${macas_promo}")

else:
        print(f"Suas maças custaram R${macas_und}")
