s = input("Nhập chuỗi: ")

# Cách 1: Slicing
print("Đảo ngược (slicing):", s[::-1])

# Cách 2: Không dùng slicing
reversed_s = ""
for ch in s:
    reversed_s = ch + reversed_s
print("Đảo ngược (không slicing):", reversed_s)