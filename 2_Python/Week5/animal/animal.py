class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 5
        return self
    def run(self):
        self.health -= 10
        return self
    def display_health(self):
        print self.name, " has ", self.health, " HP."
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"
        return self

red_panda = Animal("amber",100)

red_panda.run().display_health()

hank = Dog("Hank")

hank.display_health()
hank.pet().display_health()

drogon = Dragon("Drogon")

drogon.fly().display_health()
