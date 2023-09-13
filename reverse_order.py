#L = [1,2,3,4,5]
res = []
a = len(L)
#for循环方法
for i in range(0,a):
    res.append(L[-1-i])
#while循环方法
b = 0
while b < a:
    res.append(L[-1-b])
    b += 1

print(res)