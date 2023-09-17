S = input("请输入字符串：")
l1 = []
res = 0
for it in S:
    if len(l1)>0:
        if it == l1[-1]:
            res = 1
            break
        l1.append(it)
if res == 0:
    print("该字符串不包含两个或两个以上的连续相同字符")
else:
    print("该字符串包含两个或两个以上的连续相同字符")