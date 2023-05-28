import sys

input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    num = int(input())
    if num == 0 and stack:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))