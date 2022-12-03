from abc import ABC, abstractmethod
from datetime import datetime


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
    
    # def needs_service(self):
    #     service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
    #     if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
    #         return True
    #     else:
    #         return False
