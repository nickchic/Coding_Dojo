from store import Store
from product import Product

beer = Product(5.0, "Lager", 1, "Yeungling", 3.00)
soda = Product(1.25, "Diet Coke", 1, "Coca Cola", 0.50)
toy = Product(20.0, "Lego Batman", 2, "Lego", 5.50)

nicks_store = Store("Philadelphia", "Nick")
nicks_store.add_product(beer).add_product(soda).add_product(toy).inventory()

print nicks_store
