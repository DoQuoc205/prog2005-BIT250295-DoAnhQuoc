n = input("Nhập số nguyên dương 5 chữ số: ")
if len(n) == 5 and n.isdigit():
    lon_nhat = max(int(ch) for ch in n)
    print("Chữ số lớn nhất:", lon_nhat)
else:
    print("Không hợp lệ!")