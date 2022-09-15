n, k = map(int, input().split())
num = [i for i in range(1, n+1)]

index = 0
result = []

for i in range(n):
    index += k-1
    if index >= len(num):
        index = index%len(num)
    result.append(str(num.pop(index)))

print("<", ", ".join(result), ">", sep="")