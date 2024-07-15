n = int(input())
arr = []
MAX_NUM = 1000000000
for number in map(int, input().split()):
    s = str(number)
    temp = ''
    for i in range(len(s), 11):
        temp += s[i % len(s)]
    arr.append((int(s + temp), str(number)))
arr.sort(key= lambda x:x[0], reverse=True)
print(int(''.join([row[1] for row in arr])))