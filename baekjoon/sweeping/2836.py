import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
answer = m

for _ in range(n):
    a, b = map(int, input().split())
    if b < a:
        arr.append((b, a))

arr.sort(key= lambda x : -x[1])
tmp = []
start, end = arr[0]

for i in range(1, len(arr)):
    s, e = arr[i]
    if start <= e:
        start = min(s, start)
    else:
        tmp.append((start, end))
        start, end = s, e
tmp.append((start, end))

for s, e in tmp:
    answer += 2 * (e - s)
print(answer)