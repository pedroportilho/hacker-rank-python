# recebe um numero inteiro e positivo e retorna uma
# string com os valores entre 1
# e o próprio numero

n = int(input())

for i in range(1, n+1, 1):
    print(i, end='')
