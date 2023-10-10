import random

list1 = [random.randint(0, 100) for i in range(10)]
list2 = [random.randint(0, 100) for i in range(100)]
list3 = [random.randint(0, 100) for i in range(1000)]
cnt = 0
#选择排序
def select_sort(list):
    temp_list = list.copy()
    global cnt
    cnt = 0
    for i in range(len(temp_list) - 1):
        min_index = i
        for j in range(i + 1, len(temp_list)):
            cnt += 1
            if temp_list[j] < temp_list[min_index]:
                min_index = j
        temp_list[i], temp_list[min_index] = temp_list[min_index], temp_list[i]
    return temp_list

#归并排序
def merge(left, right):
    global cnt
    left_index = 0
    right_index = 0
    temp_list = []
    while left_index < len(left) and right_index < len(right):
        cnt += 1
        if left[left_index] < right[right_index]:
            temp_list.append(left[left_index])
            left_index += 1
        else:
            temp_list.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        cnt +=1
        temp_list.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        cnt += 1
        temp_list.append(right[right_index])
        right_index += 1
    return temp_list
def merge_sort(list):
    temp_list = list.copy()
    global cnt
    cnt += 1
    if len(temp_list) <= 1:
        return temp_list
    mid = len(temp_list) // 2
    left = merge_sort(temp_list[:mid])
    right = merge_sort(temp_list[mid:])
    return merge(left, right)

print(f"选择排序1：{select_sort(list1)}，次数：{cnt}")
cnt = 0
print(f"选择排序2：{select_sort(list2)}，次数：{cnt}")
cnt = 0
#print(f"选择排序3：{select_sort(list3)}，次数：{cnt}")
#cnt = 0
print(f"归并排序1：{merge_sort(list1)}，次数：{cnt}")
cnt = 0
print(f"归并排序2：{merge_sort(list2)}，次数：{cnt}")
cnt = 0
#print(f"归并排序3：{merge_sort(list3)}，次数：{cnt}")