from collections import defaultdict
import sys

input = sys.stdin.readline
n = int(input())

sum_result = 0
arr = []
numbers = defaultdict(int)

for i in range(n):
    num = int(input())
    arr.append(num)
    sum_result += num

    numbers[num] += 1
arr.sort()

print(round(sum_result / n))
print(arr[n // 2])

max_freq = 0
result = []

for k, v in numbers.items():
    if max_freq < v:
        max_freq = v
        result = [k]
    elif max_freq == v:
        result.append(k)

if len(result) == 1:
    print(result[0])
else:
    print(sorted(result)[1])

print(arr[-1] - arr[0])