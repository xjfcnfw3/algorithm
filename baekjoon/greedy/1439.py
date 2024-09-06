arr = list(map(int, list(input())))

result = [0, 0]
temp = arr[0]
for i in range(1, len(arr)):
    if temp != arr[i]:
        result[temp] += 1
        temp = arr[i]
result[temp] += 1
print(min(result))
