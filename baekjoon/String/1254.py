import sys

st = sys.stdin.readline().strip()

for i in range(len(st)):
    if st[i:] == st[i:][::-1]:
        print(len(st) + i)
        break
