import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    current = arr.pop()
    while arr:
        num = arr.pop()
        if current > num:
            answer += current - num
        else:
            current = num
    print(answer)