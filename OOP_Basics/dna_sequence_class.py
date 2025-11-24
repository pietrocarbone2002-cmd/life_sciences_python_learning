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
        return (((g+c)/len(self.seq)) * 100)
   
    def complement(self):
        comp_seq = self.seq.replace("A","X")
        comp_seq = comp_seq.replace("T", "A")
        comp_seq = comp_seq.replace("X", "T")
 
        comp_seq = comp_seq.replace("C", "Y")
        comp_seq = comp_seq.replace("G", "C")
        comp_seq = comp_seq.replace("Y", "G")
        return comp_seq
    
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

valid = {"A", "T", "G", "C"}

inp = input("Enter DNA Sequence: ")
sequence = inp.upper()
le = len(sequence)

valid_seq = True

if le == 0:
    valid_seq = False
else:
    for x in range(0, le):
        if sequence[x] not in valid or le == 0:
            valid_seq = False
            break

if valid_seq:
    seq1 = DNA(sequence)
    print(f'''
          Entered Sequence: {sequence}
          Length: {seq1.length()}
          C and G %Content: {seq1.gc_content()}%
          Complement Sequence: {seq1.complement()}
          Reverse Complement: {seq1.reverse_complement()}
          mRNA Equivalent: {seq1.transcribe()}
          ''')
else:
    print("Please enter a valid sequence!")

        
      
        
    

   