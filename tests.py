    
from pet.models import Pet
from user.models import User

pet1 = Pet("Dixie",8,"https://t4.ftcdn.net/jpg/01/99/00/79/360_F_199007925_NolyRdRrdYqUAGdVZV38P4WX8pYfBaRP.jpg","Dog")
pet2 = Pet("Mitzi",2,"https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg","Cat")

user1 = User("Ran","051-5355555")
user2 = User("Tal","058-5555566")

pet1.adopt(user1)
pet1.unadpot()

print("the end")


# pet2.age = 3
# pet2.name = "Bobby"

# print(pet1)
# print(pet2)
