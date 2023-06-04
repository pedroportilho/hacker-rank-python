# Recebe uma lista de alunos e todas suas notas
# retorna a media de notar de um aluno pesquisado

n = int(input())

student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

average = 0

for i in student_marks[query_name]:
    average += i

average /= 3

print("%.2f" % average)
