import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
result = 0

for num in arr:
    num -= b
    result += 1
    if num <= 0:
        continue
    else:
        if num % c > 0:
            result += num // c + 1
        else:
            result += num // c
print(result)