import csv
n = int(input("Nhập số lượng nhân viên: "))
employees = []
for i in range(n):
    name = input(f"Nhập tên nhân viên {i+1}: ")
    age = int(input(f"Nhập tuổi của {name}: "))
    emp_id = input(f"Nhập ID của {name}: ")
    employees.append({"name": name, "age": age, "id": emp_id})

with open("employees.txt", "w", encoding="utf-8") as f:
    for emp in employees:
        f.write(f"Tên: {emp['name']}, Tuổi: {emp['age']}, ID: {emp['id']}\n")

print("Đã lưu thông tin vào file employees.txt")

with open("employees.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "id"])
    writer.writeheader()
    writer.writerows(employees)

print("Đã lưu thông tin vào file employees.csv")
