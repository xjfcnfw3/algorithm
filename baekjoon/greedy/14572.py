import heapq
import sys
input = sys.stdin.readline
n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
q = []

for dead_line, value in arr:
    heapq.heappush(q, value)
    if dead_line < len(q):
        heapq.heappop(q)
print(sum(q))