N = int(input())
L = [int(i) for i in input().split()]
print("Yes" if 2 * max(L) < sum(L) else "No")
