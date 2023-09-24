def cbrt_Newton(c):
    print("c =", c)
    g = c/2
    i = 0
    while abs(g**3 - c) > 1e-10:
        g = (2*g+c/(g*g))/3
        i = i + 1
        print("{}:{:.13f}".format(i, g))
cbrt_Newton(10)