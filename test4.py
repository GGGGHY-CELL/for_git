class Dog:   
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def voice(self):
        print("Гав")

dog1 = Dog("Bobby", 3)
dog2 = Dog("Jack", 5)

dog1.voice()  
dog2.voice()  