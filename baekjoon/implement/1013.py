import re
reg = re.compile("^(100+1+|01)+$")
for _ in range(int(input())):
    arr = input()
    result = reg.match(arr)
    if result:
        print("YES")
        continue
    print("NO")
