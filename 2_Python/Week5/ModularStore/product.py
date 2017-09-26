class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold"
        return self
    def add_tax(self, tax):
        self.price += tax
        return self
    def Return(self, reason):
        self.status = reason
        return self
    def displayInfo(self):
        print "price = ", self.price
        print "name = ", self.name
        print "weight = ", self.weight
        print "brand = ", self.brand
        print "cost = ", self.cost
        print "status = ", self.status
        return self


if __name__ == "__main__":
    watch = Product(80.0, "Watch", 1, "Garmin", 60.00)
    watch.displayInfo()
