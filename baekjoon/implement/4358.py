import sys
from collections import defaultdict
input = sys.stdin.readline
d = defaultdict(int)
count = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    count += 1
    d[tree] += 1

for k, v in sorted(d.items()):
    print("%s %.4f" %(k, v / count * 100))