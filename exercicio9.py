#9) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o
#valor do salário e a porcentagem de aumento. Mostre o valor do aumento e do
#novo salário.

salario_inicial = float(input("Digite o valor do salario do fuincionario: "))
porcentagem_aumento = float(input("Digite somento o valor da porcentagem que deve ser aumentado no salario: "))

valor_aumento = salario_inicial * (porcentagem_aumento / 100)
salario_atualizado = salario_inicial + valor_aumento

print(f"O valor do aumento foi: {valor_aumento}")
print(f"O novo salario do funcionario é: {salario_atualizado}")