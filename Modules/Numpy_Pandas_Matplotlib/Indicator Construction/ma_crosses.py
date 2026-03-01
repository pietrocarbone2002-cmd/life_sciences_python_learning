import pandas as pd
import numpy as nu
import matplotlib.pyplot as ppl

#Data loading
data = pd.read_csv(r"Modules\Numpy_Pandas_Matplotlib\Indicator Construction\data.csv")
nu_data = data.to_numpy()
dataframe = pd.DataFrame(data)

#MAs -----------------------------------------------------------------------------------------
#Slow MA - Pandas Logik

sl_length = 10

data["Slow MA"] = (
    data["Value"]
    .rolling(window=sl_length)
    .mean()
)

slow_ma = nu.array(data["Slow MA"])
#Fast MA - Python Logik

fa_length = 3

#Create an empty list
fast_ma_values = []

#Scan the values in the dataset
for i in range(len(data["Value"])):

    #Append the data only after a complete window can be used for calculations
    if i >= fa_length - 1:
        #This makes the window roll
        moving_sum = sum(data["Value"][i - fa_length + 1:i + 1])
        fast_ma_values.append(moving_sum/fa_length)
    
    #Append "NaN" for the 
    else:
        fast_ma_values.append(nu.nan)

#Convert the list into an array
fast_ma = nu.array(fast_ma_values)

#Create a new column in the dataframe
data["Fast MA"] = fast_ma

#Signaling - MA Crossover -----------------------------------------------------------------------

signal = data["Fast MA"] - data["Slow MA"]
signal_prev = signal.shift(1) #shift() only works for Pandas! No Numpy Arrays

cross_up = (signal > 0)  &  (signal_prev <= 0)
data["Cross Up"] = cross_up

cross_down = (signal < 0)  &  (signal_prev >= 0)
data["Cross Down"] = cross_down

#Deviation Bands ----------------------------------------------------------------------------------

#Upperband = MA + k*STD

data["Upperband"] = data["Fast MA"] + 1 * (data["Value"].rolling(window=sl_length).std())
data["Upperband 2"] = data["Fast MA"] + 2 * (data["Value"].rolling(window=sl_length).std())
data["Upperband 3"] = data["Fast MA"] + 2.5 * (data["Value"].rolling(window=sl_length).std())

#Lowerband = MA - k*STD

data["Lowerband"] = data["Fast MA"] - 1 * (data["Value"].rolling(window=sl_length).std())
data["Lowerband 2"] = data["Fast MA"] - 2 * (data["Value"].rolling(window=sl_length).std())
data["Lowerband 3"] = data["Fast MA"] - 2.5 * (data["Value"].rolling(window=sl_length).std())

# #Upperband = MA + k*STD

# data["Upperband"] = data["Fast MA"] + 0.5 * (data["Value"].std())
# data["Upperband 2"] = data["Fast MA"] + 1 * (data["Value"].std())
# data["Upperband 3"] = data["Fast MA"] + 1.5 * (data["Value"].std())

# #Lowerband = MA - k*STD

# data["Lowerband"] = data["Fast MA"] - 0.5 * (data["Value"].std())
# data["Lowerband 2"] = data["Fast MA"] - 1 * (data["Value"].std())
# data["Lowerband 3"] = data["Fast MA"] - 1.5 * (data["Value"].std())


#Plotting -------------------------------------------------------------------------------------------

x = data["Time"]

ppl.plot(x, data["Value"], label = "Data")
ppl.plot(x, data["Slow MA"], color = "red", linewidth = 0.7)
ppl.plot(x, data["Fast MA"], color = "orange", linewidth = 0.7)

#Crossoversignal

for s in data.loc[data["Cross Up"], "Time"]:
    ppl.axvline(x=s, linewidth=0.5, color = "green", linestyle = "dashed")

for s in data.loc[data["Cross Down"], "Time"]:
    ppl.axvline(x=s, linewidth=0.5, color = "red", linestyle = "dashed")

#STD Bands
ppl.plot(data["Time"], data["Upperband"], color = "green", linewidth = 0.1)
ppl.plot(data["Time"], data["Lowerband"], color = "green", linewidth = 0.1)
ppl.fill_between(
    data["Time"],
    data["Lowerband"],
    data["Upperband"],
    alpha=0.05,
    color = "green"
)

ppl.plot(data["Time"], data["Upperband 2"], color = "orange", linewidth = 0.1)
ppl.plot(data["Time"], data["Lowerband 2"], color = "orange", linewidth = 0.1)
ppl.fill_between(
    data["Time"],
    data["Upperband"],
    data["Upperband 2"],
    alpha=0.05,
    color = "orange"
)
ppl.fill_between(
    data["Time"],
    data["Lowerband"],
    data["Lowerband 2"],
    alpha=0.05,
    color = "orange"
)
ppl.plot(data["Time"], data["Upperband 3"], color = "red", linewidth = 0.1)
ppl.plot(data["Time"], data["Lowerband 3"], color = "red", linewidth = 0.1)
ppl.fill_between(
    data["Time"],
    data["Upperband 2"],
    data["Upperband 3"],
    alpha=0.05,
    color = "red"
)
ppl.fill_between(
    data["Time"],
    data["Lowerband 2"],
    data["Lowerband 3"],
    alpha=0.05,
    color = "red"
)

ppl.xlabel("Time")
ppl.ylabel("Values")
ppl.legend()
ppl.show()
