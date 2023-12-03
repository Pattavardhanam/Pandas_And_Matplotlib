import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {'X': np.arange(1, 11),
        'Y1': np.random.rand(10) * 10,  # Random values for line graph
        'Y2': np.random.randint(5, 15, 10)}  # Random values for bar graph

df = pd.DataFrame(data)

# Line Graph
plt.figure(figsize=(8, 5))
plt.plot(df['X'], df['Y1'], marker='o', label='Line Graph')
plt.title('Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

# Bar Graph
plt.figure(figsize=(8, 5))
plt.bar(df['X'], df['Y2'], color='skyblue', label='Bar Graph')
plt.title('Bar Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(df['X'], df['Y1'], color='green', label='Scatter Plot')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
