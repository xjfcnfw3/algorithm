import sys
input = sys.stdin.readline

n = int(input())
plan = [list(map(int, input().split())) for _ in range(n)]
max_price = 0


def dfs(price, day):
    global max_price
    for z in range(day, n):
        if plan[z][0] + z <= n:
            max_price = max(max_price, price + plan[z][1])
            dfs(price + plan[z][1], z + plan[z][0])


for i in range(n):
    dfs(0, i)
print(max_price)