import pandas as pd
import matplotlib.pyplot as plt
import os

print(os.getcwd())
print("Current directory: " + os.getcwd())   #Current directory

data = pd.read_csv('TempHumidity.csv')       #load the CSV file

plt.plot(data.created_at, data.Temperature)
plt.plot(data.created_at, data.Humidity)
plt.title('Temp and Humidity visualization')
plt.xlabel('Time')
plt.ylabel('Temp & Humidity')
plt.legend(['Temperature', 'Humidity'])
plt.show()
