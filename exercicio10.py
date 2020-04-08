#10) Faça um programa que leia a quantidade de dias, horas, minutos e segundos. Calcule o total em segundos.

dias, horas, minutos, segundos = input("Digite em apenas numeros, separados por espaços, uma quantidade de dias, horas, minutos e segundos para serem convertidas para segundos: ").split()

dias = int(dias)
horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)

dias_segundos = dias * 86400
horas_segundos = horas * 3600
minutos_segundos = minutos * 60

total_segundos = dias_segundos + horas_segundos + minutos_segundos + segundos


print(f"O total em segundos é: {total_segundos}")

