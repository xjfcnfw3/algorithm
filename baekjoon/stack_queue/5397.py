for _ in range(int(input())):
    arr = list(input())
    left_stk, right_stk = [], []
    for c in arr:
        if c == "<":
            if left_stk:
                right_stk.append(left_stk.pop())
        elif c == ">":
            if right_stk:
                left_stk.append(right_stk.pop())
        elif c == "-":
            if left_stk:
                left_stk.pop()
        else:
            left_stk.append(c)
    while right_stk:
        left_stk.append(right_stk.pop())
    print("".join(left_stk))