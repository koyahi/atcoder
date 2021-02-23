N = int(input())
sum = 0
for i in range(1, N+1):
    sum += 0 if i % 3 == 0 or i % 5 == 0 else i
print(sum)
