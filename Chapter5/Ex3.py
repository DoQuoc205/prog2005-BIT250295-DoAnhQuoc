import matplotlib.pyplot as plt
products = ['A', 'B', 'C', 'D', 'E']
sales = [30, 25, 15, 20, 10]

plt.figure(figsize=(6,6))
plt.pie(sales, labels=products, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Tỷ lệ doanh số các sản phẩm')
plt.show()