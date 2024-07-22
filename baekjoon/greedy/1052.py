n, k = map(int, input().split())

number = []
result = []
for i in range(24):
    number.append(2**i)

while n > 0:
    for i in reversed(range(len(number))):
        if number[i] <= n:
            n -= number[i]
            result.append(number[i])

if len(result) <= k:
    print(0)
    exit(0)

rest_number = result[k - 1]

print(rest_number - sum(result[k:]))