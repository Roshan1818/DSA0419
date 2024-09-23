import pandas as pd
order_data = pd.DataFrame({
    'product_name': ['A', 'B', 'A', 'C', 'B', 'A'],
    'order_quantity': [1, 2, 1, 1, 3, 2]
})
top_products = order_data.groupby('product_name')['order_quantity'].sum().nlargest(5)
print("Top 5 Products Sold:\n", top_products)
