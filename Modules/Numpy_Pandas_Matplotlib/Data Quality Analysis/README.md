# Exercise: Experimental Data Quality Analysis with NumPy & Pandas
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

--------------------------------------------------
Goal:
Learn how NumPy and Pandas are used together in real-world scientific data analysis,
including inspection, cleaning, transformation, and basic statistical reasoning.

This exercise focuses on thinking in arrays and tables rather than loops.