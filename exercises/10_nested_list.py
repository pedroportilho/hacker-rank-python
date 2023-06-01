# Recebe Uma lista de alunos e suas notas
# retorna o(s) aluno(s) que tem a segunda menor nota

n = int(input())
records = []

for _ in range(n):
  name = input()
  score = float(input())
  records.append([name, score])

records.sort(key= lambda x: x[1])
lowestScore = records[0][1]
secondLowest = 10000
students = []

for i in records:
  if lowestScore < i[1] or i[1] == secondLowest:
    students.append(i[0])
    secondLowest = i[1]
    lowestScore = 1000
  elif i[1] != lowestScore:
    break

student.sort()

for student in students:
  print(student)
