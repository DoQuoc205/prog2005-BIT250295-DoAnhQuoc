m, n = 2, 3  # ví dụ ma trận 2x3
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9], [10, 11, 12]]

C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
print("Kết quả cộng ma trận:")
for row in C:
    print(row)