N, K = map(int, input().split())
available = 0
h = list(map(int, input().split()))
for i in range(N):
    available += 1 if h[i] >= K else 0
print(available)
