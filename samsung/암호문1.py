
def process_command(st, command):
    command = command.split("I")[1:]
    for c in command:
        arr = list(map(int, c.split()))
        x, y, s = arr[0], arr[1], arr[2:]
        st = st[:x] + s + st[x:]
    return st[:10]

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    st = list(map(int, input().split()))
    command_num = int(input())
    command = input()
    result = process_command(st, command)
    print("#" + str(test_case) + " ", end = "")
    print(*result)