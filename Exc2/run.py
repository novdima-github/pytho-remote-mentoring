'Run module'
from classes_stores import GroceryStore, HardwareStore
from classes_goods import Banana, Apple, Lemon, Nail, Axe, Hammer

GROCERY = GroceryStore('gs')
HARDWARE = HardwareStore('hs')
APPLE = Apple(10)
LEMON = Lemon(10)
BANANA = Banana(10)
G_BANANA = Banana(20)
NAIL = Nail(20)
AXE = Axe(20)
HAMMER = Hammer(20)
# APPLE.price
# lemon.price = 200 !!!
APPLE.set_discount(10)
BANANA.set_discount(10)
LEMON.set_discount(10)

GROCERY.add_item(APPLE)
GROCERY.add_items(BANANA, NAIL, LEMON, G_BANANA)
GROCERY.add_item(NAIL)
GROCERY.show_all_items()
GROCERY.remove_item(NAIL)
GROCERY.remove_item(BANANA)
GROCERY.show_all_items()
GROCERY.show_overall_price_no_discount()
GROCERY.show_overall_price_with_discount()
GROCERY.show_all_items()
NAIL.set_discount(10)
AXE.set_discount(10)
HAMMER.set_discount(10)
HARDWARE.add_item(NAIL)
HARDWARE.add_items(HAMMER, AXE, BANANA)
HARDWARE.show_all_items()
HARDWARE.show_overall_price_no_discount()
HARDWARE.show_overall_price_with_discount()
