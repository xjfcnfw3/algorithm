import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

sum_list = [0] * n
rest_list = [0] * m
temp = 0
for i in range(n):
    temp += arr[i]
    sum_list[i] = temp
    rest_list[temp % m] += 1
    if sum_list[i] % m == 0:
        answer += 1
for i in rest_list:
    answer += i * (i - 1) // 2
print(answer)