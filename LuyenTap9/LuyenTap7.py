class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s: str):
        name, age = s.split("-")
        return cls(name, int(age))

    def __str__(self):
        return f"{self.name}, {self.age} tuổi"

p = Person.from_string("Nam-20")
print(p)