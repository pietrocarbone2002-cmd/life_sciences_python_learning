'''
Module: loaders.py — Data Input Handling for Cell Culture Analysis
------------------------------------------------------------------

Purpose:
This module is responsible for loading cell culture growth data from different file formats
and converting them into a standardized format that can be used by the CellCultureAnalyzer.

The goal is to separate data input / parsing logic from analysis logic.

Requirements:

1. Implement one or more loader functions that read experimental data and return:
   - time (array-like, numeric)
   - cell_count (array-like, numeric)

2. Supported input formats:

   a. CSV files
      - Use pandas to read the file.
      - The file is expected to contain at least two columns:
        "time" and "cell_count".
      - Return the two columns as NumPy arrays or Python lists.

   b. TXT files
      - Assume a simple delimiter-based format (e.g. comma or tab).
      - Use either pandas or built-in file reading.
      - Convert the data into numeric arrays.

3. Input validation:
   - Raise an exception if required columns are missing.
   - Raise an exception if non-numeric values are encountered.
   - Raise an exception if the file is empty or malformed.

4. Design constraints:
   - This module must NOT perform any biological analysis.
   - This module must NOT plot data.
   - This module must NOT instantiate CellCultureAnalyzer.
   - Its sole responsibility is data loading and basic validation.

5. Output contract:
   - All loader functions must return data in the same format:
     (time, cell_count)

6. Example usage (conceptual, not code to copy):
   - time, cell_count = load_from_csv("experiment.csv")
   - analyzer = CellCultureAnalyzer(time, cell_count)

Goal:
Build a clean and extensible data-loading layer that allows the analysis code
to remain independent of file formats and input sources.

This module should make it easy to add new data formats in the future
without modifying the core analysis logic.
'''

