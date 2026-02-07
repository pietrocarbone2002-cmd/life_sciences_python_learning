import pandas as pd
import numpy as nu
import matplotlib.pyplot as ppl

#Data loading
data = pd.read_csv(r"Modules\Numpy_Pandas_Matplotlib\Indicator Construction\data.csv")
nu_data = data.to_numpy()
dataframe = pd.DataFrame(data)

#MAs
#Slow MA - Pandas Logik

sl_length = 10

data["Slow MA"] = (
    data["Value"]
    .rolling(window=sl_length)
    .mean()
)

#Fast MA - Python Logik

fa_length = 4

fast_ma_values = []

for i in range(len(data["Value"])):
    if i >= fa_length - 1:
        moving_sum2 = sum(data["Value"][i - fa_length + 1:i + 1])
        fast_ma_values.append(moving_sum2/fa_length)
    else:
        fast_ma_values.append(nu.nan)

fast_ma = nu.array(fast_ma_values)
data["Fast MA"] = fast_ma

#Plotting
ppl.plot(data["Time"], data["Value"], label = "Data")
ppl.plot(data["Time"], data["Slow MA"], color = "red")
ppl.plot(data["Time"], data["Fast MA"], color = "orange")
ppl.show()
