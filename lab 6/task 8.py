import pandas as pd

products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')

print("First 5 rows of products:")
print(products_df.head())
print("\nLast 10 rows of products:")
print(products_df.tail(10))

print("\nFirst 5 rows of orders:")
print(orders_df.head())
print("\nLast 10 rows of orders:")
print(orders_df.tail(10))

merged_df = pd.merge(orders_df, products_df, on='ProductID')

merged_df['Revenue'] = merged_df['Quantity'] * merged_df['Price']

total_revenue = merged_df['Revenue'].sum()
print("\nTotal revenue generated: $", total_revenue)

best_selling = merged_df.groupby('ProductID')['Quantity'].sum().sort_values(ascending=False)

print("\nTop 5 best-selling products:")
print(best_selling.head())

print("\nTop 5 low-selling products:")
print(best_selling.tail())

top_5_products = best_selling.head().index
top_5_categories = merged_df[merged_df['ProductID'].isin(top_5_products)]['Category']
most_common_category = top_5_categories.mode()[0]
print("\n Most common product category among the top 5 best-selling products: ", most_common_category)

average_price_by_category = products_df.groupby('Category')['Price'].mean()
print("\nAverage price of products in each category:")
print(average_price_by_category)

merged_df['Order Date'] = pd.to_datetime(merged_df['Order Date'], format='%m-%d-%Y')

merged_df['Day'] = merged_df['Order Date'].dt.day
merged_df['Month'] = merged_df['Order Date'].dt.month
merged_df['Year'] = merged_df['Order Date'].dt.year

day_with_max_revenue = merged_df.groupby('Day')['Revenue'].sum().idxmax()
month_with_max_revenue = merged_df.groupby('Month')['Revenue'].sum().idxmax()
year_with_max_revenue = merged_df.groupby('Year')['Revenue'].sum().idxmax()

print("\nDay with highest revenue: ", day_with_max_revenue)
print("Month with highest revenue: ", month_with_max_revenue)
print("Year with highest revenue: ", year_with_max_revenue)

monthly_revenue = merged_df.groupby('Month')['Revenue'].sum().reset_index()
print("\nTotal revenue for each month:")
print(monthly_revenue)

print("\nChecking for null values in products:")
print(products_df.isnull().sum())

print("\nChecking for null values in orders:")
print(orders_df.isnull().sum())
