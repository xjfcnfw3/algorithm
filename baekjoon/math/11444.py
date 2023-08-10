import sys
input = sys.stdin.readline

rest = 1000000007
adj = [[1, 1], [1, 0]]

mat = [[1], [1]]

n = int(input())

def power(adj, n):
    if n == 1:
        return adj
    elif n % 2:
        return multi(power(adj, n - 1), adj)
    else:
        return power(multi(adj, adj), n // 2)

def multi(a, b):
    temp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len((b[0]))):
            s = 0
            for k in range(2):
                s += a[i][k] * b[k][j]
            temp[i][j] = s % rest
    return temp

if n < 3:
    print(1)
else:
    print(multi(power(adj, n - 2), mat)[0][0])