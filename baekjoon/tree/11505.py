import sys

input = sys.stdin.readline

DIV = 1000000007

n, m, k = map(int, input().split())


def build(n):
    p = 0
    m = 0
    while n > m:
        m = 2 ** p
        p += 1
    tree = [0] * (m * 2)
    for i in range(n):
        tree[m + i] = int(input())
    for i in range(m - 1, 0, -1):
        tree[i] = tree[i * 2] * tree[i * 2 + 1] % DIV
    return tree, m


tree, leaf = build(n)


def change(tree, b, c, leaf):
    idx = leaf + b - 1
    tree[idx] = c
    idx //= 2
    while idx:
        tree[idx] = tree[idx * 2] * tree[idx * 2 + 1] % DIV
        idx //= 2
    return tree


def get_sum(tree, b, c, leaf):
    total = 1
    start = leaf + b - 1
    end = leaf + c - 1

    while start < end:
        if start % 2:
            total = total * tree[start] % DIV
        start = (start + 1) // 2
        if not end % 2:
            total = total * tree[end] % DIV
        end = (end - 1) // 2
    if start == end:
        total = total * tree[end] % DIV
    return total

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        tree = change(tree, b, c, leaf)
    else:
        print(get_sum(tree, b, c, leaf))
