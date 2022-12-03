from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, worn_values):
        self.worn_values = worn_values

    def needs_service(self):
        if sum(self.worn_values) > 3:
            return True
        return False
