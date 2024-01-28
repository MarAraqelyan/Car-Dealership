class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.car = None

    def purchase_car(self, car_make, car_model, sale_person):
        self.car = sale_person.sell_car(car_make, car_model)