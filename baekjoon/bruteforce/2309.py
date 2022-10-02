import itertools
arr = []
for i in range(9):
    arr.append(int(input()))

results = itertools.combinations(arr, 7)
result = []
for i in results:
    if sum(i) == 100:
        result = i
        break
result = list(result)
result = sorted(result)
print(*result, sep='\n')