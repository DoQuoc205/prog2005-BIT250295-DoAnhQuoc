def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = ["apple", "banana", "cherry", "mango", "orange"]

target = input("Nhập chuỗi cần tìm: ")

pos = binary_search(arr, target)
if pos != -1:
    print(f"Chuỗi '{target}' được tìm thấy tại vị trí {pos}")
else:
    print(f"Chuỗi '{target}' không có trong danh sách")
