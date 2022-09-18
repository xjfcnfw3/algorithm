result = [0, 1, 2, 4]
a = int(input())
m = 0
num = []
for i in range(a):
    b = int(input())
    num.append(b)
    if b > m:
        m = b

for i in range(4, m+1):
    d = ((result[i-1]+result[i-2]+result[i-3]))%1000000009
    result.append(d)

for i in num:
    print(result[i])
