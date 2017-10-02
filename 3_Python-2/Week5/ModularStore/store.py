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
    def __repr__(self):
        return "Store Location: {}, Store Owner: {}, Store Products: {}".format(self.location, self.owner, self.products)
