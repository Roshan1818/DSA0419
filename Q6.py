def calculate_total_cost(item_prices, quantities, discount_rate, tax_rate):
    subtotal = sum(price * qty for price, qty in zip(item_prices, quantities))
    discount = subtotal * (discount_rate / 100)
    total_after_discount = subtotal - discount
    tax = total_after_discount * (tax_rate / 100)
    total_cost = total_after_discount + tax
    return total_cost
item_prices = [10.0, 20.0, 15.0]
quantities = [2, 3, 1]
discount_rate = 10 
tax_rate = 5 
total_cost = calculate_total_cost(item_prices, quantities, discount_rate, tax_rate)
print(f'Total Cost: ${total_cost:.2f}')
