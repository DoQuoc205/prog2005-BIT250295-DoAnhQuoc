nums = list(map(int, input("Nhập danh sách số: ").split()))
found = None
for num in nums:
    if num > 10:
        found = num
        break
print("Số đầu tiên > 10:", found if found else "Không có")