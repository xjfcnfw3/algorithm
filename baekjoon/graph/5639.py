import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
tree = []


while True:
    try:
        tree.append(int(input()))
    except:
        break

def search(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if tree[i] > tree[start]:
            mid = i
            break
    search(start + 1, mid - 1)
    search(mid, end)
    print(tree[start])

search(0, len(tree)-1)