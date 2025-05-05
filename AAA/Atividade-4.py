print("Seja Bem-vindo!")
print("-"*20)
#defina os custos dos aneis 
custo_anel_chip = 4.00
custo_anel_alimento = 3.50
numero_frangos = int(input("Digite o número total de frangos: "))
print("-"*20)
custo_por_frango = custo_anel_chip + (2 * custo_anel_alimento)
custo_total = custo_por_frango * numero_frangos
print(f"O custo total para marcar todos é: R$ {custo_total:2f}")
print("-"*20)