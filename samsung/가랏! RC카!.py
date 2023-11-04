T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    result = 0
    speed = 0
    for _ in range(n):
        command = input()
        if command[0] != "0":
            c, v = map(int, command.split())
            if c == 1:
                speed += v
            else:
                speed -= v
                if speed < 0:
                    speed = 0
        result += speed
    print("#{} {}".format(test_case, result))
