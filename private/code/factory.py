class Animal:
    def whoami(self):
        pass

class Dog(Animal):
    def whoami(self):
        return "Woofff ..."

class Cat(Animal):
    def whoami(self):
        return "Meoww ..."

class AnimalFactory:
    @staticmethod
    def create(typ):
        if typ == "dog":
            return Dog()
        elif typ == "cat":
            return Cat()
        return None

animal = AnimalFactory.create("dog")
print(animal.whoami()) 