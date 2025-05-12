#algoritmo para calcular o gasto total da granja para marcar todos os seus frangos.

frangos = int(input("Olá, digite a quantidade de frangos: "))
print ("=============================================================================")

anel_chip = frangos * 4.00
anel_alimentos = frangos * (3.50 * 2)
total = anel_alimentos + anel_chip

print ("O total gasto para marcar todos os frangos são de: ",total)