# Receba as tres dimensoes de um cuboide, e mostre todas as coordenadas possiveis que
# a soma não seja o valor N

x = int(input())
y = int(input())
z = int(input())
n = int(input())

final = []

for i in range(x+1):
  for j in range(y+1):
    for k in range(z+1):
      if (i + j + k != n):
        final.append([i, j, k])

print(final)