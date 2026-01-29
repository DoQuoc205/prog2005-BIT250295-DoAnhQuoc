import math

def bai1():
    so_nguyen = 10
    so_thuc = 3.14
    chuoi = "Hello, World"
    print("Số nguyên:", so_nguyen)
    print("Số thực:", so_thuc)
    print("Chuỗi:", chuoi)

def bai2():
    PI = 3.14
    r = 5
    chu_vi = 2 * PI * r
    print("Chu vi hình tròn với bán kính", r, "là:", chu_vi)

def bai3():
    a = int(input("Nhập số nguyên thứ nhất: "))
    b = int(input("Nhập số nguyên thứ hai: "))
    print("Tổng:", a + b)
    print("Hiệu:", a - b)
    print("Tích:", a * b)
    print("Thương:", a / b)

def bai4():
    def sum_two_numbers(a, b):
        return a + b
    ket_qua = sum_two_numbers(7, 5)
    print("Tổng của hai số là:", ket_qua)

def bai5():
    name = "Đỗ Anh Quốc"
    age = 20
    average_score = 8.5
    print("Kiểu dữ liệu của name:", type(name))
    print("Kiểu dữ liệu của age:", type(age))
    print("Kiểu dữ liệu của average_score:", type(average_score))
    age_next_year = age + 1
    doubled_score = average_score * 2
    print("\n--- Thông tin cá nhân ---")
    print("Tên:", name, "| Kiểu:", type(name))
    print("Tuổi hiện tại:", age, "| Kiểu:", type(age))
    print("Điểm trung bình:", average_score, "| Kiểu:", type(average_score))
    print("Tuổi năm sau:", age_next_year, "| Kiểu:", type(age_next_year))
    print("Điểm nhân đôi:", doubled_score, "| Kiểu:", type(doubled_score))

def bai6():
    def is_even(n):
        return n % 2 == 0
    print(is_even(4))
    print(is_even(7))

def bai7():
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    c = int(input("Nhập số thứ ba: "))
    print("Số lớn nhất trong ba số là:", max(a, b, c))

def bai8():
    def greet(name="Student"):
        print("Hello,", name + "!")
    greet()
    greet("Quốc")

def bai9():
    age = int(input("Nhập tuổi của bạn: "))
    if 1 <= age <= 120:
        print("Tuổi hợp lệ:", age)
    else:
        print("Tuổi không hợp lệ. Vui lòng nhập từ 1 đến 120.")

def bai10():
    text = input("Nhập một chuỗi: ")
    count_a = text.count('a')
    print("Số lần xuất hiện của ký tự 'a' là:", count_a)

def bai11():
    celsius = float(input("Nhập nhiệt độ (°C): "))
    fahrenheit = celsius * 9/5 + 32
    print(f"Nhiệt độ {celsius:.2f}°C tương ứng {fahrenheit:.2f}°F")

def bai12():
    weight = float(input("Nhập cân nặng (kg): "))
    height = float(input("Nhập chiều cao (m): "))
    bmi = weight / (height * height)
    print(f"Chỉ số BMI của bạn là: {bmi:.2f}")

def bai13():
    try:
        a = int(input("Nhập số nguyên thứ nhất: "))
        b = int(input("Nhập số nguyên thứ hai: "))
        if b == 0:
            print("Lỗi: Không thể chia cho 0.")
        else:
            ket_qua = a / b
            print(f"Kết quả phép chia {a} / {b} = {ket_qua:.2f}")
    except ValueError:
        print("Lỗi: nhập số nguyên hợp lệ.")

def bai14():
    n = float(input("Nhập một số: "))
    if n < 0:
        print("Lỗi: Không thể tính căn bậc hai của số âm.")
    else:
        sqrt_n = math.sqrt(n)
        print(f"Căn bậc hai của {n} là: {sqrt_n:.2f}")

def bai15():
    students = []
    for i in range(3):
        print(f"\nNhập thông tin cho sinh viên {i+1}:")
        name = input("Tên: ")
        math_score = float(input("Điểm Toán: "))
        physics = float(input("Điểm Lý: "))
        chemistry = float(input("Điểm Hóa: "))
        average = (math_score + physics + chemistry) / 3
        students.append((name, average))
    print("\n--- Kết quả ---")
    for name, avg in students:
        print(f"Sinh viên: {name}, Điểm trung bình: {avg:.2f}")

# Menu chính
while True:
    print("\n===== MENU =====")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Bài 3")
    print("4. Bài 4")
    print("5. Bài 5")
    print("6. Bài 6")
    print("7. Bài 7")
    print("8. Bài 8")
    print("9. Bài 9")
    print("10. Bài 10")
    print("11. Bài 11")
    print("12. Bài 12")
    print("13. Bài 13")
    print("14. Bài 14")
    print("15. Bài 15")
    print("0. Thoát")

    choice = input("Chọn bài muốn chạy: ")

    if choice == "1": bai1()
    elif choice == "2": bai2()
    elif choice == "3": bai3()
    elif choice == "4": bai4()
    elif choice == "5": bai5()
    elif choice == "6": bai6()
    elif choice == "7": bai7()
    elif choice == "8": bai8()
    elif choice == "9": bai9()
    elif choice == "10": bai10()
    elif choice == "11": bai11()
    elif choice == "12": bai12()
    elif choice == "13": bai13()
    elif choice == "14": bai14()
    elif choice == "15": bai15()
    elif choice == "0":
        print("Thoát.")
        break
    else:
        print("Lựa chọn không hợp lệ, chọn lại.")