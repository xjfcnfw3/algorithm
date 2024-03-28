n = int(input())

arr = list(map(int, input().split()))

left_sum = [0] * n
left_sum[0] = arr[0]
right_sum = [0] * n
right_sum[-1] = arr[-1]

for i in range(1, n):
    left_sum[i] = left_sum[i - 1] + arr[i]
    right_sum[- i - 1] = right_sum[-i] + arr[-i - 1]

result = 0

for i in range(1, n - 1):
    temp = left_sum[-1] - arr[0] + left_sum[-1] - left_sum[i] - arr[i]
    result = max(result, temp)
    temp = right_sum[0] - arr[-1] + right_sum[0] - right_sum[i] - arr[i]
    result = max(result, temp)
    temp = left_sum[i] - arr[0] + right_sum[i] - arr[-1]
    result = max(result, temp)
print(result)