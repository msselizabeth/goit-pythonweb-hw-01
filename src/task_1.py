import logging
from abc import ABC, abstractmethod

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


# Abstract Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str) -> None:
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Concrete classes
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region}): Engine is launched.")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region}): Motor is launched.")


# Abstract Vehicle Factory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


# Concrete factories
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


# Use
if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("BMW", "R1250")
    vehicle2.start_engine()
