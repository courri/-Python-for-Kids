import copy

class Animal:
    def __init__(self, name, number_of_legs, color):
        self.name = name
        self.number_of_legs = number_of_legs
        self.color = color

harry = Animal('hippogriff', 6, 'pink')
harriet = copy.copy(animal_1)
print(harry.name)
print(harriet.name)