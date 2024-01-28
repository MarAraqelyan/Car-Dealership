from abc import ABC, abstractmethod


class ICar(ABC):
    @abstractmethod
    def fuel_type(self):
        ...


class ElectricCar(ICar):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
    
    def fuel_type(self):
        return "Electric"
    


class HybridCar(ICar):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def fuel_type(self):
        return "Gasoline"
    

