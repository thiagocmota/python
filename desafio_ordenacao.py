#receber 3 numeros na mesma linha

numero1, numero2, numero3 = input("Digite 3 numeros inteiros, separados por espaços, para serem organizados em ordem crescente: ").split()

numero1 = int(numero1)
numero2 = int(numero2)
numero3 = int(numero3)

if numero1 < numero2 < numero3:
    print(numero1)
    print(numero2)
    print(numero3)
elif numero1 < numero3 < numero2:
    print(numero1)
    print(numero3)
    print(numero2)
elif numero2 < numero1 < numero3:
    print(numero2)
    print(numero1)
    print(numero3)
elif numero2 < numero3 < numero1:
    print(numero2)
    print(numero3)
    print(numero1)
elif numero3 < numero1 < numero2:
    print(numero3)
    print(numero1)
    print(numero2)
else:
    print(numero3)
    print(numero2)
    print(numero1)