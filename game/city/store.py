from typing import List

from abc import ABC, abstractmethod


class BaseStoreItem(ABC):
    name: str
    price: float

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        class_name = self.__class__.__name__
        name = self.name
        price = self.price
        return f'{class_name}({name=}, {price=})'

    def __str__(self):
        return f'[{self.name}:{self.price}]'


class BaseStore(ABC):
    name: str
    description: str
    stock: List[BaseStoreItem]


    def __init__(self, name: str, description: str='', stock: List[BaseStoreItem]=[]):
        self.name = name
        self.description = description
        self.stock = stock

    def __repr__(self):
        class_name = self.__class__.__name__
        name = self.name
        description = self.description
        return f'{class_name}({name=}, {description=})'

    def __str__(self):
        return f'[{self.name}:{self.description}]'

    def add_to_stock(self, item: BaseStoreItem):
        print(f'item {item} added to the stock of {self}')
        self.stock.append(item)

    @abstractmethod
    def sell():
        pass


class StoreItem(BaseStoreItem):
    pass

class Store(BaseStore):
    def sell(self, item):
        if item in self.stock:
            self.stock.remove(item)
            print(f'item {item} sold')
            return item
        raise Exception(f'no item named {item.name!r} in the store {self.name!r}')

class Garage(BaseStore):
    def sell():
        pass
