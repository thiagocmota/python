#4) Leia 2 valores de ponto flutuante A e B, que correspondem a 2 notas de um
#aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e
#a nota B tem peso 7.5.

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a seungda nota do aluno: "))

media = ((nota1 * 3.5) + (nota2 * 7.5)) / 10

print(f"A media do aluno foi: {media}")