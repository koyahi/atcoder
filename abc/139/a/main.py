S = input()
T = input()
ans = 0
for i in range(len(S)):
    ans += 1 if S[i] == T[i] else 0
print(ans)
