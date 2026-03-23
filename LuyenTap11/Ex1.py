string = []
for i in range(5):
    s = input(f"nhập chuỗi thứ {i+1}: ")
    string.append(s)

n = len(string)

print("\nQuá trình sắp xếp:")

for i in range(n - 1):
    for j in range(n - i - 1):
        if len(string[j]) < len(string[j + 1]):

            string[j], string[j + 1] = string[j + 1], string[j]

        print(f"Bước {i}-{j}: {string}")

print("\nKết quả cuối cùng (giảm dần theo độ dài):")
print(string)