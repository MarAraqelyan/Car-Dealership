from abc import ABC, abstractmethod
from customExceptions import NotInInventory

class SalesOperations(ABC):
    @abstractmethod
    def add_to_inventory(self, car):
        ...

    @abstractmethod
    def search_in_inventory(self, inventory, make , model):
        ...

    @abstractmethod
    def sell_car(self, car):
        ...



class SalesPerson(SalesOperations):
    def __init__(self, name, commision_rate, inventory):
        self.name = name
        self.commision_rate = commision_rate
        self.inventory = inventory
        self.sale_history = []
        
    def sell_car(self, car_make, car_model):
        if self.search_in_inventory(car_make, car_model):
            self.sale_history.append((car_make, car_model))
            return self.inventory.pop((car_make, car_model))
        
    def search_in_inventory(self, make, model):
        if car_and_price := self.inventory.get((make, model)):
            return car_and_price
        raise NotInInventory

    def add_to_inventory(self, car):
        self.inventory[(car.make, car.model)] = (car, car.price)

    def view_history(self):
        return self.sale_history