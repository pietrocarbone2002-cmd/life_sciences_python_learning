# Python OOP Exercise – Protein Class
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