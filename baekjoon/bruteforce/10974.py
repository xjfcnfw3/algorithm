from itertools import permutations
n = int(input())
arr = list(map(int, input().split()))
result = permutations(arr, n)
max_d = 0
for i in result:
    sum_c = 0
    for j in range(len(i)-1):
        sum_c += abs(i[j]-i[j+1])
    if sum_c > max_d:
        max_d = sum_c

print(max_d)