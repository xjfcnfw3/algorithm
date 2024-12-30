n = int(input())
stk = []
result = 0
temp = 0
cnt = [0] * n

s = input()
ans = 0
for i in range(n):
    if s[i] == "(":
        stk.append(i)
    if s[i] == ")":
        if stk:
            cnt[i] = 1
            cnt[stk[-1]] = 1
            stk.pop()
for c in cnt:
    if c == 1:
        ans += 1
        result = max(result, ans)
    else:
        ans = 0
print(result)