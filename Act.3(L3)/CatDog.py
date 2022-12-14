# name: Villas, Justin Lawrence DL.
#lab: 3.2
#cource: cmpe30053
# -------------------------------------------------------------------------

class Animals:
    # purpose: initilize the variables to be used.
    # parameter:  animalName="Justin, the turtle"
    # return:    none
    def __init__(self, animalName="Justin, the turtle"):
        self.animalName = animalName
        print(f"An animal has been born.")

    # purpose: show an output "Munch, munch"
    # parameter: none
    # return:    none
    def eat(self):
        print("Munch, munch")

    # purpose: to make noice
    # parameter: none
    # return:    none
    def makeNoice(self):
        print(f"Grr says {self.animalName}.")


class Cat(Animals):
    # purpose: initilize the variables to be used.
    # parameter: animalName (Parent class)
    # return:    none

    def __init__(self, animalName):
        self.animalName = animalName
        print(f"{self.animalName}(the cat) has been born.")

    # purpose: to make noice "Meow"
    # parameter: none
    # return:    none
    def makeNoice(self):
        print(f"Meow says {self.animalName} the cat.")


class Dog(Animals):

    # purpose:  initilize the variables to be used.
    # parameter: animalName(Parent class)
    # return:    none
    def __init__(self, animalName):
        self.animalName = animalName
        print(f"{self.animalName}(the Dog) has been born.")

    # purpose:  to make the dog bark
    # parameter: none
    # return:    none
    def makeNoice(self):
        print(f"Bark says {self.animalName} (the dog).")

