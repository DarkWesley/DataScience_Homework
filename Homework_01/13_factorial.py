n = int(input("请输入一个整数："))
i = n
ans = 1
while i > 0:
    ans *= i
    i-=1
print(ans)