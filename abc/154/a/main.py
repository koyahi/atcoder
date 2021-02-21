S, T = input().split()
A, B = map(int, input().split())
U = input()
print("{} {}".format(A - 1, B) if S == U else "{} {}".format(A, B - 1))
