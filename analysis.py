import pandas as pd

df = pd.read_csv("sales.csv")

total_revenue = df["Revenue"].sum()
revenue_by_product = df.groupby("Product")["Revenue"].sum()

print("Total Revenue:", total_revenue)
print("\nRevenue by Product:\n", revenue_by_product)
