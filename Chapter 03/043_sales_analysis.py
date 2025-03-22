# Script: 043_sales_analysis.py

# Importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales_data.csv')

# Inspect the first few rows
print("Initial Data:")
print(df.head())

# Data Cleaning: Fill missing values if any
df.fillna({'Amount': df['Amount'].mean()}, inplace=True)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Data Aggregation: Total sales by Product
total_sales_by_product = df.groupby('Product')['Amount'].sum()
print("\nTotal Sales by Product:")
print(total_sales_by_product)

# Data Transformation: Adding a new column for commission (10% of Amount)
df['Commission'] = df['Amount'] * 0.1

# Data Visualization: Plot of total sales by product
plt.figure(figsize=(8, 4))
total_sales_by_product.plot(kind='bar')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Time Series Analysis: Resample to get monthly total sales
monthly_sales = df.resample('M', on='Date')['Amount'].sum()
print("\nMonthly Total Sales:")
print(monthly_sales)

# Plotting monthly sales
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Total Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()
