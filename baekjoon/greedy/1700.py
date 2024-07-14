import heapq

n, k = map(int, input().split())
arr = list(map(int, input().split()))
plug = set()
result = 0
for i in range(k):
    if arr[i] in plug:
        continue
    if len(plug) < n:
        plug.add(arr[i])
        continue
    result += 1
    q = []
    for key in plug:
        if key in arr[i + 1:]:
            heapq.heappush(q, (-(arr[i + 1:].index(key) + i), key))
        else:

            heapq.heappush(q, (-k, key))
    index, value = heapq.heappop(q)
    plug.remove(value)
    plug.add(arr[i])
print(result)

