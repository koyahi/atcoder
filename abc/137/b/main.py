K, X = map(int, input().split())
for i in range(X - (K - 1), X + K):
    print(i, end="\n" if i == X + K - 1 else " ")
