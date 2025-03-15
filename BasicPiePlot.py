import matplotlib.pyplot as plt  

a = [30, 10, 25, 15, 20]  
labels = ["Reading", "Walking", "Writing", "Thinking", "SocialMedia"]  # Labels for each slice  
e = (0.1, 0, 0.1, 0, 0)                                                 # Exploding top two slices  
  
plt.pie(a, labels=labels, explode=e, autopct='%1.1f%%', startangle=90)  # Creating the pie chart
plt.title("My Free Time") 
plt.show()
