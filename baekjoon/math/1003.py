n = int(input())

def fibo(n):
    one, zero = [0, 1, 1], [1, 0, 1]

    if n >= 3:
        for i in range(2, n):
            zero.append(zero[i - 1] + zero[i])
            one.append(one[i - 1] + one[i])

    print(zero[n], one[n])

for _ in range(n):
    num = int(input())
    fibo(num)