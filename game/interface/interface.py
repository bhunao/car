from abc import ABC, abstractmethod
from typing import List

from ..player import player
from ..city import BaseStore


class BaseInterface(ABC):
    players: List[player.Player]
    places: List[BaseStore]
    game_ticks: int = 0

    def __init__(self, players, places):
        self.players = players
        self.places = places

    def next_game_tick(self):
        pass

    @abstractmethod
    def run(self):
        pass


class Interface(BaseInterface):
    def run(self):
        print("the game is running")
        while True:
            self.next_game_tick()
