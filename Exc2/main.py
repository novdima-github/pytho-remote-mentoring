"""
Создай класс Store.
От него унаследуй подклассы GroceryStore и HardwareStore
Создай класс Good.
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
    "This is a main Store class"
    def __init__(self):
        self.items = {}
        self.number_of_products = 0
        self.overall_price_no_discount = 0
        self.overall_price_with_discount = 0

    def show_overall_price_no_discount(self):
        print('overall_price_no_discount: ' +
              str(self.overall_price_no_discount) +
              ' - for' + str(self.__class__.__mro__[0].__name__))

    def show_overall_price_with_discount(self):
        print('overall_price_with_discount: ' +
              str(self.overall_price_with_discount) +
              ' - for' + str(self.__class__.__mro__[0].__name__))

    def add_item(self, item):
        self.item = item
        self.overall_price_no_discount += item.price
        self.overall_price_with_discount += item.discounted_price
        self.items[item.__class__.__name__] = self.item.price
        print('{} added'.format(self.item.__class__.__name__))


    def remove_item(self, item):
        self.item = item
        if self.item.__class__.__name__ in self.items:
            self.overall_price_no_discount -= item._price
            self.overall_price_with_discount -= item.discounted_price
            del self.items[item.__class__.__name__]
            print('{} has removed from {}'.format(self.item.__class__.__name__,
                                              self.__class__.__mro__[0].
                                                              __name__))
        else:
            print('{} can\'t be removed. It is not in {} '.format(
                self.item.__class__.__name__, self.__class__.__mro__[0].
                                                              __name__))


    def show_all_items(self):
        print('All goods in {}: {}'.format(self.__class__.__mro__[0].__name__,
                                                            self.items))


class GroceryStore(Store):
    "GroceryStore inherited from Store"
    def add_item(self, item):
        self.item = item
        self.parent_class = Food
        if isinstance(self.item, self.parent_class) == True:
            self.overall_price_no_discount += item._price
            self.overall_price_with_discount += item.discounted_price
            self.items[item.__class__.__name__] = self.item._price
            print('{} added to the {}'.format(self.item.__class__.__name__,
                                              self.__class__.__mro__[0].
                                                              __name__))
        else:
            print('{} can\'t be added to the {}'.
                  format(self.item.__class__.__name__,
                  self.__class__.__mro__[0].
                  __name__))


class HardwareStore(Store):
    "HardwareStore inherited from Store"
    def add_item(self, item):
        self.item = item
        self.parent_class = Tool
        if isinstance(self.item, self.parent_class) == True:
            self.overall_price_no_discount += item._price
            self.overall_price_with_discount += item.discounted_price
            self.items[item.__class__.__name__] = self.item._price
            print('{} added to the {}'.format(self.item.__class__.__name__,
                                              self.__class__.__mro__[0].
                                              __name__))
        else:
            print('{} can\'t be added to the {}'.
                  format(self.item.__class__.__name__,
                         self.__class__.__mro__[0].
                         __name__))


class Good:

    def __init__(self, price):
        if price > 0:
            self._price = price
        else:
            raise ValueError
        self.discounted_price = price

    @property
    def price(self):
        print("{} price: {}".format(self.__class__.__name__, self._price))
        return self._price

    def set_discount(self, discount):
        self.discount = discount
        self.discounted_price = self._price * (1 - self.discount / 100)
        print("{} discounted price set: {}".format(self.__class__.__name__,
                                                   self.discounted_price))
        return self.discounted_price


class Food(Good):
    pass

class Banana(Food):
    pass

class Apple(Food):
    pass

class Lemon(Food):
    pass


class Tool(Good):
    pass

class Nail(Tool):
    pass

class Axe(Tool):
    pass

class Hammer(Tool):
    pass


grocery_store = GroceryStore()
hardware_store = HardwareStore()

apple = Apple(10)
lemon = Lemon(10)
banana = Banana(10)
nail = Nail(20)
axe = Axe(20)
hammer = Hammer(20)
apple.price
# lemon.price = 200 !!!

apple.set_discount(10)
banana.set_discount(10)
lemon.set_discount(10)
grocery_store.add_item(apple)
grocery_store.add_item(banana)
grocery_store.add_item(nail)
grocery_store.show_all_items()
grocery_store.remove_item(nail)
grocery_store.remove_item(banana)
grocery_store.show_all_items()
grocery_store.show_overall_price_no_discount()
grocery_store.show_overall_price_with_discount()
grocery_store.add_item(lemon)
grocery_store.show_overall_price_no_discount()
grocery_store.show_overall_price_with_discount()
grocery_store.show_all_items()

nail.set_discount(10)
axe.set_discount(10)
hammer.set_discount(10)
hardware_store.add_item(nail)
hardware_store.add_item(hammer)
hardware_store.add_item(axe)
hardware_store.show_all_items()
hardware_store.show_overall_price_no_discount()
hardware_store.show_overall_price_with_discount()