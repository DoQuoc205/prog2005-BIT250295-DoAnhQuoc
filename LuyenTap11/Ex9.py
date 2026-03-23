def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = input(f"Nhập phần tử tại vị trí [{i}][{j}]: ")
            if val.strip() == "":
                raise ValueError("Lỗi: Không được nhập giá trị trống!")
            row.append(int(val))
        matrix.append(row)
    return matrix

rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))

print("Nhập ma trận A:")
A = input_matrix(rows, cols)

print("Nhập ma trận B:")
B = input_matrix(rows, cols)

C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Kết quả cộng hai ma trận:")
for row in C:
    print(row)