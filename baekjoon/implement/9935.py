import sys

input = sys.stdin.readline

s = input().rstrip()
b = input().rstrip()

ex_size = len(b)
stack = []

for i in range(len(s)):
    stack.append(s[i])
    if "".join(stack[-ex_size:]) == b:
        for _ in range(ex_size):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")