import matplotlib.pyplot as plt 
a = [5,7,8,4,9,9] 
b = [1,2,3,4,5,6] 

plt.bar(a, b)

plt.title("BarChart")
plt.xlabel("a")
plt.ylabel("b")
plt.legend(["Bar"])
plt.show()
