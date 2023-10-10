def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element

arr = [5, 2, 9, 3, 6]
insertion_sort(arr)
print(arr)
