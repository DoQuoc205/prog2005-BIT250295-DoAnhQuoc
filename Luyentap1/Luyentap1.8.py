class Student:
    def __init__(self, tên, điểm):
        if 0 <= điểm <= 10:
            self.tên = tên
            self.điểm = điểm
        else:
            raise ValueError("Điểm phải nằm trong khoảng 0–10")