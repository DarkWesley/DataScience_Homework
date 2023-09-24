import random
import math

def get_pi_1():
    #蒙特卡罗法
    cnt_all = 0
    cnt_cir = 0
    times = 10000000
    for i in range(times):
        x = random.random()
        y = random.random()
        if x * x + y*y <= 1:
            cnt_cir += 1
        cnt_all += 1
    pi = 4 * (cnt_cir / cnt_all)
    print("蒙特卡罗法：{:.10f}".format(pi))
    print("循环次数：{}".format(cnt_all))

def get_pi_2():
    #割圆法，次数可自行更改，约12次时已较准确
    times = 14
    n = 6
    a = 1
    i = 0
    for i in range(times):
        n = n*2
        a = math.sqrt(2-2*math.sqrt(1-(a/2)**2))
    pi = n*a/2
    print("割圆法：{:.10f}".format(pi))
    print("循环次数：{}".format(times))

def get_pi_3():
    #贝利－波尔温－普劳夫公式法，执行次数同样可自行改变
    times = 10
    pi = 0
    for k in range(times):
        pi += 1 / pow(16, k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
    print("贝利－波尔温－普劳夫公式法：{:.10f}".format(pi))
    print("循环次数：{}".format(times))

get_pi_1()
get_pi_2()
get_pi_3()