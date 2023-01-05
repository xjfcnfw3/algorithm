money = input()
money = int(money)
num = 0
coins = [500, 100, 50, 10]
i = 0
while money != 0:
    if money < coins[i]:
        i += 1
    else:
        money -= coins[i]
        num += 1
print(num)