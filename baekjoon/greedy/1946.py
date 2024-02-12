import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()

    result = 1
    max_num = arr[0][1]
    for i in range(1, n):
        if max_num > arr[i][1]:
            result += 1
            max_num = arr[i][1]
    print(result)