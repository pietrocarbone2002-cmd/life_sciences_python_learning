'''
Task: Cell Culture Growth Analysis Using NumPy and Pandas

Background:
In cell culture experiments, scientists often measure how a cell population grows over time.
A common metric is the "doubling time" – how long it takes for the cell count to double.

You are given time-series data of live cell counts (e.g., from a hemocytometer,
flow cytometer, or automated cell counter).

Your job:
1. Simulate or store the following experimental data in a Pandas DataFrame:

   Time (hours):     [0, 12, 24, 36, 48, 60, 72]
   Cell count:       [1.2e5, 1.8e5, 2.8e5, 4.0e5, 5.9e5, 8.9e5, 1.3e6]

2. Using NumPy, calculate the growth rate k using the exponential model:
       N(t) = N0 * e^(k * t)

   Solve for k using linearization (log-transform the counts).

3. Compute and print the "doubling time" (in hours):
       doubling_time = ln(2) / k

4. Add the following columns to your DataFrame:
     - "log_count"     (natural log of cell count)
     - "predicted"     (predicted cell number using your model)
     - "residuals"     (actual - predicted)

5. Plot the following using matplotlib:
     - Raw cell counts vs. time (scatter)
     - Fitted exponential curve (line)
     - Residuals vs. time

6. Save:
     - The DataFrame to "cell_growth.csv"
     - The growth plot as "growth_curve.png"
     - The residual plot as "residuals.png"

Bonus (optional):
- Compute the area under the curve (AUC) using the trapezoidal rule (numpy.trapz).
- Add measurement noise to the counts and repeat the fit.
- Create an OOP class "CellCulture" that computes growth parameters from data.

Goal:
Practice NumPy mathematical operations, Pandas table handling, curve fitting logic,
and biological data interpretation in a realistic biotech scenario.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

time_h = [0, 12, 24, 36, 48, 60, 72]
cell_count = [1.2e5, 1.8e5, 2.8e5, 4.0e5, 5.9e5, 8.9e5, 1.3e6]

#Panda Dataframe
dt = pd.DataFrame({
    "Time" : time_h,
    "Cell Count" : cell_count
})

#Calculate the growth-rate

log_cell_count = np.log(cell_count)          #this scales the list to a log-scale
k, a = np.polyfit(time_h, log_cell_count, 1) #This function means np.polyfit(x-values, y-values, degree). Degree = 1 is a linear regression

growth_rate = k
print(f'Growth Rate: {growth_rate}')
print("")

#Calculate doubling time

doubling_time = np.log(2) / growth_rate

print(f'Doubling Time: {doubling_time}')
print("")

#Add the new data to the Pandas Dataset
dt["Log-Count"] = log_cell_count

#Calculate prediction
n0 = cell_count[0]
time_h_numpy = np.array(time_h)
prediction = n0 * np.exp(k * time_h_numpy)

offset = 100 - (np.array(prediction) / np.array(cell_count)) * 100 

dt["Prediction"] = prediction
dt["Offset [%]"] = offset

print(dt)

#Matplot - plotting

plt.scatter(time_h, cell_count, label="Measured")
plt.plot(time_h, prediction, label="Predicted", color="red")
plt.legend()
plt.show()







