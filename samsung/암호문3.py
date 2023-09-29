def make_command(commands):
    temp = []
    result = []
    for c in commands:
        if c in ("I", "D", "A") and temp:
            result.append(temp)
            temp = []
        temp.append(c)
    return result

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    c_n = int(input())
    commands = make_command(list(input().split()))
    index = 0
    for command in commands:
        c = command[0]
        if c == "I":
            x, y, s = int(command[1]), int(command[2]), command[3:]
            arr = arr[:x] + s + arr[x:]
        elif c == "D":
            x, y = int(command[1]), int(command[2])
            arr = arr[:x] + arr[x + y:]
        else:
            x, y, s = int(command[1]), int(command[2]), command[3:]
            arr = arr + s
    print("#{} ".format(test_case), end = "")
    print(*arr[:10])