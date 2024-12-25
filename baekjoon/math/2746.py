n, b = input().split()
answer = 0
b = int(b)

for i in range(len(n)):
    if "0" <= n[i] <= "9":
        answer += (b ** (len(n) - 1 - i)) * int(n[i])
    else:
        answer += (b ** (len(n) - 1 - i)) * (ord(n[i]) - ord('A') + 10)
print(answer)