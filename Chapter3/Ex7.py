def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nums = list(map(int, input("Nhập danh sách số: ").split()))
x = int(input("Nhập số cần tìm: "))
index = linear_search(nums, x)
print("Chỉ số của", x, "là:", index if index != -1 else "Không tìm thấy")