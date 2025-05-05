print(" Seja Bem-vindo!")
print("-"*50)
quantidade_sanduiches = int(input(" Digite a quantidades de sanduiche que deseja: "))
peso_queijo = 50 * 2
peso_pesunto = 50* 1
peso_hamburguer = 100 * 1
#
total_quiejo = peso_queijo * quantidade_sanduiches
total_presuntos = peso_pesunto * quantidade_sanduiches
total_hamburguer = peso_hamburguer * quantidade_sanduiches

total_queijo_kg = total_quiejo / 1000
total_presuntos_kg = total_presuntos / 1000
total_hamburguer_kg = total_hamburguer / 1000
#
print("-"*50)
print(f" Para {quantidade_sanduiches} sanduiches, você precisará de: ")
print("-"*40)
print(f"  - {total_queijo_kg:.2f} kg de queijo")
print(f"  - {total_presuntos_kg:.2f} kg de presuntos")
print(f"  - {total_hamburguer_kg:.2f} kg de hamburguer")
print("-"*50)