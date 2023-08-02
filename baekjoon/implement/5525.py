import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
s = input()

io = 0
result = 0
i = 0

while i < (m - 1):
    if s[i:i + 3] == "IOI":
        io += 1
        i += 2
        if io == n:
            result += 1
            io -= 1
    else:
        i += 1
        io = 0

print(result)