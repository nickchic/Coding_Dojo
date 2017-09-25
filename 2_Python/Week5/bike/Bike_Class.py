class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
        print "New bike created!"

    def displayInfo(self):
        print "Price = ", self.price, " Max speed = ", self.max_speed, " Miles = ", self.miles
        return self;

    def ride(self):
        self.miles += 10
        print "Riding"
        return self;

    def reverse(self):
        self.miles -= 5
        print "Riding backwards"
        return self;

red_bike = Bike(10,20)
red_bike.ride().ride().ride().reverse().displayInfo()

blue_bike = Bike(50,100)
blue_bike.ride().ride().reverse().reverse().displayInfo()
