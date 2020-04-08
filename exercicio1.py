#1) Faça um programa que leia dois números e calcule:
#a) A soma.
#b) A subtração.
#c) A multiplicação.
#d) A divisão.
#e) A exponenciação.
#f) O módulo.
#g) O resto.


n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2
menos = n1 - n2
vezes = n1 * n2
dividido = n1 / n2
exponenciação = n1 ** n2
resto = n1 % n2


print(f"O resultado da soma desses números é: {soma}")
print(f"O resultado da subtração desses números é: {menos}")
print(f"O resultado da multiplicação desses números é: {vezes}")
print(f"O resultado da divisão desses números é: {dividido}")
print(f"O resultado da exponenciação desses números é: {exponenciação}")
print(f"O resultado do resto desses números é: {resto}")