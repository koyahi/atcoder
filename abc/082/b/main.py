import sys
s = sorted(input())
t = sorted(input())[::-1]

for i in range(min(len(s), len(t))):
    if s[i] != t[i]:
        print("Yes" if s[i] < t[i] else "No")
        sys.exit()
print("Yes" if len(s) < len(t) else "No")
