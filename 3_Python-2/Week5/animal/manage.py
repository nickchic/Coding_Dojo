from animal import Animal, Dog, Dragon

red_panda = Animal("amber",100)

red_panda.run().display_health()

hank = Dog("Hank")

hank.display_health()

hank.pet().display_health()

drogon = Dragon("Drogon")

drogon.fly().display_health()

print hank
