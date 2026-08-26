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
##1. Region-wise Sales vs Profit char
## Region-wise Sales vs Profit Chart

import matplotlib.pyplot as plt

x = range(len(region_sales.index))

plt.figure(figsize=(8,5))

plt.bar(x, region_sales.values, width=0.4, label="Sales")
plt.bar([i + 0.4 for i in x], region_profit.values, width=0.4, label="Profit")

plt.xticks([i + 0.2 for i in x], region_sales.index)

plt.title("Region-wise Sales vs Profit")
plt.xlabel("Region")
plt.ylabel("Amount")

plt.legend()
plt.show()
##Category-wise Sales Chart
## Category-wise Sales Chart

plt.figure(figsize=(8,5))

category_sales.plot(kind="bar")

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()
##Category-wise Profit Chart
## Category-wise Profit Chart

plt.figure(figsize=(8,5))

category_profit.plot(kind="bar")

plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.show()
##Payment Method-wise Sales Chart
## Payment Method-wise Sales Chart

plt.figure(figsize=(8,5))

payment_sales.plot(kind="bar")

plt.title("Payment Method-wise Sales")
plt.xlabel("Payment Method")
plt.ylabel("Sales")

plt.show()
##Monthly Sales Char
## Monthly Sales Chart

plt.figure(figsize=(8,5))

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
##Monthly Profit Chart
## Monthly Profit Chart

plt.figure(figsize=(8,5))

monthly_profit.plot(kind="bar")

plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.show()
##Product-wise Profit Chart
## Product-wise Profit Chart

plt.figure(figsize=(8,5))

product_profit.plot(kind="bar")

plt.title("Product-wise Profit")
plt.xlabel("Product")
plt.ylabel("Profit")

plt.show()
##City-wise Profit Chart
## City-wise Profit Chart

plt.figure(figsize=(8,5))

city_profit.plot(kind="bar")

plt.title("City-wise Profit")
plt.xlabel("City")
plt.ylabel("Profit")

plt.show()
##Region-wise Profit Chart

plt.figure(figsize=(8,5))

region_profit.plot(kind="bar")

plt.title("Region-wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.show()
##Payment Method-wise Profit Chart
## Payment Method-wise Profit Chart

plt.figure(figsize=(8,5))

payment_profit.plot(kind="bar")

plt.title("Payment Method-wise Profit")
plt.xlabel("Payment Method")
plt.ylabel("Profit")

plt.show()
###Product-wise Quantity Sold Chart
## Product-wise Quantity Sold Chart

plt.figure(figsize=(8,5))

product_quantity.plot(kind="bar")

plt.title("Product-wise Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

plt.show()
###Monthly Sales vs Profit Chart
## Monthly Sales vs Profit Chart

plt.figure(figsize=(8,5))

x = range(len(monthly_sales.index))

plt.bar(x, monthly_sales.values, width=0.4, label="Sales")
plt.bar([i + 0.4 for i in x], monthly_profit.values, width=0.4, label="Profit")

plt.xticks([i + 0.2 for i in x], monthly_sales.index)

plt.title("Monthly Sales vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.legend()
plt.show()
##Overall Sales vs Profit Chart
## Overall Sales vs Profit Chart

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

plt.figure(figsize=(7,5))

plt.bar(["Sales", "Profit"], [total_sales, total_profit])

plt.title("Overall Sales vs Profit")
plt.xlabel("Metric")
plt.ylabel("Amount")

plt.show()
##Product-wise Average Discount Chart
## Product-wise Average Discount Chart

product_discount = df.groupby("Product")["Discount"].mean()

plt.figure(figsize=(8,5))

product_discount.plot(kind="bar")

plt.title("Product-wise Average Discount")
plt.xlabel("Product")
plt.ylabel("Average Discount")

plt.show()
###Category-wise Quantity Sold Chart
## Category-wise Quantity Sold Chart

category_quantity = df.groupby("Category")["Quantity"].sum()

plt.figure(figsize=(8,5))

category_quantity.plot(kind="bar")

plt.title("Category-wise Quantity Sold")
plt.xlabel("Category")
plt.ylabel("Quantity Sold")

plt.show()

## City-wise Quantity Sold Chart

city_quantity = df.groupby("City")["Quantity"].sum()

plt.figure(figsize=(8,5))

city_quantity.plot(kind="bar")

plt.title("City-wise Quantity Sold")
plt.xlabel("City")
plt.ylabel("Quantity Sold")

plt.show()
##Region-wise Quantity Sold Chart
## Region-wise Quantity Sold Chart

region_quantity = df.groupby("Region")["Quantity"].sum()

plt.figure(figsize=(8,5))

region_quantity.plot(kind="bar")

plt.title("Region-wise Quantity Sold")
plt.xlabel("Region")
plt.ylabel("Quantity Sold")

plt.show()
##payment Method-wise Quantity Sold Chart
## Payment Method-wise Quantity Sold Chart

payment_quantity = df.groupby("Payment_Method")["Quantity"].sum()

plt.figure(figsize=(8,5))

payment_quantity.plot(kind="bar")

plt.title("Payment Method-wise Quantity Sold")
plt.xlabel("Payment Method")
plt.ylabel("Quantity Sold")

plt.show()
##Sales vs Discount Chart
## Sales vs Discount Chart

plt.figure(figsize=(8,5))

plt.scatter(df["Discount"], df["Sales"])

plt.title("Sales vs Discount")
plt.xlabel("Discount")
plt.ylabel("Sales")

plt.show()
## Profit vs Sales Chart

plt.figure(figsize=(8,5))

plt.scatter(df["Sales"], df["Profit"])

plt.title("Profit vs Sales")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.show()
## Project Insights / Findings

print("PROJECT INSIGHTS")

print("1. Total Sales:", df["Sales"].sum())
print("2. Total Profit:", df["Profit"].sum())
print("3. Total Quantity Sold:", df["Quantity"].sum())

print("4. Highest Selling Product:", product_sales.idxmax())
print("5. Highest Product Sales:", product_sales.max())

print("6. Highest Profit Product:", product_profit.idxmax())
print("7. Highest Product Profit:", product_profit.max())

print("8. Highest Sales City:", city_sales.idxmax())
print("9. Highest City Sales:", city_sales.max())

print("10. Highest Profit City:", city_profit.idxmax())
print("11. Highest City Profit:", city_profit.max())

print("12. Highest Sales Category:", category_sales.idxmax())
print("13. Highest Profit Category:", category_profit.idxmax())

print("14. Highest Sales Region:", region_sales.idxmax())
print("15. Highest Profit Region:", region_profit.idxmax())

print("16. Highest Sales Payment Method:", payment_sales.idxmax())
print("17. Highest Profit Payment Method:", payment_profit.idxmax())

print("18. Highest Sales Month:", monthly_sales.idxmax())
print("19. Highest Profit Month:", monthly_profit.idxmax())

print("20. Most Sold Product:", product_quantity.idxmax())
## Project Conclusion

print("PROJECT CONCLUSION")
print("------------------")

print("The Sales Data Analysis project was performed using Python, Pandas, and Matplotlib.")

print("The analysis helped to identify sales, profit, quantity, product, category, city, region,")
print("payment method, and monthly performance.")

print("The highest-selling product, most profitable product,")
print("best-performing city, region, category, payment method, and month were identified.")

print("Charts were used to visualize the sales and profit performance.")

print("Overall, the analysis helps to understand business performance")
print("and supports better data-driven decision making.")
## Data Loading

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sales_Data_Analysis_Full(1).csv")


## Data Inspection

print("FIRST 5 ROWS:")
print(df.head())

print("SHAPE:")
print(df.shape)

print("DATA INFORMATION:")
print(df.info())

print("DESCRIPTIVE STATISTICS:")
print(df.describe())

print("COLUMNS:")
print(df.columns)

print("MISSING VALUES:")
print(df.isnull().sum())

print("DUPLICATE ROWS:")
print(df.duplicated().sum())

print("DATA TYPES:")
print(df.dtypes)

print("PRODUCT COUNT:")
print(df["Product"].value_counts())
## Sales Analysis

print("TOTAL SALES:", df["Sales"].sum())

product_sales = df.groupby("Product")["Sales"].sum()

print("PRODUCT-WISE SALES:")
print(product_sales)

print("HIGHEST SELLING PRODUCT:", product_sales.idxmax())
print("HIGHEST PRODUCT SALES:", product_sales.max())

city_sales = df.groupby("City")["Sales"].sum()

print("CITY-WISE SALES:")
print(city_sales)

print("HIGHEST SALES CITY:", city_sales.idxmax())
print("HIGHEST CITY SALES:", city_sales.max())

region_sales = df.groupby("Region")["Sales"].sum()

print("REGION-WISE SALES:")
print(region_sales)

print("HIGHEST SALES REGION:", region_sales.idxmax())
print("HIGHEST REGION SALES:", region_sales.max())
## Monthly Sales Analysis

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Month"] = df["Order_Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

print("MONTHLY SALES:")
print(monthly_sales)

print("HIGHEST SALES MONTH:", monthly_sales.idxmax())
print("HIGHEST MONTH SALES:", monthly_sales.max())
## Payment Method-wise Sales Analysis

payment_sales = df.groupby("Payment_Method")["Sales"].sum()

print("PAYMENT METHOD-WISE SALES:")
print(payment_sales)

print("HIGHEST SALES PAYMENT METHOD:", payment_sales.idxmax())
print("HIGHEST PAYMENT SALES:", payment_sales.max())
## Profit Analysis

print("TOTAL PROFIT:", df["Profit"].sum())

product_profit = df.groupby("Product")["Profit"].sum()

print("PRODUCT-WISE PROFIT:")
print(product_profit)

print("HIGHEST PROFIT PRODUCT:", product_profit.idxmax())
print("HIGHEST PROFIT AMOUNT:", product_profit.max())
## Discount Analysis

print("AVERAGE DISCOUNT:", df["Discount"].mean())
print("HIGHEST DISCOUNT:", df["Discount"].max())
print("LOWEST DISCOUNT:", df["Discount"].min())
## Category-wise Sales & Profit Analysis

category_sales = df.groupby("Category")["Sales"].sum()

print("CATEGORY-WISE SALES:")
print(category_sales)

print("HIGHEST SALES CATEGORY:", category_sales.idxmax())
print("HIGHEST CATEGORY SALES:", category_sales.max())


category_profit = df.groupby("Category")["Profit"].sum()

print("CATEGORY-WISE PROFIT:")
print(category_profit)

print("HIGHEST PROFIT CATEGORY:", category_profit.idxmax())
print("HIGHEST CATEGORY PROFIT:", category_profit.max())
## Quantity Analysis

print("TOTAL QUANTITY SOLD:", df["Quantity"].sum())

product_quantity = df.groupby("Product")["Quantity"].sum()

print("PRODUCT-WISE QUANTITY:")
print(product_quantity)

print("MOST SOLD PRODUCT:", product_quantity.idxmax())
print("MOST SOLD QUANTITY:", product_quantity.max())
## City-wise Profit Analysis

city_profit = df.groupby("City")["Profit"].sum()

print("CITY-WISE PROFIT:")
print(city_profit)

print("HIGHEST PROFIT CITY:", city_profit.idxmax())
print("HIGHEST CITY PROFIT:", city_profit.max())
## Monthly Profit Analysis

monthly_profit = df.groupby("Month")["Profit"].sum()

print("MONTHLY PROFIT:")
print(monthly_profit)

print("HIGHEST PROFIT MONTH:", monthly_profit.idxmax())
print("HIGHEST MONTH PROFIT:", monthly_profit.max())
## Payment Method-wise Profit Analysis

payment_profit = df.groupby("Payment_Method")["Profit"].sum()

print("PAYMENT METHOD-WISE PROFIT:")
print(payment_profit)

print("HIGHEST PROFIT PAYMENT METHOD:", payment_profit.idxmax())
print("HIGHEST PAYMENT PROFIT:", payment_profit.max())
## Region-wise Profit Analysis

region_profit = df.groupby("Region")["Profit"].sum()

print("REGION-WISE PROFIT:")
print(region_profit)

print("HIGHEST PROFIT REGION:", region_profit.idxmax())
print("HIGHEST REGION PROFIT:", region_profit.max())
## Sales Summary

min_sales = product_sales.min()
average_sales = product_sales.mean()
highest_product = product_sales.idxmax()
lowest_product = product_sales.idxmin()

print("MINIMUM PRODUCT SALES:", min_sales)
print("AVERAGE PRODUCT SALES:", average_sales)
print("HIGHEST SELLING PRODUCT:", highest_product)
print("LOWEST SELLING PRODUCT:", lowest_product)


highest_city = city_sales.idxmax()
lowest_city = city_sales.idxmin()
average_city_sales = city_sales.mean()

print("HIGHEST SALES CITY:", highest_city)
print("LOWEST SALES CITY:", lowest_city)
print("AVERAGE SALES PER CITY:", average_city_sales)
## Additional Quantity Analysis

category_quantity = df.groupby("Category")["Quantity"].sum()

print("CATEGORY-WISE QUANTITY:")
print(category_quantity)

print("MOST SOLD CATEGORY:", category_quantity.idxmax())
print("HIGHEST CATEGORY QUANTITY:", category_quantity.max())


city_quantity = df.groupby("City")["Quantity"].sum()

print("CITY-WISE QUANTITY:")
print(city_quantity)

print("MOST SOLD CITY:", city_quantity.idxmax())
print("HIGHEST CITY QUANTITY:", city_quantity.max())


region_quantity = df.groupby("Region")["Quantity"].sum()

print("REGION-WISE QUANTITY:")
print(region_quantity)

print("MOST SOLD REGION:", region_quantity.idxmax())
print("HIGHEST REGION QUANTITY:", region_quantity.max())


payment_quantity = df.groupby("Payment_Method")["Quantity"].sum()

print("PAYMENT METHOD-WISE QUANTITY:")
print(payment_quantity)

print("MOST USED PAYMENT METHOD:", payment_quantity.idxmax())
print("HIGHEST PAYMENT QUANTITY:", payment_quantity.max())
## Product-wise Sales Chart

plt.figure(figsize=(8,5))

product_sales.plot(kind="bar")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()
## City-wise Sales Chart

plt.figure(figsize=(8,5))

city_sales.plot(kind="bar")

plt.title("City-wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")

plt.show()