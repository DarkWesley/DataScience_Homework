import time
start_time = time.time()

#任意一个程序
for i in range(0,1000):
    print(i, end=" ")
print()
end_time = time.time()
print(f"运行时间为{end_time - start_time}秒")