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

        #Validator Array Length

        if nu.size(self.time) != nu.size(self.cell_count):
            raise ValueError(''' Invalid Data Entered:
                             Time and Cell Count must be of equal length!
                             ''')
        
        #Validator Cell Count
        for a in self.cell_count:
            if a <= 0:
                raise ValueError('''Invalid Data Entered:
                                 Cell Count cannot be 0!
                                 ''')
        
        #Validator Array minimal size

        if nu.size(self.time) <= 3 or nu.size(self.cell_count) <= 3:
            raise ValueError('''Invalid Data Entered!
                             Data Set size must be larger than 3 data points!
                             ''')

    def growth_rate(self):
        k, a = nu.polyfit(self.time, self.cell_count, 1) 
        return k
    
    def doubling_time(self):
        k = self.growth_rate() 
        doubling_time = nu.log(self.cell_count) / k
        return doubling_time
    
    def predict(self, n_hours):
        k = self.growth_rate()
        prediction = self.cell_count[0] * nu.exp(k * n_hours)
        return prediction
    
    def to_dataframe(self):
        dt = pd.DataFrame({
            "Time" : self.time,
            "Cell Count" : self.cell_count,
            "Log Count" : nu.log(self.cell_count),
            "Prediction" : self.predict(),
            "Error [%]" : 100 - (nu.array(self.rediction) / nu.array(self.cell_count)) * 100 
        })
        return dt
    
    def plot(self, future_h):

        plt.scatter(self.time, self.cell_count, color="blue", label="Cell Count")

        N0 = self.cell_count[0]
        k = self.growth_rate()
        t_future = nu.linspace(self.time.max(), self.time.max() + future_h, 200)
        future_curve = N0 * nu.exp(k * t_future)

        t_fit = nu.linspace(self.time.min(), self.time.max(), 200)
        fit_curve = N0 * nu.exp(k * t_fit)

        plt.plot(t_fit, fit_curve, color="green", label="Fit Curve")
        plt.plot(t_future, future_curve, "--", label="Future Prediction")
        
        plt.legend()
        plt.show()
