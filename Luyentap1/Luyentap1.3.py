def bai3():
    a = int(input("nhập số: "))
    if a < 1 or a > 9:
        print("nhập một số từ 1 tới 9")
    else:
        print("bảng cửu chương của {a} là: ")
        for i in range(1,11):
            print(f'{a}*{i} = {a*i}')
bai3()