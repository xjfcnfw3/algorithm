import sys

input = sys.stdin.readline

t = int(input())

def build(n):
    p = 0
    m = 0
    while m < n:
        m = 2 ** p
        p += 1
    tree = [[0, 0] for _ in range(2 * m)]
    for i in range(n):
        tree[m + i][0] = i
        tree[m + i][1] = i
    for i in range(m - 1, 0, -1):
        tree[i][0] = min(tree[i * 2][0], tree[i * 2 + 1][0])
        tree[i][1] = max(tree[i * 2][1], tree[i * 2 + 1][1])
    return tree, m

def update(tree, a, b, leaf):
    idx_a = leaf + a
    idx_b = leaf + b
    temp = tree[idx_b]
    tree[idx_b] = tree[idx_a]
    tree[idx_a] = temp
    idx_a //= 2
    idx_b //= 2
    while idx_a:
        tree[idx_a][0] = min(tree[idx_a * 2][0], tree[idx_a * 2 + 1][0])
        tree[idx_a][1] = max(tree[idx_a * 2][1], tree[idx_a * 2 + 1][1])
        idx_a //= 2
    while idx_b:
        tree[idx_b][0] = min(tree[idx_b * 2][0], tree[idx_b * 2 + 1][0])
        tree[idx_b][1] = max(tree[idx_b * 2][1], tree[idx_b * 2 + 1][1])
        idx_b //= 2

def get_result(tree, a, b, leaf):
    strat = leaf + a
    end = leaf + b
    min_result = 1e9
    max_result = -1

    while strat < end:
        if strat % 2:
            min_result = min(tree[strat][0], min_result)
            max_result = max(tree[strat][1], max_result)
        strat = (strat + 1) // 2
        if not end % 2:
            min_result = min(tree[end][0], min_result)
            max_result = max(tree[end][1], max_result)
        end = (end - 1) // 2
    if strat == end:
        min_result = min(tree[end][0], min_result)
        max_result = max(tree[end][1], max_result)
    return min_result, max_result

for _ in range(t):
    n, k = map(int, input().split())
    tree, leaf = build(n)
    for _ in range(k):
        a, b, c = map(int, input().split())
        if a == 1:
            min_result, max_result = get_result(tree, b, c, leaf)
            if min_result == b and max_result == c:
                print("YES")
            else:
                print("NO")
        else:
            update(tree, b, c, leaf)
