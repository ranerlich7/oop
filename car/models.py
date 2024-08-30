class Car:  
    def __init__(self, model, number, color="Black", fuel=50, full_tank=50):
        self.model = model
        self.number = number
        self.color = color
        self.fuel = fuel
        self.full_tank = full_tank
        print("starting a new car")

    def __str__(self):
        return f'model:{self.model}'

    # def drive(self, kilometer):
    #     fuel_c = kilometer / 10
    #     self.fuel = self.fuel - fuel_c

    def drive(self, fuel_consumption):
        # print("driving....fuel consumption:",fuel_consumption)
        if (self.fuel - fuel_consumption) < 0:
            print("you cannot drive so far!!!")
            return
        self.fuel = self.fuel - fuel_consumption
        # print("fuel left:", self.fuel)

    def fueling(self, fuel_amount=-1):
        if fuel_amount == -1:
            self.fuel_amount = self.full_tank
        else:
            self.fuel = self.fuel + fuel_amount
        # print('After fueling. fule is', self.fuel)

