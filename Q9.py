import pandas as pd
property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4],
    'location': ['CityA', 'CityB', 'CityA', 'CityB'],
    'number_of_bedrooms': [3, 5, 4, 6],
    'area_in_sqft': [1500, 2000, 1800, 2200],
    'listing_price': [300000, 400000, 350000, 500000]
})
average_price = property_data.groupby('location')['listing_price'].mean()
print("Average Listing Price by Location:\n", average_price)
properties_with_five_plus_bedrooms = property_data[property_data['number_of_bedrooms'] > 4].shape[0]
print(f"\nNumber of Properties with More than 4 Bedrooms: {properties_with_five_plus_bedrooms}")
largest_property = property_data.loc[property_data['area_in_sqft'].idxmax()]
print("\nProperty with the Largest Area:\n", largest_property)
