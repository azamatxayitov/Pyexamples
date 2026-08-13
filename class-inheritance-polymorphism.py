'''
Class deep diving
1 encapsulation 
2 inheritance
3 polymorphism

'''

print("==== inheritance ====")
# parent > child

class Animal:
    # state 
    description = " The class creates animals "
    
    #constructor
    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice
        
    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")
        
        
class Dog(Animal): # child
    # state 
    
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
        
    #method 
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")
        
    def protect(self):
        print("Yes, I can protect you!") 
        
        
class Cat(Animal): # child
    # state 
    
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
        
    #method 
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")
        
    def play(self):
        pss
        
        
class Fish(Animal): # child
    # state 
    
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
        
    #method 
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")
        
    def swim(self):
        print("Yes, I can swim!")                                  
        
        
dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()
        