students = []
for i in range(3):
    print(f"\nNhập thông tin cho sinh viên {i+1}:")
    name = input("Tên: ")
    math = float(input("Điểm Toán: "))
    physics = float(input("Điểm Lý: "))
    chemistry = float(input("Điểm Hóa: "))
    average = (math + physics + chemistry) / 3
    students.append((name, average))
print("\n--- Kết quả ---")
for name, avg in students:
    print(f"Sinh viên: {name}, Điểm trung bình: {avg:.2f}")