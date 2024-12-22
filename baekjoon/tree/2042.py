import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())


def build(n):
    k = 0
    m = 0
    while n > m:
        m = 2 ** k
        k += 1
    tree = [0] * (m * 2)
    for i in range(n):
        tree[i + m] = int(input())
    for i in range(m - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]
    return tree, m


tree, leaf = build(n)


def change(tree, b, c, leaf):
    idx = leaf + b - 1
    cnt = c - tree[idx]
    while idx:
        tree[idx] += cnt
        idx //= 2
    return tree


def get_sum(tree, b, c, leaf):
    total = []
    start = leaf + b - 1
    end = leaf + c - 1
    while start < end:
        if start % 2:
            total.append(tree[start])
        start = (start + 1) // 2
        if not end % 2:
            total.append(tree[end])
        end = (end - 1) // 2
    if start == end:
        total.append(tree[end])
    return sum(total)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        tree = change(tree, b, c, leaf)
    else:
        answer = get_sum(tree, b, c, leaf)
        print(answer)
