"""Run module"""

from stores import GroceryStore, HardwareStore, Store
from goods import Banana, Apple, Lemon, Nail, Axe, Hammer, Pear

grocery = GroceryStore()
hardware = HardwareStore()
print(grocery.all_goods_in_store)
pear = Pear(2.56, 50)
hammer = Hammer(100, 25)
print(pear.price)
print(pear.discount)
print(pear.price_with_discount)
hardware.add_good(pear)
print(hardware.all_goods_in_store)
grocery.add_good(pear)
print(grocery.all_goods_in_store)
apple = Apple(3, 20)
grocery.add_good(apple)
print(grocery.all_goods_in_store)
print(grocery.overall_price_no_discount)
print(grocery.overall_price_with_discount)

apple.discount = 50
print(apple.price_with_discount)
print(grocery.overall_price_with_discount)
apple.discount = 57
super_store = Store()
apple.price = 301
grocery.add_goods(hammer, hammer)
hardware.add_goods(hammer, apple, pear)
print(grocery.overall_price_no_discount)
print(grocery.overall_price_with_discount)

lemon = Lemon(123.4, 34.23)
nail = Nail(432.23, 87.66)
grocery.add_goods(lemon, nail)
hardware.add_goods(lemon, nail)
print(grocery.overall_price_no_discount)
print(grocery.overall_price_with_discount)
print(hardware.overall_price_no_discount)
print(hardware.overall_price_with_discount)

hardware.remove_good(nail)
grocery.remove_good(lemon)

print(hardware.overall_price_no_discount)
print(hardware.overall_price_with_discount)
print(hardware.all_goods_in_store)
print(grocery.all_goods_in_store)

grocery.add_good(hammer)