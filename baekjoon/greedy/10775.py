import sys, bisect
input = sys.stdin.readline
g = int(input())
p = int(input())

gate = [i for i in range(1, g + 1)]
result = 0

for i in range(p):
    number = int(input())
    index = bisect.bisect_right(gate, number)
    if index != 0:
        del gate[index - 1]
        result += 1
    else:
        break
print(result)