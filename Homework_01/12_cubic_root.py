n = float(input("请输入一个数："))
def cubic_rt(x):
    g = x/2
    i = 0
    while abs(g**3 - x) > 0.00000000001:
        g = (2*g)/3 + x/(3*(g**2))
        i = i + 1
    return g
ans = cubic_rt(n)
print("{:.6f}".format(ans))