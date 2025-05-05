  # Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit.  
# Este algoritmo lê uma temperatura em Celsius e a converte para Fahrenheit.  

# Exibe uma mensagem de boas-vindas ao usuário  
print("Olá Seja Bem-vindo(a)!🤗 ")  

# Exibe uma linha de separação  
print("-" * 50)  

# Solicita ao usuário que insira a temperatura em Celsius  
# A entrada é convertida para um número de ponto flutuante (float)  
tc = float(input("Temperatura em Celsius: "))  

# Cálculo da temperatura em Fahrenheit  
# Fórmula de conversão: (°C * 9/5) + 32  
# Aqui utilizamos a fórmula para converter a temperatura de Celsius para Fahrenheit  
# O resultado é impresso com duas casas decimais  
print("Temperatura em Fahrenheit: %.2f" % (9 * tc / 5 + 32)) 
print("-" * 50)  