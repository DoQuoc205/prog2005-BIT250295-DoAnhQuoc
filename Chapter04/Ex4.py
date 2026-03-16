class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau

    def __str__(self):
        return f"Hoa: {self.ten}, Màu: {self.mau}"

hoa_hong = Hoa("Hoa Hồng", "Đỏ")
print(hoa_hong)