'''
Exercise: Experimental Data Quality Analysis with NumPy & Pandas
----------------------------------------------------------------

Context:
You are given experimental measurement data from a biotechnology process.
The data contains time points and measured values, but also includes noise,
outliers, and missing values.

Your task is to explore NumPy and Pandas tools to clean, analyze, and summarize
the data in a realistic scientific workflow.

You are NOT required to use OOP in this exercise.

--------------------------------------------------
Part 1 — Create the raw dataset
--------------------------------------------------

1. Create a Pandas DataFrame with the following columns:
   - "Time" (hours): numeric
   - "Measurement": numeric

2. The dataset should include:
   - At least 15–20 rows
   - Some missing values (NaN)
   - At least one obvious outlier
   - Non-uniform time intervals

--------------------------------------------------
Part 2 — Data inspection
--------------------------------------------------

3. Use Pandas to:
   - Display the first and last rows
   - Show basic summary statistics
   - Identify missing values per column
   - Identify min, max, mean, and median

--------------------------------------------------
Part 3 — Data cleaning
--------------------------------------------------

4. Handle missing values using at least one strategy:
   - Removal
   - Forward fill
   - Mean/median replacement

5. Detect outliers using a statistical method:
   - Standard deviation
   - Interquartile range (IQR)

6. Remove or flag outliers.

--------------------------------------------------
Part 4 — NumPy-based analysis
--------------------------------------------------

7. Convert the cleaned measurement column to a NumPy array.

8. Compute:
   - Mean
   - Standard deviation
   - Normalized values (z-score)

9. Create a NumPy boolean mask that identifies values above the mean.

--------------------------------------------------
Part 5 — Pandas transformations
--------------------------------------------------

10. Add new columns to the DataFrame:
    - "Deviation" (value − mean)
    - "Above_Mean" (True / False)

11. Sort the DataFrame by measurement value.

--------------------------------------------------
Part 6 — Visualization (optional but recommended)
--------------------------------------------------

12. Create at least one plot using Matplotlib:
    - Measurement vs. Time
    - Highlight cleaned data vs. removed outliers

--------------------------------------------------
Goal:
Learn how NumPy and Pandas are used together in real-world scientific data analysis,
including inspection, cleaning, transformation, and basic statistical reasoning.

This exercise focuses on thinking in arrays and tables rather than loops.
'''

import numpy as nu
import pandas as pd
import matplotlib.pyplot as plt

#Datasets and Dataframe

time = [
    0, 2, 5, 9, 12, 15, 18, 22, 25, 28,
    32, 36, 40, 45, 50, 55, 60, 66, 72
]

measurement = [
    1.02, 1.05, 1.10, None, 1.25, 1.30, 1.28,
    1.35, 1.40, 4.90, 1.45, None, 1.55,
    1.60, 1.62, 1.65, 1.70, 1.72, 1.75
]

dataframe = pd.DataFrame({
    "Time" : time,
    "Measurements" : measurement
})

# print(dataframe)
# print("")

#Data Inspection

print(f'''First Row Dataframe:
      {dataframe.head(n=1)}''')

print(f'''Last Row Dataframe:
      {dataframe.tail(n=1)}''')

print(f'''Basic Summary Statistics:
      {dataframe.describe(
         include = dataframe["Measurements"].count()
      )}
      ''')

print(f'''Missing Values:
      Time:          {dataframe["Time"].isna().sum()} missing values out of {dataframe["Time"].count() + dataframe["Time"].isna().sum()}.
      Measurements:  {dataframe["Measurements"].isna().sum()} missing values out of {dataframe["Measurements"].count() + dataframe["Measurements"].isna().sum()}.''')

#Data Cleaning

#Idea 1 (good for research): implement a numpy regression and fill the None values with a plausible integer
#Idea 2 (good for GMP): remove data pairs where a value is attributed to None

if None in dataframe["Time"]:
    #Fill for Idea 1 or cut for Idea 2

if None in dataframe["Measurements"]:
    #Fill for Idea 1 or cut for Idea 2


