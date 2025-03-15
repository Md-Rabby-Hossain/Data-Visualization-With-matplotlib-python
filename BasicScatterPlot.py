import matplotlib.pyplot as plt 

a = [3,6,1,4,3,5,3,5,4,3,5,6,4,3,2,3]
b = [5,1,2,3,5,4,4,3,2,3,3,3,2,4,2,3]

plt.scatter(a, b)

plt.legend("Points")
plt.title("ScatterChart")
plt.xlabel('a')
plt.ylabel('b')
plt.show()
