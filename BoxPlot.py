import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data = np.random.normal(100,20,90)

fig = plt.figure(figsize = (10,50))

plt.boxplot(data)
plt.show()