class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal sound...")


class Dog(Animal):
    def __init__(self, name):

        super().__init__(name)

    def sound(self):
        print("Gâu gâu!")

cho1 = Dog("Bun Bun")
print("Tên:", cho1.name)
cho1.sound()