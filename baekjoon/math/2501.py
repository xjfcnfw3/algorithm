n, k = map(int, input().split())
arr = []
for i in range(1, int(n**(1/2))+1):
    if n % i == 0:
        arr.append(i)

for i in reversed(arr):
    if int(n/i) != i:
        arr.append(int(n/i))

if len(arr) < k:
    print(0)
else:
    print(arr[k-1])