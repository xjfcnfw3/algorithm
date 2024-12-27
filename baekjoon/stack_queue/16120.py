p = input()
stk = []

for c in p:
    if stk[-3:] == ["P", "P", "A"] and c == "P":
        for _ in range(3):
            stk.pop()
        stk.append(c)
    else:
        stk.append(c)
if stk == ["P", "P", "A", "P"] or stk == ["P"]:
    print("PPAP")
else:
    print("NP")