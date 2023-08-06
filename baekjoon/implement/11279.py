import heapq
import sys

input = sys.stdin.readline
n = int(input())

q = []

for _ in range(n):
    num = int(input())

    if num > 0:
        heapq.heappush(q, -num)
    else:
        if q:
            v = heapq.heappop(q)
            print(-v)
        else:
            print(0)