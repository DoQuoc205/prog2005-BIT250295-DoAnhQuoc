n = int(input("Nhập số dương: "))
if n > 1:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Nguyên tố" if is_prime else "Không phải nguyên tố")
else:
    print("Số không hợp lệ!")