def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1, num2 = int(input("请输入整数num1：")), int(input("请输入整数num2："))
result = gcd(num1, num2)
print(f"最大公约数是：{result}")
