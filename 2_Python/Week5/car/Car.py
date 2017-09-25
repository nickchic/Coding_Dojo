class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price < 10000:
            self.tax = 0.12
        else:
            self.tax = 0.15
        self.display_all()
    def display_all(self):
        print "Price: ", self.price
        print "Fuel: ", self.fuel
        print "Speed: ", self.speed
        print "Mileage: ", self.mileage
        print "Tax: ", self.tax
        return self

red_car = Car(3000,100,"full",30)
blue_car = Car(20000,130,"not full",40)
purple_car = Car(17000,140,"full",30)
yellow_car = Car(7000,50,"kind of full",100)
green_car = Car(4000,110,"full",20)
black_car = Car(1000000,9000,"full",450000)
