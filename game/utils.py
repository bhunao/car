from typing import List

from .city import store


def generate_stock(item: store.BaseStoreItem, quantity:int =0) -> List[store.BaseStoreItem]:
        return [item for _ in range(quantity)]
