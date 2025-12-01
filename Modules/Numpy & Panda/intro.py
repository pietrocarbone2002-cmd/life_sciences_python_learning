'''
Task: Intro to NumPy and Pandas

Goal:
Learn the basics of NumPy and Pandas by working with DNA sequences represented in numerical form.

Description:
You will write a Python script that:
1. Creates a DNA sequence as a string.
2. Converts the DNA sequence into a NumPy array of integers, according to the encoding:
       A = 0
       C = 1
       G = 2
       T = 3
3. Computes basic statistics using NumPy:
       - Length of the sequence
       - Count of each nucleotide
       - GC-content (in %)
4. Creates a Pandas DataFrame with the following columns:
       - "Position" (index of each nucleotide)
       - "Base" (the original A/C/G/T)
       - "Numeric" (the encoded numeric value)
5. Prints the DataFrame.
6. Saves the DataFrame to a CSV file (e.g. "sequence_table.csv").

Rules:
- Use NumPy arrays for all numerical operations.
- Use Pandas for the table (DataFrame) part.
- The DNA sequence can be a hardcoded string (e.g. "ACGTTGCAACGT").

Bonus (optional):
- Use NumPy's vectorized operations to compute GC-content without loops.
- Plot the numeric sequence as a line plot using matplotlib.

Objective:
Understand how NumPy handles numerical arrays and how Pandas organizes biological data in table form.

'''
