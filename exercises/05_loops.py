#Recebe um valor inteiro positivo e retorna uma lista com os valores ao quadrado de cada
# numero positivo (e zero) menores que o valor recebido

n = int(input())

numbers = range(n)

for num in numbers:
  print(num ** 2)