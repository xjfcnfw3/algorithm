for _ in range(int(input())):
    st = input().rstrip()
    left, right = 0, len(st) - 1
    result = 0
    while left < right:
        if st[left] == st[right]:
            left += 1
            right -= 1
            continue
        if st[left] == st[right - 1]:
            temp = st[left: right]
            if st[left: right] == temp[::-1]:
                result = 1
                break

        if st[left + 1] == st[right]:
            temp = st[left + 1: right + 1]
            if st[left + 1: right + 1] == temp[::-1]:
                result = 1
                break

        result = 2
        break
    print(result)
