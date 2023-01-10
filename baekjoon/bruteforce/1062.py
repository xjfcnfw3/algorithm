from itertools import combinations
import sys

n, k = map(int, input().split())

arr = {'a', 'c', 'i', 't', 'n'}
remain = set(chr(a) for a in range(97, 123)) - arr
answer = 0

data = [sys.stdin.readline().rstrip()[4: -4] for _ in range(n)]


def solution(data, learned):
    cnt = 0
    for word in data:
        can_read = True

        for w in word:
            if learned[ord(w)] == 0:
                can_read = False
                break
        if can_read:
            cnt += 1
    return cnt


if k >= 5:
    learned = [0] * 123
    for i in arr:
        learned[ord(i)] = 1

    for teach in list(combinations(remain, k - 5)):
        for i in teach:
            learned[ord(i)] = 1
        cnt = solution(data, learned)

        answer = max(answer, cnt)

        for t in teach:
            learned[ord(t)] = 0
    print(answer)
else:
    print(0)