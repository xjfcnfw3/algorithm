import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def build(n):
    p = 0
    m = 0
    while m < n:
        m = 2 ** p
        p += 1
    min_tree = [1e9] * (m * 2)
    max_tree = [0] * (m * 2)
    for i in range(n):
        num = int(input())
        min_tree[i + m] = num
        max_tree[i + m] = num
    for i in range(m - 1, 0, -1):
        min_tree[i] = min(min_tree[i * 2], min_tree[i * 2 + 1])
        max_tree[i] = max(max_tree[i * 2], max_tree[i * 2 + 1])
    return min_tree, max_tree, m



min_tree, max_tree, leaf = build(n)

def get_result(a, b, leaf):
    min_result = 1e9
    max_result = 0
    start = leaf + a - 1
    end = leaf + b - 1
    while start < end:
        if start % 2:
            min_result = min(min_tree[start], min_result)
            max_result = max(max_tree[start], max_result)
        start = (start + 1) // 2
        if not end % 2:
            min_result = min(min_tree[end], min_result)
            max_result = max(max_tree[end], max_result)
        end = (end - 1) // 2
    if start == end:
        min_result = min(min_tree[end], min_result)
        max_result = max(max_tree[end], max_result)
    return min_result, max_result

for _ in range(m):
    a, b = map(int, input().split())
    print(*get_result(a, b, leaf))

