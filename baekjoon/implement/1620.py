import sys
from collections import defaultdict

input = sys.stdin.readline
names = defaultdict(int)
numbers = defaultdict(str)

n, m = map(int, input().split())

for i in range(n):
    monster = input().rstrip()
    names[monster] = i + 1
    numbers[i + 1] = monster

for i in range(m):
    question = input().rstrip()

    if question.isnumeric():
        print(numbers[int(question)])
    else:
        print(names[question])