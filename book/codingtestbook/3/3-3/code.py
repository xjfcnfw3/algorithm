n, m = input().split()
n = int(n)
m = int(m)
result = 0
for i in range(n):
    arr = map(int, input().split())
    num = min(arr)
    result = max(result, num)
print(result)