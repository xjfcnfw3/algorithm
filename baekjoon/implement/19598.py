import heapq

n = int(input())

q = [0]

time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x : (x[0], x[1]))

for start, end in time:
    if start >= q[0]:
        heapq.heappushpop(q, end)
    else:
        heapq.heappush(q, end)
print(len(q))