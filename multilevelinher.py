class Animal:
    def walk(self):
        print("walking....")
    def eat(self):
        print("eating......")

class Dog(Animal):
    def sound(self):
        print("vauu vauu barking")
    def move(self):
        print("moving...")

d1=Dog()
d1.eat()

class Labrador(Dog):
    def protect(self):
        print("Alert....")
    
d=Labrador()
d.walk()
