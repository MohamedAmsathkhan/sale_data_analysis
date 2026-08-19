import pandas as pd

df = pd.read_csv("Sales_Data_Analysis_Full(1).csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
print(df["Product"].value_counts())

print(df["Sales"].sum())
print(df["Product"].value_counts())

print(df["Sales"].sum())
product_sales = df.groupby("Product")["Sales"].sum()

print(product_sales)
print(product_sales.idxmax())
print(product_sales.max())
city_sales = df.groupby("City")["Sales"].sum()
print(city_sales)
print(city_sales.idxmax())
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)
print(region_sales.idxmax())
print(region_sales.max())
#month sale  analysis..
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales.idxmax())
print(monthly_sales.max())
#Payment method-wise total Sales
payment_sales = df.groupby("Payment_Method")["Sales"].sum()

print(payment_sales)
##Highest sales payment method
print(payment_sales.idxmax())
##Highest sales amount
print(payment_sales.max())

## Total Profit analysis
print("TOTAL PROFIT:",df["Profit"].sum())
print("TOTAL SALES:", df["Sales"].sum())
print("HIGHEST SALES PRODUCT:", product_sales.idxmax())
print("HIGHEST SALES AMOUNT:", product_sales.max())
## Product-wise Profit analysis
product_profit = df.groupby("Product")["Profit"].sum()

print("PRODUCT-WISE PROFIT:")
print(product_profit)
##Highest Profit Product
print("HIGHEST PROFIT PRODUCT:", product_profit.idxmax())
print("HIGHEST PROFIT AMOUNT:", product_profit.max())
##Average Discount
print("AVERAGE DISCOUNT:", df["Discount"].mean())
print("HIGHEST DISCOUNT:", df["Discount"].max())
print("LOWEST DISCOUNT:", df["Discount"].min())
##category_wise sale analysis
category_sales = df.groupby("Category")["Sales"].sum()

print("CATEGORY-WISE SALES:")
print(category_sales)

print("HIGHEST SALES CATEGORY:", category_sales.idxmax())

category_profit = df.groupby("Category")["Profit"].sum()

print("CATEGORY-WISE PROFIT:")
print(category_profit)

print("HIGHEST PROFIT CATEGORY:", category_profit.idxmax())
##category_wise profit
category_profit = df.groupby("Category")["Profit"].sum()

print("CATEGORY-WISE PROFIT:")
print(category_profit)

print("HIGHEST PROFIT CATEGORY:", category_profit.idxmax())
print("HIGHEST CATEGORY PROFIT:", category_profit.max())
## Quantity Analysi
print("TOTAL QUANTITY SOLD:", df["Quantity"].sum())

product_quantity = df.groupby("Product")["Quantity"].sum()

print("PRODUCT-WISE QUANTITY:")
print(product_quantity)

print("MOST SOLD PRODUCT:", product_quantity.idxmax())
##City-wise Profit Analysis
city_profit = df.groupby("City")["Profit"].sum()

print("CITY-WISE PROFIT:")
print(city_profit)

print("HIGHEST PROFIT CITY:", city_profit.idxmax())
print("HIGHEST CITY PROFIT:", city_profit.max())
##monthly profit
monthly_profit = df.groupby("Month")["Profit"].sum()

print("MONTHLY PROFIT:")
print(monthly_profit)

print("HIGHEST PROFIT MONTH:", monthly_profit.idxmax())
print("HIGHEST MONTH PROFIT:", monthly_profit.max())
##payment mthod profit_wise
payment_profit =df.groupby("Payment_Method")["Profit"].sum()

print("PAYMENT METHOD-WISE PROFIT:")
print(payment_profit)

##Region-wise Profit edukkura

region_profit = df.groupby("Region")["Profit"].sum()
df.groupby("Region")
df.groupby("Region")["Profit"]
df.groupby("Region")["Profit"].sum()
region_profit = df.groupby("Region")["Profit"].sum()
##Result-a display panna
region_profit = df.groupby("Region")["Profit"].sum()
print("REGION-WISE PROFIT:")
print(region_profit)
##to find highest value
highest_region_profit = region_profit.max()
highest_region = region_profit.idxmax()
## it using to identify the highest profit in region
print("HIGHEST PROFIT REGION:", highest_region)
##highest profit amount
print("HIGHEST REGION PROFIT:", highest_region_profit)
## overall sales groupby
payment_sales = df.groupby("Payment_Method")["Sales"].sum()
## to display the overall result
print("PAYMENT METHOD-WISE SALES:")
print(payment_sales)
highest_payment_sales = payment_sales.max()
##to fiinnd minimmum product sale

min_sales = product_sales.min()

print("MINIMUM PRODUCT SALES:", min_sales)
average_sales = product_sales.mean()

print("AVERAGE PRODUCT SALES:", average_sales)
highest_product = product_sales.idxmax()

print("HIGHEST SELLING PRODUCT:", highest_product)
lowest_product = product_sales.idxmin()

print("LOWEST SELLING PRODUCT:", lowest_product)
##to find the highest sale city
highest_city = city_sales.idxmax()

print("HIGHEST SALES CITY:", highest_city)
lowest_city = city_sales.idxmin()

print("LOWEST SALES CITY:", lowest_city)
average_city_sales = city_sales.mean()

print("AVERAGE SALES PER CITY:", average_city_sales)
quantity_sales = df.groupby("Product")["Quantity"].sum()

print("PRODUCT-WISE QUANTITY SOLD:")
print(quantity_sales)
##product  wise sale chart
import matplotlib.pyplot as plt

product_sales.plot(kind="bar")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()
##city_wise sale chart
city_sales.plot(kind="bar")
plt.title("City-wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.show()

