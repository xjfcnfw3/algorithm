import bisect
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    answer = 0
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))

    for num in a:
        answer += bisect.bisect(b, num - 1)
    print(answer)