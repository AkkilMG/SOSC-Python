# class and inheritance
class Animal:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
        
    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
        
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def show(self):
        super().show()
        print(f"Breed: {self.breed}")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        super().show()
        print(f"Color: {self.color}")        