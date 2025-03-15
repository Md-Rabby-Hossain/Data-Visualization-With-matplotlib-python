import matplotlib.pyplot as plt
x=[1,2,3]
y=[7,5,6]
z=[5,2,8]
fig = plt.figure()

ax = plt.axes(projection='3d')
ax.plot3D(z,y,x)
plt.show()