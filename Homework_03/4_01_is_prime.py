import math
num = int(input("请输入一个正整数："))
def is_Prime(n):
    flag = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break
    return flag

if is_Prime(num):
    print(f"{num}是一个质数")
else:
    print(f"{num}不是一个质数")