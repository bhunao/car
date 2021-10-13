from .car import car
from .car import car_parts
from .city import store
from .player import player
from . import utils


def main():
    # car
    engine = car_parts.Engine()
    gas_tank = car_parts.Gas_Tank()
    wheels = car_parts.Wheels()
    car1 = car.Car("random_car", engine, gas_tank, wheels)

    # places
    store1 = store.Store("loja1")
    store2 = store.Store('loja2')
    store3 = store.Store('garage')

    # items
    item1 = store.StoreItem('manga', 1)
    item2 = store.StoreItem('motor', 50)
    item3 = store.StoreItem('pneu', 20)
    [store1.add_to_stock(item) for item in utils.generate_stock(item1, 10)]
    [store2.add_to_stock(item) for item in utils.generate_stock(item2, 10)]
    [store3.add_to_stock(item) for item in utils.generate_stock(item3, 10)]

    # player
    player1 = player.Player(player_car=car1, start_position=store1)


if __name__ == "__main__":
    main()
