#8) Modificando o exercício anterior, faça um programa que converta a temperatura digitada em Fahrenheit para Celsius.

temperatura_f = float(input("Digite a termperatura em Fahrenheit que deseja converter para celsius: "))

temperatura_c = (temperatura_f - 32) * 5/9

print(f"A temperatura convertida é: {temperatura_c}")