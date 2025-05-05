# Entrada das informações  
metros_por_blusa = 120  
metros_por_novelo = 125  

# Pergunta ao usuário quantas blusas ele deseja produzir  
quantidade_blusas = int(input("Quantas blusas você deseja produzir? "))  

# Cálculo da quantidade total de metros necessários  
metros_necessarios = metros_por_blusa * quantidade_blusas  

# Cálculo da quantidade de novelos necessários  
novelos_necessarios = metros_necessarios / metros_por_novelo  
novelos_necessarios_arredondados = int(novelos_necessarios) + (1 if novelos_necessarios % 1 > 0 else 0)  

# Saída do resultado  
print("-" * 50)  # Linha de separação  
print(f"Para produzir {quantidade_blusas} blusa(s), você precisará de {novelos_necessarios_arredondados} novelo(s) de lã.")  
print("-" * 50)  # Linha de separação  