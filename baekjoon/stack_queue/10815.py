import sys
input = sys.stdin.readline
n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
checks = list(map(int, input().split()))

for num in checks:
    left, right = 0, n - 1
    offset = False
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] > num:
            right = mid - 1
        elif cards[mid] < num:
            left = mid + 1
        else:
            offset = True
            break
    print(1 if offset else 0, end = ' ')