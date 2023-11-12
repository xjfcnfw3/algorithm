T = int(input())

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global result, n
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)

for test_case in range(1, T + 1):
    n = int(input())
    result = 0
    row = [0] * n
    n_queens(0)
    print("#{} {}".format(test_case, result))