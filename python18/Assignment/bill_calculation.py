import pandas as pd
import numpy as np
from tabulate import tabulate   

df = pd.read_csv("bill.csv")

df['Total'] = df['Quantity'] * df['PricePerUnit']

df['Discount%'] = np.random.randint(5, 15, len(df))
df['FinalBill'] = df['Total'] * (1 - df['Discount%'] / 100)

df = df.sort_values(by="FinalBill", ascending=False)

exp_item = df.loc[df['FinalBill'].idxmax(), 'Item']

grand_total = df['FinalBill'].sum()

df.to_csv("bill_summary.csv", index=False)

print("\n Supermarket Bill\n")
print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
print("\nMost Expensive Item After Discount:", exp_item)
print("Grand Total (Final Bill):", round(grand_total, 2))
print("\nSummary saved as bill_summary.csv")
