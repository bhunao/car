from abc import ABC, abstractmethod

from . import car_parts

class BaseCar(ABC):
    model_name: str
    engine: car_parts.BaseEngine
    gas_tank: car_parts.BaseGas_Tank
    wheels: car_parts.BaseWheels

    
    def __init__(self, name: str,
                 engine: car_parts.Engine,
                 gas_tank: car_parts.Gas_Tank,
                 wheels: car_parts.Wheels):
        self.model_name = name
        self.engine = engine
        self.gas_tank = gas_tank
        self.wheels = wheels

    def __repr__(self):
        class_name = self.__class__.__name__
        model = self.model_name
        gas_tank = self.gas_tank.name
        wheels = self.wheels.name
        return f'{class_name}({model=}, {gas_tank=}, {wheels=})'

    def __str__(self):
        return f'[{self.model_name}:{self.get_max_speed()}]'

    def get_max_speed(self):
        return self.engine.power * (self.wheels.size * 0.2)

    @abstractmethod
    def get_acceleration(self):
        pass


class Car(BaseCar):
    def get_acceleration(self):
        return self.engine.horses * (self.wheels.size * 0.1)
