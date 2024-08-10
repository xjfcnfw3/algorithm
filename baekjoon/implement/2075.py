import heapq, sys
input = sys.stdin.readline
n = int(input())
q = []

for _ in range(n):
    arr = list(map(int, input().split()))
    for i in range(n):
        if len(q) < n:
            heapq.heappush(q, arr[i])
        else:
            if q[0] < arr[i]:
                heapq.heappushpop(q, arr[i])
print(q[0])