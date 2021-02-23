import sys
def equal_or_smaller_than_M(X, n, M):
    X_reversed = reversed(X)
    base = 1
    num = 0
    for x in X_reversed:
        num += x * base
        base *= n
    return num <= M

#X = map(int, list(input()))
X = [int(n) for n in list(input())]
M = int(input())
d = max(X)
if len(X) == 1:
    print(0 if X[0] > M else 1)
    sys.exit()

l = d
r = M + 1

while l + 1 < r:
    m = (l + r) // 2
    if equal_or_smaller_than_M(X, m, M):
        l = m
    else:
        r = m
print(l - (d + 1) + 1)
