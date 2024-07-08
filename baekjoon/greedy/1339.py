from collections import defaultdict
n = int(input())

arr = [input() for _ in range(n)]

alpha = defaultdict(int)

for st in arr:
    for i in range(len(st)):
        alpha[st[i]] += 10**(len(st) - i)

result = sorted(alpha.items(), key= lambda x:x[1], reverse=True)
alpha_num = {}
number = 9

for i in range(len(result)):
    alpha_num[result[i][0]] = str(number)
    number -= 1

sum_result = 0

for st in arr:
    temp = ""
    for i in range(len(st)):
        temp += alpha_num[st[i]]
    sum_result += int(temp)
print(sum_result)