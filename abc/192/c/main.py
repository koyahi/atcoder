def g1(x):
    x_list = list(str(x))
    x_list.sort(reverse=True)
    ret = int("".join(x_list))
    return ret

def g2(x):
    x_list = list(str(x))
    x_list.sort()
    ret = int("".join(x_list))
    return ret

def f(x):
    return g1(x) - g2(x)

N, K = map(int, input().split())
a = N

for i in range(K):
    a = f(a)

print(a)
