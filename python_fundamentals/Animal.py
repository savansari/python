class Animal:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    
    def walk(self):
        self.health-=1
        return self

    def run(self):
        self.health-=5
        return self

    def display_health(self):
        print(self.name," Health:",self.health)
        return self
    
class Dog(Animal):
    def __init__(self,name,health):
        super().__init__(name,health)
        self.health=150
    
    def pet(self):
        self.health+=5
        return self

class Dragon(Animal):
    def __init__(self,name,health):
        super().__init__(name,health)
        self.health=170 

    def fly(self):
        self.health+=10
        return self

    def display_health(self):
        super().display_health()
        print("I am a Dragon")

cat=Animal("Catty",100)
cat.walk().walk().walk().run().run().display_health()

dog=Dog("doggy",100)
dog.walk().walk().walk().run().run().pet().display_health()


dragon=Dragon("dragonny",200)
dragon.display_health()

one_animal=Animal("oneAnimal",300)

one_animal.display_health()
#one_animal.pet()
#one_animal.fly()

dog.fly()

