import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("First 5 rows of dataset:")
print(data.head())

# Check dataset information
print("\nDataset Information:")
print(data.info())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Total sales by category
sales_by_category = data.groupby("Category")["Sales"].sum()
print("\nTotal Sales by Category:")
print(sales_by_category)

# Plot bar chart for sales by category
plt.figure(figsize=(8,5))
sales_by_category.plot(kind='bar', color='skyblue')
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 products by sales
top_products = data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Sales:")
print(top_products)

# Plot top products
plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()

# Sales by region
sales_by_region = data.groupby("Region")["Sales"].sum()

plt.figure(figsize=(6,6))
sales_by_region.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()