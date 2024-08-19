n = int(input())
arr = [0] + list(map(int, input().split()))

result = [0] * (n + 1)
for i in range(1, n + 1):
    result[arr[i]] = i

max_length = -1
temp = 1
for i in range(1, n):
    if result[i] < result[i + 1]:
        temp += 1

        if temp > max_length:
            max_length = temp
    else:
        temp = 1
print(n - max_length if max_length != -1 else 0)