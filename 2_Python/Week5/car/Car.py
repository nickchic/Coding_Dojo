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
    def __repr__(self):
        return "Price: {}, Speed: {}, Fuel: {}, Milage: {}, Tax: {}".format(self.price, self.fuel, self.speed, self.mileage, self.tax)
