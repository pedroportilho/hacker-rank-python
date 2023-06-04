# Recebe um numero inteiro positivo e deve retornar:
#   Weird se for impar
#   Not Weird se estiver entre 1 e 5
#   Weird se estiver entre 6 e 20
#   Not Weird se for maior que 20

n = int(input())

if (n % 2 == 1) or (n >= 6 and n <= 20):
    print('Weird')
else:
    print('Not Weird')
