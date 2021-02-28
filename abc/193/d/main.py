import copy
def get_point(S):
    ret = 0
    for i in range(1, 10):
        ret += i * 10 ** S.count(str(i))
    return ret

K = int(input())
S = input()
T = input()
remain_list = [K - S.count(str(i)) - T.count(str(i)) for i in range(1, 10)]
remain = 9 * K - 8
ans_deno = remain * (remain - 1)
ans_nume = 0

for s in range(1, 10):
    rl = copy.copy(remain_list)
    if rl[s-1] == 0:
        continue
    rl[s-1] -= 1
    S = S[:4] + str(s)
    point_s = get_point(S)
    for t in range(1, 10):
        if rl[t-1] == 0:
            continue
        T = T[:4] + str(t)
        point_t = get_point(T)
        if point_s > point_t:
            ans_nume += (rl[s-1] + 1) * rl[t-1]

print(ans_nume / ans_deno)
