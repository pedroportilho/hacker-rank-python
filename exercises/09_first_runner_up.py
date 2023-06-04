# recebe um array e o numero de elementos dele,
# deve imprimir o segundo maior valor do array

n = int(input())
arr = map(int, input().split())
sortedList = sorted(list(arr), reverse=True)
runnerUp = 0

for i in sortedList:
    if i != sortedList[0]:
        runnerUp = i
        break

print(runnerUp)
