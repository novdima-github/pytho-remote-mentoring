"""
Создай класс Store. +
От него унаследуй подклассы GroceryStore и HardwareStore +
Создай класс Good. +
От него унаследуй подклассы Food и Tool. Создай 4-5 подклассов от каждого (Banana, Apple, Ham, Nail, Axe,  Saw…)
Каждый объект Good должен обладать read-only аттрибутом price, который задается в конструкторе, и должен быть положительным int или float.
У этих объектов также должен быть метод set_discount, который принимает аргумент процентов скидки в виде int.
Создай по одному магазину каждого типа, у каждого магазина должны быть методы add_item(item) и add_items(*items)

У магазина должны быть аттрибуты, показывающие суммарную цену всех товаров в нем, со скидкой и без.
Подсчитай общую стоимость товаров в каждом магазине со скидкой и без.
Магазины должны добавлять товар только свойственного им типа.


Пример:

belmarket = GroceryStore()
bananas = Banana(6)  # создаем бананы по 6$
strawberry = Strawberry(22)  # создаем клубнику по 22$
belmarket.add_item(bananas)
belmarket.add_item(strawberry)
print(belmarket.overall_price_no_discount)  # -> возвращаем 6+22 -> 28

belmarket.remove_item(strawberry)
strawberry.set_discount(50)
belmarket.add_item(strawberry)
print(belmarket.overall_price_no_discount)


hammer = Hammer(50)
belmarket.add_item(hammer)  # -> печатаем ошибку и не добавляем товар
"""

class Store:

    def __init__(self):
        self.items = {}
        self.number_of_products = 0
        self.overall_price_no_discount = 0
        self.overall_price_with_discount = 0

    def show_overall_price_no_discount(self):
        print(self.overall_price_no_discount)

    def show_overall_price_with_discount(self):
        print(self.overall_price_with_discount)

    def add_item(self, item):
        self.item = item
        self.overall_price_no_discount += item.price
        self.overall_price_with_discount += item.discounted_price

    def show_all_items(self):
        print(self.items)


class Good:

    def __init__(self, price):
        if price > 0:
            self.price = price
        else:
            raise ValueError
        self.discounted_price = price

    def set_discount(self, discount):
        self.discount = discount
        self.discounted_price = self.price * (1 - self.discount/100)





store = Store()

apple = Good(10)
orange = Good(20)

apple.set_discount(30)
orange.set_discount(30)
print(apple.price)
print(apple.discounted_price)

print(orange.price)
print(orange.discounted_price)

store.add_item(apple)
store.add_item(orange)
store.show_overall_price_no_discount()
store.show_overall_price_with_discount()