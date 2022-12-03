from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, worn_values):
        self.worn_values = worn_values

    def needs_service(self):
        for tire in self.worn_values:
            if tire > 0.9:
                return True
        return False
