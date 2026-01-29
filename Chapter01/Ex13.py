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