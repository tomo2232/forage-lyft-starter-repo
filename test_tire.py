import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tyres = [0.7, 0.8, 0.95, 0.5]
        tyre = CarriganTire(tyres)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        tyres = [0.7, 0.8, 0.8, 0.5]
        tyre = CarriganTire(tyres)
        self.assertFalse(tyre.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tyres = [0.7, 0.8, 0.9, 0.8]
        tyre = OctoprimeTire(tyres)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        tyres = [0.1, 0.9, 0.9, 0.1]
        tyre = OctoprimeTire(tyres)
        self.assertFalse(tyre.needs_service())


if __name__ == '__main__':
    unittest.main()