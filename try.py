class Store():

    def __init__(self):
        self.all_products = {}

    def add_product(self, product):
        self.product = product
        self.all_products[self.product.name] = self.product.price


class Product():
    def __init__(self, name, price):
        self.price = price
        self.name = name


prod1 = Product('prod1', 10)
my_store = Store()

my_store.add_product(prod1)

print(my_store.all_products)

