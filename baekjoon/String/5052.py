import sys
input = sys.stdin.readline
t = int(input())


def solution():
    n = int(input())
    arr = [input() for _ in range(n)]
    arr.sort()
    for i in range(n - 1):
        if arr[i][:-1] == arr[i + 1][:len(arr[i]) - 1]:
            print("NO")
            return
    print("YES")


for _ in range(t):
    solution()
