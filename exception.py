#erros em tempo de execução -> Exceções
def fsimples(n):
    a = 1/n

def outrafuncao(n):
    fsimples(n)
numero = int(input())
#try/except/finally
try:
    outrafuncao(numero)
    print("Tudo certo.")
except ZeroDivisionError:
    print("Não é permitida a divisão por zero.")
    print(sys.exc_info())
except ValueError:
    print("Use apenas numeros")
    print(sys.exc_info())
finally:
    print("Sempre apareço")
