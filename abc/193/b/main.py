N = int(input())
minv = 10**10
for i in range(N):
    A, P, X = map(int, input().split())
    if A < X:
        minv = min(minv, P)
print(-1 if minv == 10**10 else minv)
