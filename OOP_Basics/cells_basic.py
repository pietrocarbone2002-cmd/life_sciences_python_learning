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
#Create the OOP logic
class Cell():
    
    #Here we create the blueprints of the attributes. 
    def __init__ (self, max_age, cell_type): #only max_age and cell_type are user attributes
        self.age = 0                         #All cells start from 0
        self.max_age = max_age
        self.alive = True                    #All cells are initially alive
        self.cell_type = cell_type
        self.organelles = []                 #Organelles are entered later
    
    #This function makes the cell age by 1. And also switches the viability
    def age_one_day(self):
        self.age = self.age + 1
        if self.age >= self.max_age:
            self.alive = False

   #Here we create the function to add the organelles to self.organelles
    def add_organelle(self, name):
        if name not in self.organelles:
            self.organelles.append(name)
        else:
            print("Organelle already present!")

   #This function is used to display our results
    def info(self):
         print(f'''Cell Infos:
               Age: {self.age},
               Maximal Age: {self.max_age},
               Alive? {self.alive},
               Cell Type: {self.cell_type},
               Organelles: {self.organelles}''')
    
# --- Simple demonstration of the Cell class ---

# Create a few example cells
cell1 = Cell(10, "animal") #the first argument is the max_age and the second the cell_type
cell2 = Cell(15, "plant")
cell3 = Cell(5, "bacterial")

# Add some organelles
cell1.add_organelle("Mitochondria")
cell1.add_organelle("Nucleus")

cell2.add_organelle("Chloroplast")

cell3.add_organelle("Ribosome")

# Age the cells a little
cell1.age_one_day()
cell1.age_one_day()

cell3.age_one_day()

# Show info for each cell
cell1.info()
cell2.info()
cell3.info()
        
        



