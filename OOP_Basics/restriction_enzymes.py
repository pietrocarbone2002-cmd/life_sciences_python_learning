'''
Python OOP Exercise – Restriction Enzyme Simulator
--------------------------------------------------

Task:
You will implement a class that simulates DNA restriction enzymes,
including recognition-site scanning and DNA cutting.

Requirements:

1. Create a class called `RestrictionEnzyme` with the following attributes:
   - name (e.g. "EcoRI")
   - recognition_site (e.g. "GAATTC")
   - cut_position (integer indicating where the enzyme cuts relative
     to the recognition site, e.g. EcoRI cuts between G and A → cut_position = 1)

2. Add the following methods:

   a. `find_sites(dna_sequence)`
      Returns a list of start positions where the recognition site occurs
      in the given DNA sequence.

   b. `cut(dna_sequence)`
      Simulates cutting the DNA sequence at all recognition sites.
      Returns a list of DNA fragments created by the cuts.

   c. `__str__()`
      Returns a formatted string describing the enzyme, for example:
      "EcoRI (GAATTC), cuts after position 1".

3. Input validation:
   - The recognition_site must contain only A, T, C, G.
   - The dna_sequence passed into the methods must also contain only A, T, C, G.
   - cut_position must be within the recognition site's length.
   - On invalid input, raise an exception or print an error message.

4. Demonstration:
   At the bottom of the script, create at least two RestrictionEnzyme objects
   (e.g., EcoRI and BamHI). Provide a DNA sequence and:
   - Print all recognition site positions for each enzyme.
   - Print the resulting DNA fragments after cutting.
   - Print the enzyme description using the __str__() method.

Goal:
Learn how to combine OOP design, string-search logic, validation rules,
and sequence manipulation in a biologically realistic context.
'''

class RestictionEnzyme():
    
    def __init__(self, name, recognition_site, cut_position):
        self.name = name
        self.recognition_site = recognition_site
        self.cut_position = int(cut_position)
      
    def find_sites(self, dna_sequence):
        start_positions = []
        for x in range(0, len(dna_sequence) - len(self.recognition_site) + 1): #Scans for x in the dna_sequence until the last logical possibility
            if dna_sequence[x : x + len(self.recognition_site)] == self.recognition_site: #This compares the dna_sequence from x -> known length to the known site 
                start_positions.append(x)
        return start_positions
    
    def cut(self, dna_sequence):
        dna_fragments = []
        for x in range(0, len(dna_sequence) - len(self.recognition_site) + 1):
            if dna_sequence[x : x + len(self.recognition_site)] == self.recognition_site:
                