from models import Car

car1 = Car("Toyota","444-555-66","Yellow")
car2 = Car("Ford","222-555-66")

car1.model = "Toyota Corolla"

print(car1)
car1.drive(5)
car2.drive(10)

