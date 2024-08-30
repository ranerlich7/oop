class Car:  
    def __init__(self, model, number, color="Black", fuel=50):
        self.model = model
        self.number = number
        self.color = color
        self.fuel = fuel
        print("starting a new car")

    def __str__(self):
        return f'model:{self.model}'

    def drive(self, fuel_consumption):
        print("driving....fuel consumption:",fuel_consumption)
        self.fuel = self.fuel - fuel_consumption
        print("fuel left:", self.fuel)
        
