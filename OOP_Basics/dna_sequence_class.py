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
#Define a class with methods
class DNA():
     
    #This connects the entered sequence with the methods 
    def __init__(self, seq):
        self.seq = str(seq)

    #This methods returns the length of a sequence
    def length(self):
        return len(self.seq)
        
    #This method calcualtes the content of G and C as a % of the whole sequence    
    def gc_content(self):
        g = self.seq.count("G")
        c = self.seq.count("C")
        return (((g+c)/len(self.seq)) * 100)
    
    #This method creates the complementary sequence (inverts the bases)
    def complement(self):
        comp_seq = self.seq.replace("A","X")    #First all As are "saved" in a placeholder
        comp_seq = comp_seq.replace("T", "A")   #All Ts are converted to As
        comp_seq = comp_seq.replace("X", "T")   #All saved As are converted to Ts
 
        comp_seq = comp_seq.replace("C", "Y")
        comp_seq = comp_seq.replace("G", "C")
        comp_seq = comp_seq.replace("Y", "G")
        return comp_seq
    
    #This method is similar to complement(), but creates a sequence in the reverse order
    def reverse_complement(self):
        rev_seq = self.seq[::-1]                #This reverses the sequence 3'-> 5' to 5'-> 3'
        comp_rev = rev_seq.replace("A", "X")    #Same game as per complement()
        comp_rev = comp_rev.replace("T", "A")
        comp_rev = comp_rev.replace("X", "T")

        comp_rev = comp_rev.replace("C", "Y")
        comp_rev = comp_rev.replace("G", "C")
        comp_rev = comp_rev.replace("Y", "G")
        return comp_rev
    
    #This method translates the DNA sequence into mRNA
    def transcribe(self):
        rna_seq = self.seq.replace("T", "U")
        return rna_seq

#First we define which characters are valid inputs
valid = {"A", "T", "G", "C"}

inp = input("Enter DNA Sequence: ")
sequence = inp.upper()
le = len(sequence)

#Then we scan if the sequence contains any invalid input
valid_seq = True

#This prevents the sequence fomr being empty
if le == 0:
    valid_seq = False 

#This scans through the whole sequence for invalid characters
else:
    for x in range(0, le):
        if sequence[x] not in valid or le == 0:
            valid_seq = False
            break

#Finally the infos are printed
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

#This message is printed if the sequence is invalid
else:
    print("Please enter a valid sequence!")

        
      
        
    

   