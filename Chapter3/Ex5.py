def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

nums = list(map(float, input("Nhập danh sách số thực, cách nhau bởi dấu cách: ").split()))
print("Danh sách sau khi sắp xếp giảm dần:", insertion_sort_desc(nums))