import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

max_num = -sys.maxsize
min_num = sys.maxsize

def dfs(depth, current, plus, minus, mul, div):
    global max_num, min_num

    if depth == n:
        max_num = max(current, max_num)
        min_num = min(current, min_num)
        return

    if plus:
        dfs(depth + 1, current + arr[depth], plus - 1, minus, mul, div)
    if minus:
        dfs(depth + 1, current - arr[depth], plus, minus - 1, mul, div)
    if mul:
        dfs(depth + 1, current * arr[depth], plus, minus, mul - 1, div)
    if div:
        dfs(depth + 1, int(current / arr[depth]), plus, minus, mul, div - 1)

dfs(1, arr[0], op[0], op[1], op[2], op[3])
print(max_num)
print(min_num)