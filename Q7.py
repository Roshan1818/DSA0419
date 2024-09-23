import pandas as pd
order_data = pd.DataFrame({
    'customer_id': [1, 2, 1, 3, 2, 1],
    'order_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', '2023-01-02', '2023-01-01']),
    'product_name': ['A', 'B', 'A', 'C', 'B', 'A'],
    'order_quantity': [1, 2, 1, 1, 3, 2]
})
total_orders = order_data['customer_id'].value_counts()
print("Total Orders by Customer:\n", total_orders)
average_quantity = order_data.groupby('product_name')['order_quantity'].mean()
print("\nAverage Order Quantity per Product:\n", average_quantity)
earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()
print(f"\nEarliest Order Date: {earliest_date}")
print(f"Latest Order Date: {latest_date}")
