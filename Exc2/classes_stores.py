'Subclasses of Store class'
from classes_goods import Tool, Food
from class_store import Store


class GroceryStore(Store):
    "GroceryStore inherited from Store"

    def __init__(self, item):
        super().__init__(item)
        self.parent_class = Food

    def add_item(self, item):
        'Add an item to the store'
        self.item = item
        if isinstance(self.item, self.parent_class):
            self.overall_price_no_discount += item._price
            self.overall_price_with_discount += item.discounted_price
            self.goods[item.__class__.__name__] = self.item._price
            print('{} added to the {}'.format
                  (self.item.__class__.__name__, self.__class__.__mro__[
                      0].__name__))
        else:
            print('{} can\'t be added to the {}'.format
                  (self.item.__class__.__name__,
                   self.__class__.__mro__[0].__name__))

    def add_items(self, *items):
        'Add items to the store'
        for self.item in items:
            if isinstance(self.item, self.parent_class):
                self.overall_price_no_discount += self.item._price
                self.overall_price_with_discount += self.item.discounted_price
                self.goods[self.item.__class__.__name__] = self.item._price
                print('{} added to the {}'.format
                      (self.item.__class__.__name__,
                       self.__class__.__mro__[0].__name__))
            else:
                print('{} can\'t be added to the {}'.format
                      (self.item.__class__.__name__,
                       self.__class__.__mro__[0].__name__))


class HardwareStore(Store):
    "HardwareStore inherited from Store"

    def __init__(self, item):
        super().__init__(item)
        self.parent_class = Tool

    def add_item(self, item):
        'Add an item to the store'
        self.item = item
        if isinstance(self.item, self.parent_class):
            self.overall_price_no_discount += item._price
            self.overall_price_with_discount += item.discounted_price
            self.goods[item.__class__.__name__] = self.item._price
            print('{} added to the {}'.format
                  (self.item.__class__.__name__,
                   self.__class__.__mro__[0].__name__))
        else:
            print('{} can\'t be added to the {}'.format
                  (self.item.__class__.__name__,
                   self.__class__.__mro__[0].__name__))

    def add_items(self, *items):
        'Add items to the store'
        for self.item in items:
            if isinstance(self.item, self.parent_class):
                self.overall_price_no_discount += self.item._price
                self.overall_price_with_discount += self.item.discounted_price
                self.goods[self.item.__class__.__name__] = self.item._price
                print('{} added to the {}'.format
                      (self.item.__class__.__name__,
                       self.__class__.__mro__[0].__name__))
            else:
                print('{} can\'t be added to the {}'.format
                      (self.item.__class__.__name__,
                       self.__class__.__mro__[0].__name__))
