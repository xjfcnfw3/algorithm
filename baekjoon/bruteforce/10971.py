from itertools import permutations
n = int(input())
arr = []
for i in range(n):
    arr_s = list(map(int, input().split()))
    arr.append(arr_s)

result = permutations(list(range(n)), n)
min_d = 99999999999
for path in result:
    distance = 0
    for i in range(0, len(list(path))-1):
        distance += arr[path[i]][path[i+1]]
    distance += arr[path[n-1]][path[0]]
    if min_d > distance:
        min_d = distance
print(min_d)