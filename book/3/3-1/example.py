money = input()
money = int(money)
num = 0
coins = [500, 100, 50, 10]

for coin in coins:
    num += money // coin
    money %= coin

print(num)