from abc import ABC, abstractmethod


class BaseEngine(ABC):
    name: str
    engine_block: str
    piston: str
    power: float
    horses: int


    def __init__(self):
        self.name = 'engine_name'
        self.engine_block = 'normal_block'
        self.piston = 'normal_piston'
        self.power = 1.2
        self.horse = 3

class BaseGas_Tank(ABC):
    name: str
    size: int
    type: int # 1 for gas, 2 for alcohol, 2 for flex

    def __init__(self):
        self.name = 'gast_tank_name'
        self.size = 10
        self.type = 1


class BaseWheels(ABC):
    name: str
    size: float # in cm


    def __init__(self):
        self.name = 'wheels_name'
        self.size = 60

class Engine(BaseEngine):
    pass


class Gas_Tank(BaseGas_Tank):
    pass

class Wheels(BaseWheels):
    pass
