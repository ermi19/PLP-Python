class Hero: # parent class
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def __str__(self):
        return f"Hero Name: {self.name}, Power: {self.power}, Origin: {self.origin}"


class MyHero(Hero): # child class
    def __str__(self): #polymorphism
        return f"My Hero Name: {self.name}, Power: {self.power}, Origin: {self.origin}"  
    

hero1 = Hero("Mom", "Patience", "Ethiopia") #object one
hero3 = MyHero("Dad", "Consistency", "Ethiopia")

print(hero1)
print(hero3)

