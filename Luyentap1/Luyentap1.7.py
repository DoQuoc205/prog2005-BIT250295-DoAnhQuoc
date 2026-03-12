class Student:
    def __init__(self, tên, điểm):
        self.tên = tên
        self.điểm = điểm
sv1 = Student("TRAN DUY LONG", 9)
sv2 = Student("LAM TRAN", 7)
print(sv1.tên, sv1.điểm)
print(sv2.tên, sv2.điểm)