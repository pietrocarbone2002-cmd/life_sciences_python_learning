import numpy as np
import pandas as pd
import matplotlib.pyplot as ppl

data = pd.read_csv(r"Modules\Numpy_Pandas_Matplotlib\Indicator Construction\RSI\stationarity_test_data.csv")

#Data Inspection ---------------------------------------------------------------------

#Visual Test
# ppl.plot(data["Time"], data["Value"])
# ppl.show()

#Statistical Test - ADF

#RSI = 100 - 100/(1+RS)
#RS = +dy/-dy
data["RoC"] = [
    result - (result-1) for result in (data["Value"] - data["Value"])
]

#Create the positive RoC for the numerator
data["+ ROC"] = [
    pos for pos in data["RoC"] if pos >= 0.
    ]

#Create the negative RoC for the denominator
data["- ROC"] = [
    neg for neg in data["RoC"] if neg <= 0.
    ]

print(data)