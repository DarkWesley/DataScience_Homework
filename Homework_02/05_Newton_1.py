def sqrt_newton(c):
    print("c =",c)
    g = c/2
    i = 0
    while (abs(g*g - c) > 1e-10):
        g = (g + c/g)/2
        i += 1
        print("{}:{:.13f}".format(i,g))
    #print("根号{}的值是:{:.13f}".format(c,g))
sqrt_newton(2)
sqrt_newton(2000)
sqrt_newton(200000)