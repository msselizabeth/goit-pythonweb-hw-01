import logging
from abc import ABC, abstractmethod

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s" 
)
logger = logging.getLogger(__name__)


# Abstarct Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self):
        pass


# Concrete classes
class Car(Vehicle):

    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Engine is launched.")


class Motorcycle(Vehicle):

    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Motor is launched.")


# Abstarct Factory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model, region):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model, region):
        pass


# Concrete factories
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU Spec")


# Use
if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("BMW", "R1250")
    vehicle2.start_engine()
