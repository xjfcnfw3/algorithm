n = int(input())

result = 1
current = 1
point = 1

while current < n:
    point += 1
    current += 6 * point - 6
    result += 1

print(result)

