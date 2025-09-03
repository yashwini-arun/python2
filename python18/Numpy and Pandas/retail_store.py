import pandas as pd 
import numpy as np 


data = {
    'Product': ['Shoes', 'Shirt', 'Watch', 'Shoes', 'Shirt', 'Watch'],
    'Units': [10, 8, 5, 6, 4, 3],
    'Price': [2000, 1500, 5000, 2000, 1500, 5000],
    'Region': ['North', 'North', 'North', 'South', 'South', 'South']
}
df = pd.DataFrame(data)

df['Revenue'] = df['Units'] * df['Price']

region_sales = df.groupby('Region')['Revenue'].sum()


discounts = np.random.randint(5, 20, size=len(df))  # 5–20%
df['Discount%'] = discounts
df['FinalRevenue'] = df['Revenue'] * (1 - discounts / 100)


best_product = df.groupby('Product')['FinalRevenue'].sum().idxmax()

print("Sales Data:\n", df, "\n")
print("Region-wise Sales:\n", region_sales, "\n")
print("Best-Selling Product:", best_product)
