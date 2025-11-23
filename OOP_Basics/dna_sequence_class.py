"""
Python OOP Exercise – DNA Sequence Class
----------------------------------------

Task:
You will implement a class that represents a DNA sequence and includes
basic bioinformatics functions.

Requirements:

1. Create a class called `DNA` with one attribute:
   - seq (a string containing the nucleotide sequence, e.g. "ATGCTATA")

2. Add the following methods:

   a. `length()`  
      Returns the length of the sequence.

   b. `gc_content()`  
      Returns the GC content as a percentage of the sequence.

   c. `complement()`  
      Returns the complementary DNA strand.
      (A <-> T, C <-> G)

   d. `reverse_complement()`  
      Returns the reverse-complement of the sequence.

   e. `transcribe()`  
      Returns the RNA transcript (replace 'T' with 'U').

3. Handle invalid input:
   - If the sequence contains characters other than A, T, C, G,
     print an error message or raise an exception.

4. At the bottom of your script, create 2–3 DNA objects.
   Demonstrate all methods and print the results.

Goal:
Learn to work with strings, biological logic, and OOP methods.
"""

class DNA():
     
    def __init__(self, seq):
        self.seq = str(seq)

    def length(self):
        return len(self.seq)
        
    def gc_content(self):
        g = self.seq.count("G")
        c = self.seq.count("C")
        return ((g+c/len(self.seq)) * 100)
   
    def complement(self):
        self.seq = self.seq.replace("A","X")
        self.seq = self.seq.replace("T", "A")
        self.seq = self.seq.replace("X", "T")
 
        self.seq = self.seq.replace("C", "Y")
        self.seq = self.seq.replace("G", "C")
        self.seq = self.seq.replace("Y", "G")
        return self.seq
    
    def reverse_complement(self):
        rev_seq = self.seq[::-1]
        comp_rev = rev_seq.replace("A", "X")
        comp_rev = comp_rev.replace("T", "A")
        comp_rev = comp_rev.replace("X", "T")

        comp_rev = comp_rev.replace("C", "Y")
        comp_rev = comp_rev.replace("G", "C")
        comp_rev = comp_rev.replace("Y", "G")
        return comp_rev
    
    def transcribe(self):
        rna_seq = self.seq.replace("T", "U")
        return rna_seq
        
      
        
    

   