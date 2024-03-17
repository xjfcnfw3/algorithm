s = input()
stk = []
answer = 0
current = 1
depths = [0] * (len(s) + 1)
if len(s) == 1:
    print(0)
    exit(0)
for i in range(len(s)):
    if s[i] == '(' or s[i] == '[':
        stk.append(s[i])
    elif s[i] == ')':
        if not stk or stk[-1] != '(':
            print(0)
            exit(0)
        else:
            if depths[len(stk) + 1] == 0:
                depths[len(stk)] += 2
            else:
                depths[len(stk)] += depths[len(stk) + 1] * 2
                depths[len(stk) + 1] = 0
            stk.pop()
    else:
        if not stk or stk[-1] != '[':
            print(0)
            exit(0)
        else:
            if depths[len(stk) + 1] == 0:
                depths[len(stk)] += 3
            else:
                depths[len(stk)] += depths[len(stk) + 1] * 3
                depths[len(stk) + 1] = 0
            stk.pop()
print(depths[1])