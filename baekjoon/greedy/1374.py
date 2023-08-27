import heapq
import sys

input = sys.stdin.readline

n = int(input())

q = []
h = []

for _ in range(n):
    num, start, end = map(int, input().split())
    heapq.heappush(q, [start, end, num])

start, end, num = heapq.heappop(q)
heapq.heappush(h, end)

while q:
    start, end, num = heapq.heappop(q)
    if h[0] <= start:
        heapq.heappop(h)
    heapq.heappush(h, end)

print(len(h))