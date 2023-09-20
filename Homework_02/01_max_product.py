n = int(input("请输入一个正整数："))
rmd = n % 3
threes = 0
twos = 0
if n > 2:
    if rmd == 0:
        threes = n // 3
    elif rmd == 1:
        threes = (n // 3) - 1
        twos = 2
    elif rmd == 2:
        threes = n // 3
        twos = 1
    print("所求正整数列表由{}个2和{}个3组成".format(twos,threes))
else:
    print("1无法拆解，所求正整数列表即为1")