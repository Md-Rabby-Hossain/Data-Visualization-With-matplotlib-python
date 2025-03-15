import matplotlib.pyplot as plt

a = [5,6,7,9]
b = [8,7,4,2]
c = [6,8,3,2]

plt.plot(a,b)
plt.plot(a,c)
plt.title('Line Graph')
plt.xlabel('a')
plt.ylabel('b & c')
plt.legend(['a vs b', 'a vs c'])
plt.show()
