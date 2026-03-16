s = input("nhập chuỗi: ")
upper = sum(1 for c in s if c.upper())
lower = sum(1 for c in s if c.lower())
digit = sum(1 for c in s if c.isdigit())
space = s.count(" ")
special = len(s) - (upper + lower + digit + space)
vowels = "aeiouAEIOU"
nguyen_am = sum(1 for c in s if c in vowels)
phu_am = sum(1 for c in s if c.isalpha() and c not in vowels)

print("In hoa:", upper)
print("In thường:", lower)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)
print("Khoảng trắng:", space)
print("Nguyên âm:", nguyen_am)
print("Phụ âm:", phu_am)


