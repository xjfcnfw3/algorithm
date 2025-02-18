import sys
from itertools import combinations
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def get_number(li, num):
    return bisect_right(li, num) - bisect_left(li, num)


n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = arr[:n // 2]
right = arr[n // 2:]
left_sum, right_sum = [], []

for i in range(1, len(left) + 1):
    for c in combinations(left, i):
        left_sum.append(sum(c))
for i in range(1, len(right) + 1):
    for c in combinations(right, i):
        right_sum.append(sum(c))
left_sum.sort()
right_sum.sort()
answer = 0

for num in left_sum:
    v = s - num
    answer += get_number(right_sum, v)

answer += get_number(right_sum, s)
answer += get_number(left_sum, s)

print(answer)
