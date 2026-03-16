
class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
s1 = student("Trần Duy Long",9.3)
s2 = student("Nguyen Thi Nhi", 9.6)
if s1.score > s2.score:
        print("sinh viên có điểm cao hơn:", s1.name)
else:
        print("sinh viên có điểm cao hơn:", s2.name)