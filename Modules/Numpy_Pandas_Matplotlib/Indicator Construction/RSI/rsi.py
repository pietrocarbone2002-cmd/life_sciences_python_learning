import numpy as np
import pandas as pd
import matplotlib.pyplot as ppl

data = pd.read_csv(r"Modules\Numpy_Pandas_Matplotlib\Indicator Construction\RSI\stationarity_test_data.csv")

#Data Inspection ---------------------------------------------------------------------

#Visual Test
ppl.plot(data["Time"], data["Value"])
ppl.show()

#Statistical Test