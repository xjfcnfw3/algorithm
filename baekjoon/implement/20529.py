import sys
from collections import defaultdict
from itertools import combinations

input = sys.stdin.readline

n = int(input())


def getDistance(a, b):
    result = 0
    for i in range(4):
        if a[i] != b[i]:
            result += 1
    return result


for _ in range(n):
    num = int(input())
    result = sys.maxsize
    data = defaultdict(int)
    people = input().split()
    complete = False
    for i in people:
        data[i] += 1

        if data[i] >= 3:
            complete = True
            print(0)
            break
    if complete:
        continue
    for x, y, z in combinations(people, 3):
        cnt = getDistance(x, y) + getDistance(y, z) + getDistance(z, x)
        result = min(cnt, result)
    print(result)

