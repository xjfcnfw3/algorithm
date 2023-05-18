import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())

sets = [i for i in range(n + 1)]

def find(num):
    if sets[num] != num:
        sets[num] = find(sets[num])
    return sets[num]

for _ in range(m):
    commend, a, b = map(int, input().split())
    root_a = find(a)
    root_b = find(b)
    if commend == 0:
        if root_a < root_a:
            sets[root_b] = root_a
        else:
            sets[root_a] = root_b
    else:
        if sets[root_a] == sets[root_b]:
            print("YES")
        else:
            print("NO")