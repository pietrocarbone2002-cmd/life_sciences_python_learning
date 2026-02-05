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

#Dropping missing pairs

dataframe = dataframe.dropna()
#print(dataframe)

#Outlier detection
outlier = 2.5

#Calculate the z-score
mean = dataframe["Measurements"].mean()
std = dataframe["Measurements"].std()

z_score = (dataframe["Measurements"] - mean)/std

#Create a new column with all z-scores
dataframe["Z-Score"] = z_score

#Create a new column which shows if the value is below or above the mean
mask_mean = dataframe["Measurements"] >= mean

dataframe["Above/Below the Mean"] = "Below"
dataframe.loc[mask_mean, "Above/Below the Mean"] = "Above"

print("")
print(dataframe)
print("")

mask = dataframe["Z-Score"] > outlier

print(f'''Outliers:
      {dataframe["Z-Score"].gt(outlier).sum()} outliers detected!
      Time: {dataframe[mask]["Time"].values}
      Outlier(s): {dataframe[mask]["Z-Score"].to_string(index=False)}
      Measurement(s): {dataframe[mask]["Measurements"].to_list()}''')

#.values returns the indices as values
#.to_string returns the indices as a string
#.to_list resturns the indices as a list

#Plotting
plt.scatter(time, measurement, color = "blue", label = "Data Points")

plt.legend()
plt.show()