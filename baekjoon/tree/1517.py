import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

d = {}

for i in range(len(arr)):
    if arr[i] not in d:
        d[arr[i]] = deque()
    d[arr[i]].append(i)


def build(n):
    p = 0
    m = 0
    while m < n:
        m = 2 ** p
        p += 1
    tree = [0] * (m * 2)
    return tree, m


tree, leaf = build(n)


def get_sum(tree, a, b, leaf):
    result = 0
    start = leaf + a - 1
    end = leaf + b - 1
    while start < end:
        if start % 2:
            result += tree[start]
        start = (start + 1) // 2
        if not end % 2:
            result += tree[end]
        end = (end - 1) // 2
    if start == end:
        result += tree[end]
    return result


def update(tree, a, leaf):
    idx = leaf + a - 1
    tree[idx] = 1
    idx //= 2
    while idx:
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        idx //= 2
    return tree


arr = sorted(arr)
result = 0
for i in range(n):
    idx = d[arr[i]].popleft()
    result += get_sum(tree, idx, n - 1, leaf)
    update(tree, idx, leaf)

print(result)
