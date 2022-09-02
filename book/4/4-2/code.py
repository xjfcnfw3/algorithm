n = input()
n = int(n)
num = 0
for i in range(n + 1):
    h = str(i)
    if '3' in h:
        num += 3600
    else:
        for j in range(60):
            m = str(j)
            if '3' in m:
                num += 60
                continue
            else:
                for k in range(60):
                    s = str(k)
                    if '3' in s:
                        num += 1

print(num)
