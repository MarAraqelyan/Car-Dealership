import inventory
import salespeople
import customers
import cars

carInventory = inventory.Inventory()

car1 = cars.HybridCar(make = "Honda", model = "Civic", price = "$22000")
car2 = cars.ElectricCar(make = "Nissan", model = "Leaf", price = "$31000")



sale_person = salespeople.SalesPerson("Bob", 25, carInventory.car_inventory)

sale_person.add_to_inventory(car1)
sale_person.add_to_inventory(car2)

customer1 = customers.Customer("Emma", "077-777-777")

customer1.purchase_car("Honda", "Civic", sale_person)

print(sale_person.view_history())

customer1.purchase_car("Honda", "Pilot", sale_person)