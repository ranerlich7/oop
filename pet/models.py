class Pet:
    def __init__(self, name, age, image, animal_type):
        self.name = name
        self.age = age
        self.image = image
        self.animal_type = animal_type

    def __str__(self):
        return f"{self.animal_type}. The name is: {self.name}. The age is: {self.age}"

    def adopt(self, user):
        self.user = user
        print(f"{self.name} was adopted by:", user.name)
    
    def unadpot(self):
        print(f"{self.name} was returned by {self.user.name}")
        self.user = None
