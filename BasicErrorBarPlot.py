import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[2,3,2,1,2,3]
y_error= 0.1
plt.plot(x,y)

plt.errorbar(x,y,yerr = y_error, fmt='o')
plt.show()
