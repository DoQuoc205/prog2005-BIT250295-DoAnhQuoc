class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Tuổi không được âm")
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Tuổi không hợp lệ")
        self._age = age

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"Person(name={self._name}, age={self._age})"

    def introduce(self):
        return f"Xin chào, tôi là {self._name}, {self._age} tuổi."

    @classmethod
    def from_string(cls, info_str):
        name, age = info_str.split(",")
        return cls(name.strip(), int(age.strip()))

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __eq__(self, other):
        if isinstance(other, Person):
            return self._name == other._name and self._age == other._age
        return False


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id

    def get_student_id(self):
        return self._student_id

    def set_student_id(self, student_id):
        self._student_id = student_id

    def __str__(self):
        return f"Student(name={self._name}, age={self._age}, id={self._student_id})"

    def study(self, subject):
        return f"{self._name} đang học môn {subject}."


p1 = Person("An", 20)
p2 = Person.from_string("Bình, 25")
s1 = Student("Cường", 19, "SV001")

print(p1.introduce())
print(p2)
print(s1)
print(s1.study("Toán"))

print("p1 == p2 ?", p1 == p2)
print("Người 20 tuổi có phải người lớn?", Person.is_adult(20))

try:
    p1.set_age(-5)
except ValueError as e:
    print("Lỗi:", e)