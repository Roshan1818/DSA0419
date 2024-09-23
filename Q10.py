import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [100, 200, 150, 300]
plt.plot(months, sales)
plt.title('Monthly Sales (Line Plot)')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()
plt.bar(months, sales)
plt.title('Monthly Sales (Bar Plot)')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()
