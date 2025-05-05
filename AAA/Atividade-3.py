# Exibe uma mensagem de boas-vindas para o usuário  
print("Seja Bem-vindo!")  

# Exibe uma linha de separação  
print("-" * 20)  

# Definindo os valores que o trabalhador ganha por hora  
valor_hora_normal = 10.00  # Valor ganho por hora normal  
valor_hora_extra = 15.00    # Valor ganho por hora extra  

# _______________________________________________________________________________________  
# Solicita ao usuário o número de horas normais e horas extras trabalhadas  
horas_normais = float(input("Digite o número de horas normais trabalhadas: "))  # Entrada de horas normais  
horas_extras = float(input("Digite o número de horas extras trabalhadas: "))    # Entrada de horas extras  

# Exibe uma linha de separação  
print("-" * 20)  

# Cálculo do salário bruto  
# O salário bruto é calculado multiplicando as horas normais pelo valor por hora normal  
# e as horas extras pelo valor por hora extra, e somando ambos  
salario_bruto = (horas_normais * valor_hora_normal) + (horas_extras * valor_hora_extra)  

# Cálculo do desconto de impostos  
# Desconto de 10% sobre o salário bruto  
desconto_impostos = salario_bruto * 0.10  

# Cálculo do salário líquido  
# O salário líquido é o salário bruto menos o desconto de impostos  
salario_liquido = salario_bruto - desconto_impostos  

# Exibe o salário bruto formatado com duas casas decimais  
print(f"\nSalário Bruto: R${salario_bruto:.2f}")  

# Exibe o salário líquido formatado com duas casas decimais  
print(f"Salário Líquido: R${salario_liquido:.2f}")  