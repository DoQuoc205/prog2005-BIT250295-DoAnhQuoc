class Student:
    def __init__(self, tên, điểm):
        if 0 <= điểm <= 10:
            self.tên = tên
            self.điểm = điểm
        else:
            raise ValueError("Điểm phải nằm trong khoảng 0–10")
    def display(self):
        print(f"Sinh viên {self.tên} có điểm là {self.điểm}")
sv1 = Student("DO ANH QUOC", 10)
sv1.display()