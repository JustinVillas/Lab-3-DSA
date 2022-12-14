from CatDog import Animals
from CatDog import Cat
from CatDog import Dog

lines = "==================================================="
print(f"{lines},\n")
pet1 = Animals()
pet1.eat()
pet1.makeNoice()

print(f"{lines},\n")
pet2 = Cat("Asley")
pet2.eat()
pet2.makeNoice()

print(f"{lines},\n")
pet3 = Dog("Shinny")
pet3.eat()
pet3.makeNoice()

print(f"{lines},\n")
pet3 = Dog("Rio")
pet3.eat()
pet3.makeNoice()
print(f"{lines},\n")
"================================================================="
