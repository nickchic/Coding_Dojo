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

class Store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def inventory(self):
        idx = 0
        for product in self.products:
            idx += 1
            print "product ", idx
            product.displayInfo()
        return self

beer = Product(5.0, "Lager", 1, "Yeungling", 3.00)
soda = Product(1.25, "Diet Coke", 1, "Coca Cola", 0.50)
toy = Product(20.0, "Lego Batman", 2, "Lego", 5.50)

nicks_store = Store("Philadelphia", "Nick")
nicks_store.add_product(beer).add_product(soda).add_product(toy).inventory()
