"""
Python OOP Exercise – Biotech Context
-------------------------------------

Task:
You will implement a simple object-oriented model of a biological cell.
This exercise introduces basic OOP concepts such as classes, attributes,
methods, and object behavior – but in a biotechnology context.

Requirements:

1. Create a class called `Cell` with the following instance attributes:
   - age (starts at 0)
   - max_age (value passed when creating the object)
   - alive (default: True)
   - cell_type (e.g. "animal", "plant", "bacterial")
   - organelles (an empty list on creation)

2. Add a method `age_one_day()` that:
   - increases the cell’s age by 1
   - automatically sets alive = False if age > max_age

3. Add a method `add_organelle(name)` that:
   - adds an organelle to the cell
   - prevents adding duplicates

4. Add a method `info()` that prints the current state of the cell
   (age, max_age, alive status, type, organelles)

5. Create several Cell objects (e.g., 3–5) and demonstrate:
   - aging the cells over several days
   - adding organelles
   - showing information about each cell

Goal:
Understand how to model real biological objects using classes and 
object-oriented programming fundamentals in Python.
"""
class Cell():
    
    def __init__ (self, max_age, cell_type):
        self.age = 0
        self.max_age = max_age
        self.alive = True
        self.cell_type = cell_type
        self.organelles = []
    
    def age_one_day(self):
        self.age = self.age + 1
        if self.age >= self.max_age:
            self.alive = False

    def add_organelle(self, name):
        name = input("Enter an organell")
        if name not in self.organelles:
            self.organelles.append(name)
        else:
            print("Organell already present!")
    

        
        



