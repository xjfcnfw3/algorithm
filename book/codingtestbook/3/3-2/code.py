n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

sum = 0
j = 0
for i in range(m):
   if j == k:
       sum += second
       j=0
   else:
       sum += first
       j +=1

print(sum)