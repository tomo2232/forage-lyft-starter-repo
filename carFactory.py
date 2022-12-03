from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.splinder_battery import SplinderBattery
from battery.nubbin_battery import NubbinBattery

from car import Car

class CarFactory():
    def __init__(self) -> None:
        self.cars = []

    def create_calliope(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        car = Car(CapuletEngine, SplinderBattery)
        self.cars.append(car)
        return car

    def create_glissade(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        car = Car(WilloughbyEngine, SplinderBattery)
        self.cars.append(car)
        return car
    
    def create_palindrome(self, current_date: datetime, last_service_date: datetime, warning_light_on: bool) -> Car:
        car = Car(SternmanEngine, SplinderBattery)
        self.cars.append(car)
        return car
    
    def create_rorschach(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        car = Car(WilloughbyEngine, NubbinBattery)
        self.cars.append(car)
        return car
    
    def create_thovex(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        car = Car(CapuletEngine, NubbinBattery)
        self.cars.append(car)
        return car

