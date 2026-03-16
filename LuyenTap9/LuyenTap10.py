class SinhVien:
    so_luong = 0

    def __init__(self, name):
        self.name = name

        SinhVien.so_luong += 1

    @classmethod
    def dem_so_luong(cls):
        return cls.so_luong



sv1 = SinhVien("Lâm")
sv2 = SinhVien("Long")
sv3 = SinhVien("Quốc")

print("Số lượng sinh viên:", SinhVien.dem_so_luong())