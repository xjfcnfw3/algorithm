s = input()
t = input()

flag = False

while len(s) <= len(t):
    if s != t:
        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1]
            t = t[::-1]
    else:
        flag = True
        break
if flag:
    print(1)
else:
    print(0)