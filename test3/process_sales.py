import pandas as pd

# Read the CSV file (it must be placed in the same folder)
df = pd.read_csv("sales-data.csv")

# Calculate price per square foot
df["price_per_sqft"] = df["SalePrice"] / df["Sqft"]

# Calculate average price per square foot
avg_price_per_sqft = df["price_per_sqft"].mean()

# Filter properties below average price/ft²
filtered_df = df[df["price_per_sqft"] < avg_price_per_sqft]

# Save results
filtered_df.to_csv("filtered_sales.csv", index=False)

print("Generated filtered_sales.csv successfully.")
