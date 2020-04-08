#5) Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A
#seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B
#tem peso 3 e a nota C tem peso 5.

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

print(f"A media do aluno foi: {media}")

