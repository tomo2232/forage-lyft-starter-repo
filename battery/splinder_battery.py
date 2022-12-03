from abc import ABC, abstractmethod
from datetime import datetime

from battery.battery import Battery

class SplinderBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        # super().__init__(last_service_date, current_date)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False

