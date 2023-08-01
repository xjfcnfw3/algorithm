import heapq
import sys

input = sys.stdin.readline

q = []
n = int(input())

for i in range(n):
    x = int(input())

    if x == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(x), x))