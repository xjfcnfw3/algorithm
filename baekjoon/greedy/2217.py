n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()
result = []

for num in arr:
    result.append(num * n)
    n -= 1
print(max(result))