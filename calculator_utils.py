def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_fahrenheit(kelvin: float) -> float:
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))
