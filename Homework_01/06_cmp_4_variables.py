w,x,y,z = map(int,input("请输入4个整数：").split())
list = [w,x,y,z]
res = []
while len(list)>0:
    m = max(list)
    list.remove(m)
    res.append(m)
i = 0
while i < 4:
    print(res[i],end=' ')
    i+=1
