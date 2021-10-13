from typing import List

from abc import ABC, abstractmethod

from ..city import store
from ..car import car


class BasePlayer(ABC):
    place: store.BaseStore
    car: car.BaseCar
    items: List = []

    def __init__(self, player_car: car.BaseCar, start_position: store.BaseStore):
        self.car = player_car
        self.place = start_position

    def move_to(self, place: store.BaseStore):
        if place is self.place:
            print('you already at', place)
        else:
            print(f'moved from {self.place} to {place}')
            self.place = place

    def buy(self, item: store.StoreItem):
        items = self.place.sell(item)
        self.items.append(item)


class Player(BasePlayer):
    pass
