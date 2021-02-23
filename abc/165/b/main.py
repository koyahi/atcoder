import math
X = int(input())
year = 0
cur = 100
while cur < X:
    cur = (cur * 101) // 100
    year += 1
print(year)
