n = int(input())
commands = []

for _ in range(n):
  c = input().split()
  commands.append(c)

list = []

for com in commands:
  match com[0]:
    case "insert":
        list.insert(int(com[1]), int(com[2]))
    case "print":
        print(list)
    case "remove":
        list.remove(int(com[1]))
    case "append":
        list.append(int(com[1]))
    case "sort":
        list.sort()
    case "pop":
        list.pop()
    case "reverse":
        list.reverse()
