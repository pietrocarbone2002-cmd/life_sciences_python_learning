'''
Python OOP Exercise – Protein Class
-----------------------------------

Task:
Implement a Python class that models a protein sequence and provides 
basic structural and biochemical calculations.

Requirements:

1. Create a class called `Protein` with one attribute:
   - `seq` (a string containing the amino-acid sequence in one-letter code,
      e.g. "MKTFFVIL")

2. Add the following methods:

   a. `length()`
      Returns the length of the protein sequence.

   b. `molecular_weight()`
      Computes the molecular weight (in Daltons) using the
      average residue masses (you must define a dictionary of 
      amino-acid masses inside the class).

   c. `aa_composition()`
      Returns a dictionary showing how many times each amino acid occurs.

   d. `hydrophobic_fraction()`
      Returns the fraction (0–1) of hydrophobic residues.
      Consider the following amino acids hydrophobic:
      A, V, I, L, M, F, W, Y

   e. `to_fasta(header)`
      Returns a FASTA-formatted string:
          >header
          SEQUENCE

3. Handle invalid input:
   - If the sequence contains characters outside the 20 standard amino acids,
     raise an exception or print an error message.

4. At the bottom of your script:
   - Create 2–3 `Protein` objects.
   - Demonstrate all methods and print the results.

Goal:
Learn to work with dictionaries, biochemical rules, sequence logic,
and object-oriented design
'''

class Protein():

    #This dictionary contains all relevant information
    amino_acids_FASTA_code = {
      "A":{"name":"Alanine"        , "mass": 89.09   },
      "R":{"name":"Arginine"       , "mass": 174.20  },
      "N":{"name":"Asparagine"     , "mass": 132.12  },
      "D":{"name":"Aspartic Acid"  , "mass": 133.10  },
      "C":{"name":"Cysteine"       , "mass": 121.15  },
      "E":{"name":"Glutamic Acid"  , "mass": 147.13  },
      "Q":{"name":"Glutamine"      , "mass": 146.15  },
      "G":{"name":"Glycine"        , "mass": 75.07   },
      "H":{"name":"Histidine"      , "mass": 155.16  },
      "I":{"name":"Isoleucine"     , "mass": 131.17  },
      "L":{"name":"Leucine"        , "mass": 131.17  },
      "K":{"name":"Lysine"         , "mass": 146.19  },
      "M":{"name":"Methiodine"     , "mass": 149.21  },
      "F":{"name":"Phenylalanine"  , "mass": 165.19  },
      "P":{"name":"Proline"        , "mass": 115.13  },
      "S":{"name":"Serine"         , "mass": 105.09  },
      "T":{"name":"Threonine"      , "mass": 119.12  },
      "W":{"name":"Tryptophan"     , "mass": 204.23  },
      "Y":{"name":"Tyrosine"       , "mass": 181.19  },
      "V":{"name":"Valine"         , "mass": 117.15  },
    }

    #The __init__ method itself checks fir input-validity
    def __init__(self, seq):
        self.seq = seq
        valid = set(self.amino_acids_FASTA_code)
        if not set(self.seq).issubset(valid):       #If the sequence contains characters outside the dictionary
            raise ValueError("Sequence invalid!")    #An error message gets printed

    #This methos simply returns the length of the sequence
    def length(self):
        return len(self.seq)
    
    #This method returns the total weigth in Dalton
    def molecular_weigth(self):
        total = 0
        for aa in self.seq:
            mass = self.amino_acids_FASTA_code[aa]["mass"] #The mass is extracted from the dictionary
            total = total + mass
        return total
    
    #This method returns how many times an amino-acid is present in the sequence
    def aa_composition(self):
        composition = {}
        for aa in self.amino_acids_FASTA_code:
            count = self.seq.count(aa)
            composition[aa] = count
        return composition
    
    #This method calculates the %-content of hydrophobis amino-acids
    def hydrophobic_fraction(self):
        hydro = {"A", "V", "I", "L", "M", "F", "W", "Y"} #Check-tuple
        count = 0
        for aa in self.seq:
            if aa in hydro:
                count = count + 1
        fraction = count / len(self.seq)
        return fraction
    
    #This method returns the sequence in the FASTA format
    def to_fasta(self, header):
        return(f'''
              >{header}
              {self.seq}
              ''')

#Object examples

seq1 = Protein("AAAVCGK")
print(seq1.aa_composition())
print(seq1.hydrophobic_fraction())
print(seq1.molecular_weigth())
print(seq1.to_fasta(header="My seq"))