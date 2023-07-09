a, b, c = map(int, input().split())


def multiply(n):
    if n == 1:
        return a % c
    num = multiply(n//2)

    if n % 2 == 0:
        return (num * num) % c
    else:
        return (num * num * a) % c

print(multiply(b))