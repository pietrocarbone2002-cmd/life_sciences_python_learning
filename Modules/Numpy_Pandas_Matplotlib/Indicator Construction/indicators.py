import pandas as pd
import numpy as nu
import matplotlib.pyplot as ppl

#Data loading
data = pd.read_csv(r"Modules\Numpy_Pandas_Matplotlib\Indicator Construction\data.csv")
nu_data = data.to_numpy()
dataframe = pd.DataFrame(data)

#MAs
#Slow MA

sl_length = 10

slow_ma_values = []

for i in range(len(data["Value"])):
    if i > sl_length - 1:
        moving_sum = sum(data["Value"][:sl_length])
        slow_ma_values.append(moving_sum/sl_length)
    else:
        slow_ma_values.append(nu.nan)

slow_ma = nu.array(slow_ma_values)

data["Slow MA"] = slow_ma

#Fast MA

fa_length = 5

fast_ma_values = []

for i in range(len(data["Value"])):
    if i > fa_length - 1:
        moving_sum2 = sum(data["Value"][:fa_length])
        fast_ma_values.append(moving_sum2/fa_length)
    else:
        fast_ma_values.append(nu.nan)

fast_ma = nu.array(fast_ma_values)

data["Fast MA"] = fast_ma

print(data)

#Plotting
ppl.plot(data["Time"], data["Value"], label = "Data")
ppl.plot(data["Time"], data["Slow MA"], color = "red")
ppl.plot(data["Time"], data["Slow MA"], color = "orange")
ppl.show()
