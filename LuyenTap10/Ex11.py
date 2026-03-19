def bai6():
    s = input("Nhập chuỗi: ")
    reversed_s = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    print("Chuỗi đảo ngược:", reversed_s)

def bai8():
    strings = []
    for i in range(5):
        s = input(f"Nhập chuỗi thứ {i+1}: ")
        strings.append(s)
    n = len(strings)
    print("\nQuá trình sắp xếp:")
    for i in range(n - 1):
        for j in range(n - i - 1):
            if len(strings[j]) < len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
            print(f"Bước {i}-{j}: {strings}")
    print("\nKết quả cuối cùng:", strings)

def bai9():
    class Person:
        def __init__(self, name, age):
            if age < 0:
                raise ValueError("Tuổi không được âm")
            self._name = name
            self._age = age

        def get_name(self): return self._name
        def get_age(self): return self._age
        def set_age(self, age):
            if age < 0: raise ValueError("Tuổi không hợp lệ")
            self._age = age
        def __str__(self): return f"Person(name={self._name}, age={self._age})"
        def introduce(self): return f"Tôi là {self._name}, {self._age} tuổi."
        @classmethod
        def from_string(cls, info_str):
            name, age = info_str.split(",")
            return cls(name.strip(), int(age.strip()))
        @staticmethod
        def is_adult(age): return age >= 18
        def __eq__(self, other):
            return isinstance(other, Person) and self._name == other._name and self._age == other._age

    class Student(Person):
        def __init__(self, name, age, student_id):
            super().__init__(name, age)
            self._student_id = student_id
        def __str__(self): return f"Student(name={self._name}, age={self._age}, id={self._student_id})"
        def study(self, subject): return f"{self._name} đang học {subject}"

    p1 = Person("An", 20)
    p2 = Person.from_string("Bình, 25")
    s1 = Student("Cường", 19, "SV001")
    print(p1.introduce())
    print(p2)
    print(s1)
    print(s1.study("Toán"))
    print("p1 == p2 ?", p1 == p2)
    print("Người 20 tuổi có phải người lớn?", Person.is_adult(20))

def bai10():
    strings = []
    for i in range(5):
        s = input(f"Nhập chuỗi thứ {i+1}: ")
        strings.append(s)
    n = len(strings)
    print("\nQuá trình sắp xếp:")
    for i in range(n - 1):
        for j in range(n - i - 1):
            if len(strings[j]) < len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
            print(f"Bước {i}-{j}: {strings}")
    print("\nKết quả cuối cùng:", strings)

while True:
    print("\n--- MENU ---")
    print("6. Bài 6: Đảo ngược chuỗi")
    print("8. Bài 8: Bubble sort độ dài chuỗi (giảm dần)")
    print("9. Bài 9: Class Person/Student")
    print("10. Bài 10: Bubble sort độ dài chuỗi (giảm dần)")
    print("0. Thoát")

    choice = input("Chọn bài tập muốn chạy: ")

    if choice == "6":
        bai6()
    elif choice == "8":
        bai8()
    elif choice == "9":
        bai9()
    elif choice == "10":
        bai10()
    elif choice == "0":
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")