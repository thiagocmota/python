#3) Faça um programa que peça 2 números inteiros e 1 número real. Calcule e mostre:
#a) O produto do dobro do primeiro com metade do segundo.
#b) A soma do triplo do primeiro com o terceiro.
#c) O terceiro elevado ao cubo.


n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
n3 = int(input("Agora digite um numero real: "))

resposta_a = (n1 * 2) * (n2 / 2)
resposta_b = (n1 * 3) + n3
resposta_c = n3 ** 3

resposta_a = int(resposta_a)
respota_b = int(resposta_b)
resposta_c = int(resposta_c)

print(f"O produto do dobro do primeiro numero com metade do segundo é: {resposta_a}")
print(f"A soma do triplo do primeiro numero com o terceiro é: {resposta_b}")
print(f"O terceiro numero elevado ao cubo é: {resposta_c}")
