#Import the required modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Here we create our DNA-Sequence

seq = "AGGCGGGCTAGAGAAATGCTA"
seq_list = list(seq)

encoding = {
    "A":0 ,
    "C":1 ,
    "G":2 ,
    "T":3
}

encoded_array = np.array([encoding[base] for base in seq])
#---------------- NUMPY ----------------

#Python Version: Length of the sequence
length = len(seq)

print(length)

#Numpy Version: Length of the sequence
length_numpy = np.size(seq_list)

print(length_numpy)
print("")
#---------------------------

#Python Version: Count each nucleotide
counts = {base: 0 for base in encoding.keys()}
for base in seq:
    counts[base] += 1

print(counts)

#Numpy Version: Count each nucleotide
unique, counts = np.unique(encoded_array, return_counts=True)
nucleotides_count = {base: int(count) for base, count in zip(encoding.keys(), counts)}

print(nucleotides_count)
print("")
#---------------------------

#GC-Content Python
gc = seq.count("G") + seq.count("C")
gc_percentage = ((gc)/len(seq)) * 100

print(f'{gc_percentage}%')

#GC-Content Numpy
gc_mask = np.isin(encoded_array, [1,2])
gc_percentage_numpy = gc_mask.mean() * 100

print(f'{gc_percentage_numpy}%')
print("")
#---------------- PANDAS ----------------

positions = np.arange(len(seq))

dataframe = pd.DataFrame({
    "Position":positions,
    "Base": seq_list,
    "Numeric": encoded_array
})

#dataframe.to_csv("sequence_table.csv", index=False)
print(dataframe)

#---------------- BONUS: MATPLOTLIB ----------------

plot = plt.plot(positions, encoded_array)
plt.show()
