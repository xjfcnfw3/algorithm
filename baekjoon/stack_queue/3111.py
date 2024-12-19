import sys
input = sys.stdin.readline

a = input().rstrip()
t = list(input().rstrip())
a_reverse = a[::-1]
left, right = 0, len(t) - 1
left_stk = []
right_stk = []

while left <= right:
    while left <= right:
        left_stk.append(t[left])
        left += 1
        if len(left_stk) >= len(a) and ''.join(left_stk[-len(a):]) == a:
            del left_stk[-len(a):]
            break
    while left <= right:
        right_stk.append(t[right])
        right -= 1
        if len(right_stk) >= len(a) and ''.join(right_stk[-len(a):]) == a_reverse:
            del right_stk[-len(a):]
            break
stk_merged = left_stk + right_stk[::-1]
stk = []
for char in stk_merged:
    stk.append(char)
    if char == a[-1] and ''.join(stk[-len(a):]) == a:
        del stk[-len(a):]

print("".join(stk))