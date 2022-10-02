n = int(input())
arr = list(str(n))
result = 0
m = len(arr)
for i in range(m-1):
    result += 9*(10**i)*(i+1)
result += ((n % 10**m)-10**(m-1)+1)*m
print(result)