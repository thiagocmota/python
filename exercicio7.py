#7) Faça um programa que converta a temperatura digitada em Celsius para Fahrenheit.
#Cálculo para Fahrenheit: F = 9*C/5+32

temperatura_celsius = float(input("Digite a temperatura em celsius que deseja converter para Fahrenheit: "))

temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

print(f"A temperatura convertida é: {temperatura_fahrenheit}")