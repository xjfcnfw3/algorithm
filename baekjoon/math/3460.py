t = int(input())
for i in range(t):
    n = list(reversed(str(bin(int(input())))))
    for i in range(len(n)):
        if n[i] == '1':
            print(i, end=" ")