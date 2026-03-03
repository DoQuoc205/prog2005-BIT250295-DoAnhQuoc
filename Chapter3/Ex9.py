nums = list(map(int, input("Nhập danh sách số: ").split()))
odds = [num for num in nums if num % 2 != 0]
print("Các số lẻ:", odds)