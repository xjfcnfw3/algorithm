from sys import stdin
from collections import Counter

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
num = Counter(arr)

result = [-1 for i in range(n)]
stack = [0]

for i in range(n):
    while stack and num[arr[stack[-1]]] < num[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)