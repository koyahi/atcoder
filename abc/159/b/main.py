S = input()
S1 = S[:len(S)//2]
S2 = S[-1:(len(S) - 1)//2:-1]
S11 = S1[:len(S1)//2]
S12 = S1[-1:(len(S1) - 1)//2:-1]
S21 = S2[:len(S2)//2]
S22 = S2[-1:(len(S2) - 1)//2:-1]
print("Yes" if S1 == S2 and S11 == S12 and S21 == S22 else "No")
