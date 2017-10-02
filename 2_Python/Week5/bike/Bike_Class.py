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

    def __repr__(self):
        return "Price: {}, Max Speed: {}, Miles: {}".format(self.price, self.max_speed, self.miles)
