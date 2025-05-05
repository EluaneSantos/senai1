# Entrada: ano de nascimento e ano atual
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

# Calcula a idade em anos
idade_anos = ano_atual - ano_nascimento

# Converte para meses, dias e semanas
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365  # Considerando anos não bissextos
idade_semanas = idade_dias // 7

# Exibe os resultados
print("Idade em anos:", idade_anos)
print("Idade em meses:", idade_meses)
print("Idade em dias:", idade_dias)
print("Idade em semanas:", idade_semanas)