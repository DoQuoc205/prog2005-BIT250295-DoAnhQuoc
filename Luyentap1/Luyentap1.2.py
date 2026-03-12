def bai2():
    a = float(input("nhập a: "))
    b = float(input("nhập b: "))

    luy_thua_a = a ** a
    luy_thua_b = b ** b
    can_bac_2_a = a ** 0.5
    can_bac_2_b = b ** 0.5
    chia_nguyen = a // b
    chia_du = a % b
    lam_tron = round(luy_thua_a, 2)
    lam_tron = round(luy_thua_b, 2)

    print("Lũy thừa a ^ a          =", luy_thua_a)
    print("Lũy thừa b ^ b          =", luy_thua_b)
    print("Căn bậc 2 của a         =", can_bac_2_a)
    print("Căn bậc 2 của b         =", can_bac_2_b)
    print("Chia lấy phần nguyên    =", chia_nguyen)
    print("Chia lấy phần dư        =", chia_du)
    print("Lũy thừa làm tròn 2 số  =", lam_tron)
bai2()