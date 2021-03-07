N, K = map(int, input().split())
A = sorted([int(i) for i in input().split()])
print(sum(A[:K]))
