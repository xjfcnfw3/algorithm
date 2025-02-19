import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

pizzaA = [int(input()) for _ in range(a)]
pizzaB = [int(input()) for _ in range(b)]

def getPizzaSum(pizza):
    dic = defaultdict(int)

    for i in range(len(pizza)):
        temp = pizza[i]
        dic[temp] += 1
        for j in range(1, len(pizza) - 1):
            temp += pizza[(i + j) % len(pizza)]
            dic[temp] += 1
    dic[0] += 1
    dic[sum(pizza)] += 1
    return dic

sumA = getPizzaSum(pizzaA)
sumB = getPizzaSum(pizzaB)
answer = 0
for i in range(n + 1):
    answer += sumA[i] * sumB[n - i]

print(answer)