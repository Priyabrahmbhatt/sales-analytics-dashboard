import pandas as pd

df = pd.read_csv("data/train.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales.sort_values(ascending=False))

top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 Products:")
print(top_products)
state_sales = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop States:")
print(state_sales)
import matplotlib.pyplot as plt

region_sales.sort_values().plot(kind="bar")

plt.title("Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()

plt.show()
