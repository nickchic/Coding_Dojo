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

beer = Product(5.0, "Lager", 1, "Yeungling", 3.00)
soda = Product(1.25, "Diet Coke", 1, "Coca Cola", 0.50)

beer.displayInfo()
beer.add_tax(0.60).sell().displayInfo()
soda.sell().displayInfo()
soda.Return("Too flat").displayInfo()
