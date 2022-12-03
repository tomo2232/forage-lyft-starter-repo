from abc import ABC, abstractmethod
from engine.engine import Engine
from battery.battery import Battery

from serviceable import Serviceable #unsure about this

class Car(Serviceable, ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery
