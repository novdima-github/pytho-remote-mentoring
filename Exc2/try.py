class Geeks:
    def __init__(self, age):
        self._age = age

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

        # a setter function

    # @age.setter
    # def age(self, a):
    #     if (a < 18):
    #         raise ValueError("Sorry you age is below eligibility criteria")
    #     print("setter method called")
    #     self._age = a


mark = Geeks(10)

# mark.age = 19

print(mark.age) 