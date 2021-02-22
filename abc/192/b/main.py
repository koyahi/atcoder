S = list(input())
unreadable = True
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            unreadable = False
            break
    else:
        if S[i] in "abcdefghijklmnopqrstuvwxyz":
            unreadable = False
            break
print("Yes" if unreadable else "No")
