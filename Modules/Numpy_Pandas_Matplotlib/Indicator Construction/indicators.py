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
moving_sum = sum(data["Value"][:sl_length])
slow_ma_values.append(moving_sum/sl_length)
for i in range(len(data["Value"]) - sl_length):
    moving_sum += (data["Value"][i + sl_length] - data["Value"][i])
    slow_ma_values.append(moving_sum/sl_length)

slow_ma = nu.array(slow_ma_values)

data["Slow MA"] = slow_ma

print(data)
#Fast MA

fa_length = 5

#Plotting
ppl.plot(data["Time"], data["Value"], label = "Data")
ppl.show()
