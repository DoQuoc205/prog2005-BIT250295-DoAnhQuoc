chuoi = input("Nhập chuỗi các số cách nhau bởi dấu chấm phẩy (;): ")
danh_sach = []
for phan in chuoi.split(';'):
    phan = phan.strip()
    if phan:
        so = int(phan)
        danh_sach.append(so)

print("\nKẾT QUẢ")
print("Các số trong chuỗi:")
for so in danh_sach:
    print(so)
dem_chan = 0
for so in danh_sach:
    if so % 2 == 0:
        dem_chan += 1
dem_am = 0
for so in danh_sach:
    if so < 0:
        dem_am += 1
def la_nguyen_to(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

dem_nguyen_to = 0
for so in danh_sach:
    if la_nguyen_to(so):
        dem_nguyen_to += 1
tong = 0
for so in danh_sach:
    tong += so
trung_binh = tong / len(danh_sach) if danh_sach else 0

print(f"\nSố lượng số chẵn     : {dem_chan}")
print(f"Số lượng số âm       : {dem_am}")
print(f"Số lượng số nguyên tố: {dem_nguyen_to}")
print(f"Giá trị trung bình   : {trung_binh:.2f}")

