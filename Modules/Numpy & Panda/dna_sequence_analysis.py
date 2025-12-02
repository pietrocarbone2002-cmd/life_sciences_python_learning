'''
Task: Advanced DNA Sequence Analysis with NumPy and Pandas

You are given a DNA sequence (string of A, C, G, T).  
Write a Python script that performs the following:

1. Encode the sequence numerically using NumPy:
   - A → 0, C → 1, G → 2, T → 3

2. Compute the following using vectorized NumPy operations (no loops):
   - GC content (%)
   - AT content (%)
   - The proportion of each nucleotide (A, C, G, T)

3. Create sliding windows (size 5 and size 10) and compute:
   - GC content *inside each window*
   - Store results as NumPy arrays

4. Build a Pandas DataFrame with:
   - "Position" (index)
   - "Base"
   - "Numeric"
   - "GC_Window5"
   - "GC_Window10"

5. Print the head() of the DataFrame.

6. Save the DataFrame to a CSV file.

Bonus:
- Plot the sliding-window GC content using matplotlib.
- Try adding a column with cumulative GC content using np.cumsum().

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

