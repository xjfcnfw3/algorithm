n = int(input())

arr = list(map(int, input().split()))
arr.sort()

if sum(arr) != n * (n - 1) // 2:
    print(-1)
    exit(0)

point = 0
for i in range(n):
    point += arr[i]
    if point < i * (i + 1) // 2:
        print(-1)
        exit(0)

print(1)