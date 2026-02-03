n = int(input("Nhập số n: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Không phải số nguyên tố")
            break
    else:
        print("Là số nguyên tố")
else:
    print("Không hợp lệ!")