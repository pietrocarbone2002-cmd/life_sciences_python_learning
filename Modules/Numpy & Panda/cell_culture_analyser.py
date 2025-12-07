'''
Create a Python program with a class `CellCultureAnalyzer` that models, analyzes, and visualizes batch cell culture growth.

1. The class should accept:
    - `time` (list or numpy array): time points in hours
    - `cell_count` (list or numpy array): viable cell count at each time point
    - Automatically convert them to NumPy arrays internally.

2. Implement the following methods:

    a. `growth_rate()`
       - Computes the exponential growth constant k using linear regression on log(cell_count).
       - Use NumPy to compute slope: 
         k = slope of log(cell_count) vs. time.

    b. `doubling_time()`
       - Computes doubling time td = ln(2) / k.

    c. `predict(n_hours)`
       - Returns predicted cell counts for a given number of hours into the future.
       - Uses the exponential model:
         N(t) = N0 * exp(k * t)

    d. `to_dataframe()`
       - Returns a Pandas DataFrame with:
         - Time
         - Cell Count
         - Log Cell Count
         - Predicted Cell Count (based on fitted model)
         - Error (%) = 100 - prediction/actual * 100

    e. `plot()`
       - Produces a MatPlotLib plot with:
         - Actual cell counts
         - Fitted exponential curve
         - Future prediction (optional dashed)

3. Input validation:
    - Raise an exception if time and cell_count have different lengths.
    - Raise an exception if any cell count ≤ 0.
    - Raise an exception if fewer than 3 data points (regression requires meaningful data).

4. In the main program:
    - Provide example data.
    - Instantiate `CellCultureAnalyzer`.
    - Print growth rate and doubling time.
    - Print the DataFrame.
    - Create a 48-hour future prediction.
    - Plot actual vs. predicted growth.

Goal:
Practice hybrid OOP + Numpy + Pandas + MatPlotLib design while working with a realistic biotech growth-modeling workflow.

'''
import numpy as nu
import pandas as pd
import matplotlib.pyplot as plt

class CellCultureAnalyser():

    def __init__ (self, time, cell_count):
        self.time = nu.array(time)
        self.cell_count = nu.array(cell_count)


    def growth_rate(self):
        k, a = nu.polyfit(self.time, self.cell_count, 1) 
        growth_rate = k
        return growth_rate
    
    def doubling_time(self):
        k, a = nu.polyfit(self.time, self.cell_count, 1) 
        growth_rate = k
        doubling_time = nu.log(self.cell_count) / growth_rate
        return doubling_time
    
    def predict(self, n_hours):
        k, a = nu.polyfit(self.time, self.cell_count, 1) 
        growth_rate = k
        prediction = self.cell_count[0] * nu.exp(growth_rate * n_hours)
        return prediction
    
    def to_dataframe(self):
        pass 