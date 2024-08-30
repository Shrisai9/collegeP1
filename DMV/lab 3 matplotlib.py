import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot data
x_line = x
y_line = y

# Scatter plot data
x_scatter = x
y_scatter = y + np.random.normal(0, 0.1, size=x.shape)

# Histogram data
data_hist = np.random.randn(1000)
