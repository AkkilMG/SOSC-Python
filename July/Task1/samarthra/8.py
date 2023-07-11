
# overloading
class Math:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

    def multiply(self, a, b):
        return a * b

    def multiply(self, a, b, c):
        return a * b * c



maths = Math()


print(maths.add(2, 3))               
print(maths.add(2, 3, 4))             

print(maths.multiply(2, 3))           
print(maths.multiply(2, 3, 4))       

# overriding
class Animal:
    def make_sound(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")


class Cat(Animal):
    def make_sound(self):
        print("The cat meows.")



animal = Animal()
dog = Dog()
cat = Cat()


animal.make_sound()  
dog.make_sound()     
cat.make_sound()     
