strings = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    strings.append(s)

n = len(strings)

print("\nQuá trình sắp xếp:")

for i in range(n - 1):
    for j in range(n - i - 1):
        if len(strings[j]) < len(strings[j + 1]):

            strings[j], strings[j + 1] = strings[j + 1], strings[j]

        print(f"Bước {i}-{j}: {strings}")

print("\nKết quả cuối cùng (giảm dần theo độ dài):")
print(strings