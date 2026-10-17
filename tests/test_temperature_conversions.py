import unittest

from calculator_utils import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
)


class TemperatureConversionTests(unittest.TestCase):
    def test_celsius_and_fahrenheit(self) -> None:
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)

    def test_celsius_and_kelvin(self) -> None:
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)

    def test_fahrenheit_and_kelvin(self) -> None:
        self.assertAlmostEqual(fahrenheit_to_kelvin(32), 273.15)
        self.assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32)


if __name__ == "__main__":
    unittest.main()
