import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Selbststudium/ML Learning/linear_regression_sample.csv", delimiter=",")

#Gradient Descent to adjust the regression
def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    n = len(points)

    for i in range(n):
        x = points.iloc[i]["x_values"]
        y = points.iloc[i]["y_values"]

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L

    return m, b

m = 0
b = 0
L = 0.0001
epochs = 400
rounding = 3

for i in range(epochs):
    m, b = gradient_descent(m, b, data, L)
    if i % 50 == 0:
        print(f"Epoch: {i}")

print(m, b)

plt.scatter(data["x_values"], data["y_values"], color="black", label = "Raw Data")
plt.plot(list(range(0, 100)), [m * x + b for x in range(0, 100)], color = "red", label = f"Linear Regression: y = {round(m,rounding)}x + {round(b,rounding)}")
plt.title("Example Linear Regression", weight = "bold")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

