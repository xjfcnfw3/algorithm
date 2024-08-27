s = int(input())
total = 0
result = 0

while total <= s:
    result += 1
    total += result
print(result - 1)