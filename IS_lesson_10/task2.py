# task2
from abc import ABC, abstractmethod
from math import ceil


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    @property
    def consumption(self):
        return ceil((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def consumption(self):
        return ceil((2 * self.param) + 0.3)


coat = Coat(50)
suit = Suit(150)
print(coat.consumption)
print(suit.consumption)
