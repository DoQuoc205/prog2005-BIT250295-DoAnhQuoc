def bai4():
    print("in các số từ 1 - 100, bỏ qua các số chia hết cho 3.")
    for i in range(1, 101):
        if i % 3 != 0:
            print(i, end=" ")
bai4()