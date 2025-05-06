from typing import Self
from abc import ABC, abstractmethod

from logger import logger


class Vehicle(ABC):
    """Abstract base class for any"""

    @abstractmethod
    def start_engine(self: Self):
        """Abstract basic function"""


class VehicleFactory(ABC):
    """Abstract vehicle factory class"""

    @abstractmethod
    def create_car(self: Self, make: str, model: str) -> Vehicle:
        """Abstract create car method"""

    @abstractmethod
    def create_motorcycle(self: Self, make: str, model: str) -> Vehicle:
        """Abstract create motorcycle method"""


class USVehicleFactory(VehicleFactory):
    """Implementation for US factory"""

    def __init__(self: Self):
        self.region = "US Spec"

    def create_car(self: Self, make: str, model: str) -> Vehicle:
        """Create a US car"""
        return Car(make, model, self.region)

    def create_motorcycle(self: Self, make: str, model: str) -> Vehicle:
        """Create a US motorcycle"""
        return Motorcycle(make, model, self.region)


class EUVehicleFactory(VehicleFactory):
    """Implementation for EU factory"""

    def __init__(self: Self):
        self.region = "EU Spec"

    def create_car(self: Self, make: str, model: str) -> Vehicle:
        """Create a EU car"""
        return Car(make, model, self.region)

    def create_motorcycle(self: Self, make: str, model: str) -> Vehicle:
        """Create a EU motorcycle"""
        return Motorcycle(make, model, self.region)


class Car(Vehicle):
    """Implementation car"""

    def __init__(self: Self, make: str, model: str, region: str):
        """
        Args:
            make (str): Manufacturer of the car.
            model (str): Model name of the car.
            region (str): Specification region (e.g., 'US Spec').
        """
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self: Self):
        """Simulate start engine"""
        logger(f"{self.make} {self.model} ({self.region}): Двигун запущено")


class Motorcycle(Vehicle):
    """Implementation motorcycle"""

    def __init__(self: Self, make: str, model: str, region: str):
        """
        Args:
            make (str): Manufacturer of the motorcycle.
            model (str): Model name of the motorcycle.
            region (str): Specification region (e.g., 'EU Spec').
        """
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self: Self):
        """Simulate start engine"""
        logger(f"{self.make} {self.model} ({self.region}): Мотор заведено")


# Using
factory1 = USVehicleFactory()
vehicle1 = factory1.create_car("Toyota", "Corolla")
vehicle1.start_engine()

factory2 = EUVehicleFactory()
vehicle2 = factory2.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
