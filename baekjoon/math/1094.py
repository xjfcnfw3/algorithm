n = int(input())

result = 0

while n > 1:
    if n % 2 == 1:
        result += 1
    n //= 2

if n:
    result += 1

print(result)