import sys
input = sys.stdin.readline
n, m = map(int, input().split())

roots = [i for i in range(n)]

num = 0


def find(num):
    if num != roots[num]:
        roots[num] = find(roots[num])
    return roots[num]


def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root == b_root:
        return True
    if a_root > b_root:
        roots[a_root] = b_root
    else:
        roots[b_root] = a_root
    return False


for _ in range(m):
    a, b = map(int, input().split())
    num += 1
    result = union(a, b)
    if result:
        print(num)
        exit(0)
print(0)
