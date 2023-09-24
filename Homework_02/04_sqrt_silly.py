n = 2
def sqrt_silly(c):
    g = 0
    i = 0
    for j in range(0,c+1):
        if(j*j>c and g == 0):
            g = j - 1
            break
    while(abs(g*g - c)>0.0001):
        g+=0.00001
        #i+=1
    print("根号2的值是:{:.5f}".format(g))
sqrt_silly(n)