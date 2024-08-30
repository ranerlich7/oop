from models import Car

car1 = Car("Toyota","444-555-66","Yellow")
car2 = Car("Ford","222-555-66")

car1.model = "Toyota Corolla"

car1.drive(15)
print("fuel is:", car1.fuel)
car1.drive(15)
print("fuel is:", car1.fuel)
car1.fueling(20)
print("final fuel is:", car1.fuel)
# print(car1)
# car2.drive(10)

car1.drive(10)

