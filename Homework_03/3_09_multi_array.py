def makeB(A):
    n = len(A)
    left_product = [1] * n
    right_product = [1] * n
    result = [0] * n

    left = 1
    for i in range(n):
        left_product[i] = left
        left *= A[i]

    right = 1
    for i in range(n - 1, -1, -1):
        right_product[i] = right
        right *= A[i]

    for i in range(n):
        result[i] = left_product[i] * right_product[i]

    return result

# 示例用法
A = [1, 2, 3, 4]
B = makeB(A)
print(f"数组A：{A}")
print(f"输出数组B:{B}")  # 输出 [24, 12, 8, 6]
