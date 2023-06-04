# Recebe uma quantidade de numeros, e seus valores
# retorna uma hash da tupla desses valores

n = int(input())
entrada = input()

t = tuple(int(item) for item in entrada.split())

print(hash(t))
