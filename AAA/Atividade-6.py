# Entrada de dados  
print("_"*50)
latas = int(input("Número de latas (350 ml): "))  
garrafas_600ml = int(input("Número de garrafas de 600 ml: "))  
garrafas_2l = int(input("Número de garrafas de 2 litros: "))  
print("_"*50)
# Cálculo da quantidade total em litros  
litros_latas = latas * 0.35  # 350 ml = 0.35 litros  
litros_garrafas_600ml = garrafas_600ml * 0.6  # 600 ml = 0.6 litros  
litros_garrafas_2l = garrafas_2l  # 2 litros já está em litros  

# Soma total de litros  
total_litros = litros_latas + litros_garrafas_600ml + litros_garrafas_2l  
print("_"*50)
# Saída do resultado  
print("Total de refrigerante comprado:", round(total_litros, 2), "litros")
print("_"*50)