def bai5():
    import random
    m = int(input("nhập số hàng m: "))
    n = int(input("nhập số cột n: "))
    matrix = []
    for i in range(m):
        hang = []
        for j in range(n):
            so_ngau_nhien = random.randint(1, 99)
            hang.append(so_ngau_nhien)
        matrix.append(hang)
    print("\n ma trận vừa tạo là: ")
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()
    print("\n hiển thị hàng")
    hang_muon_xem = int(input(f"nhập số hàng muốn xem (từ 1 đến {m}): "))
    if 0 <= hang_muon_xem <= m:
        print(f"hàng {hang_muon_xem + 1}: {matrix[hang_muon_xem]}")
    else:
        print("số hàng không hợp lệ")
    print("\n hiển thị cột")
    cot_muon_xem = int(input(f"nhập số cột muốn xem (từ 1 đến {n}): ")) - 1
    if 0 <= cot_muon_xem <= n:
        print(f"Cột {cot_muon_xem + 1}: ", end="")
        for i in range(m):
            print(matrix[i][cot_muon_xem], end=" ")
        print()
    else:
        print("số cột không hợp lệ")
    gia_tri_lon_nhat = matrix[0][0]

    for i in range(m):
        for j in range(n):
            if matrix[i][j] > gia_tri_lon_nhat:
                gia_tri_lon_nhat = matrix[i][j]

    print(f"\nGiá trị lớn nhất trong ma trận là: {gia_tri_lon_nhat}")
bai5()