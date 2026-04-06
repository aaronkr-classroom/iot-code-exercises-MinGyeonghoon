#5_class.py

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"My name is {self.name}!")

class Dog(Animal): #is-a 관계(자식)
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age #has-a 속성
    
    def speak(self):
        super().speak()
        print(f"{self.name} says woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")
        
my_dog = Dog("spot", 3)
my_cat = Cat("Fireheart")
my_dog.speak()
my_cat.speak()