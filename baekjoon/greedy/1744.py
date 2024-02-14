from collections import deque

n = int(input())
numbers_pos = []
numbers_neg = []
for _ in range(n):
    number = int(input())
    if number > 0:
        numbers_pos.append(number)
    else:
        numbers_neg.append(number)
numbers_neg.sort()
numbers_pos.sort(reverse=True)

result = 0
q = deque(numbers_pos)


def check(q: deque):
    global result
    while q:
        if len(q) >= 2:
            a, b = q.popleft(), q.popleft()
            result += max(a * b, a + b)
        else:
            result += q.popleft()


check(q)
q = deque(numbers_neg)
check(q)

print(result)
