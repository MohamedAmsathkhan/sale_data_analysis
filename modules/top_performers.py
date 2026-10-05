"""
Top Performers & Insights Module
--------------------------------
Contains routines for computing Top 5 rankings (Products, Cities, Months, Regions),
extracting executive insights, and generating business conclusions.
"""

from typing import Dict, Any
import pandas as pd
from .sales_analysis import (
    get_product_sales,
    get_city_sales,
    get_region_sales,
    get_monthly_sales,
    get_payment_sales,
    get_category_sales,
    get_total_sales,
)
from .profit_analysis import (
    get_product_profit,
    get_city_profit,
    get_region_profit,
    get_monthly_profit,
    get_payment_profit,
    get_category_profit,
    get_total_profit,
)
from .quantity_analysis import (
    get_product_quantity,
    get_total_quantity,
)


def get_top_products_by_sales(df: pd.DataFrame, n: int = 5) -> pd.Series:
    """Returns top N products sorted by sales descending."""
    return get_product_sales(df).sort_values(ascending=False).head(n)


def get_top_products_by_profit(df: pd.DataFrame, n: int = 5) -> pd.Series:
    """Returns top N products sorted by profit descending."""
    return get_product_profit(df).sort_values(ascending=False).head(n)


def get_top_products_by_quantity(df: pd.DataFrame, n: int = 5) -> pd.Series:
    """Returns top N products sorted by quantity sold descending."""
    return get_product_quantity(df).sort_values(ascending=False).head(n)


def get_top_cities_by_sales(df: pd.DataFrame, n: int = 5) -> pd.Series:
    """Returns top N cities sorted by sales descending."""
    return get_city_sales(df).sort_values(ascending=False).head(n)


def get_top_cities_by_profit(df: pd.DataFrame, n: int = 5) -> pd.Series:
    """Returns top N cities sorted by profit descending."""
    return get_city_profit(df).sort_values(ascending=False).head(n)


def get_best_sales_month(df: pd.DataFrame) -> Dict[str, Any]:
    """Returns the month with the highest sales."""
    m_sales = get_monthly_sales(df)
    return {"month": m_sales.idxmax(), "sales": float(m_sales.max())}


def get_best_profit_month(df: pd.DataFrame) -> Dict[str, Any]:
    """Returns the month with the highest profit."""
    m_profit = get_monthly_profit(df)
    return {"month": m_profit.idxmax(), "profit": float(m_profit.max())}


def get_best_sales_region(df: pd.DataFrame) -> Dict[str, Any]:
    """Returns the region with highest sales."""
    r_sales = get_region_sales(df)
    return {"region": r_sales.idxmax(), "sales": float(r_sales.max())}


def get_best_profit_region(df: pd.DataFrame) -> Dict[str, Any]:
    """Returns the region with highest profit."""
    r_profit = get_region_profit(df)
    return {"region": r_profit.idxmax(), "profit": float(r_profit.max())}


def get_best_payment_method(df: pd.DataFrame) -> Dict[str, Any]:
    """Returns the payment method generating highest sales and profit."""
    pay_sales = get_payment_sales(df)
    pay_profit = get_payment_profit(df)
    return {
        "best_sales_method": pay_sales.idxmax(),
        "highest_sales": float(pay_sales.max()),
        "best_profit_method": pay_profit.idxmax(),
        "highest_profit": float(pay_profit.max()),
    }


def generate_insights_and_conclusion(df: pd.DataFrame) -> None:
    """Generates and prints structured business insights and executive conclusion."""
    p_sales = get_product_sales(df)
    p_profit = get_product_profit(df)
    p_qty = get_product_quantity(df)
    c_sales = get_city_sales(df)
    c_profit = get_city_profit(df)
    cat_sales = get_category_sales(df)
    cat_profit = get_category_profit(df)
    r_sales = get_region_sales(df)
    r_profit = get_region_profit(df)
    pay_sales = get_payment_sales(df)
    pay_profit = get_payment_profit(df)
    m_sales = get_monthly_sales(df)
    m_profit = get_monthly_profit(df)

    print("=" * 60)
    print("                    PROJECT INSIGHTS (TOP 20)")
    print("=" * 60)
    print(f" 1. Total Sales                    : ${get_total_sales(df):,.2f}")
    print(f" 2. Total Profit                   : ${get_total_profit(df):,.2f}")
    print(f" 3. Total Quantity Sold            : {get_total_quantity(df):,}")
    print(f" 4. Highest Selling Product        : {p_sales.idxmax()}")
    print(f" 5. Highest Product Sales          : ${p_sales.max():,.2f}")
    print(f" 6. Highest Profit Product         : {p_profit.idxmax()}")
    print(f" 7. Highest Product Profit         : ${p_profit.max():,.2f}")
    print(f" 8. Highest Sales City             : {c_sales.idxmax()}")
    print(f" 9. Highest City Sales             : ${c_sales.max():,.2f}")
    print(f"10. Highest Profit City            : {c_profit.idxmax()}")
    print(f"11. Highest City Profit            : ${c_profit.max():,.2f}")
    print(f"12. Highest Sales Category         : {cat_sales.idxmax()}")
    print(f"13. Highest Profit Category        : {cat_profit.idxmax()}")
    print(f"14. Highest Sales Region           : {r_sales.idxmax()}")
    print(f"15. Highest Profit Region          : {r_profit.idxmax()}")
    print(f"16. Highest Sales Payment Method   : {pay_sales.idxmax()}")
    print(f"17. Highest Profit Payment Method  : {pay_profit.idxmax()}")
    print(f"18. Highest Sales Month            : Month {m_sales.idxmax()}")
    print(f"19. Highest Profit Month           : Month {m_profit.idxmax()}")
    print(f"20. Most Sold Product              : {p_qty.idxmax()}")
    print("=" * 60 + "\n")

    print("-" * 60)
    print("                   PROJECT CONCLUSION")
    print("-" * 60)
    print("The Sales Data Analysis project was performed using Python, Pandas, and Matplotlib.")
    print("The analysis helped to identify sales, profit, quantity, product, category, city, region,")
    print("payment method, and monthly performance.")
    print("The highest-selling product, most profitable product, best-performing city, region, category,")
    print("payment method, and month were successfully identified.")
    print("Charts were used to visualize the sales and profit performance.")
    print("Overall, the analysis helps to understand business performance and supports better")
    print("data-driven decision making.")
    print("=" * 60 + "\n")


def print_top_performers_report(df: pd.DataFrame) -> None:
    """Prints top 5 breakdown reports for products, cities, and metrics."""
    print("=" * 60)
    print("               TOP PERFORMERS & RANKINGS REPORT")
    print("=" * 60)

    print("\n--- TOP 5 PRODUCTS BY SALES ---")
    print(get_top_products_by_sales(df))

    print("\n--- TOP 5 PRODUCTS BY PROFIT ---")
    print(get_top_products_by_profit(df))

    print("\n--- TOP 5 PRODUCTS BY QUANTITY SOLD ---")
    print(get_top_products_by_quantity(df))

    print("\n--- TOP 5 CITIES BY SALES ---")
    print(get_top_cities_by_sales(df))

    print("\n--- TOP 5 CITIES BY PROFIT ---")
    print(get_top_cities_by_profit(df))

    best_sales_m = get_best_sales_month(df)
    best_profit_m = get_best_profit_month(df)
    best_sales_r = get_best_sales_region(df)
    best_profit_r = get_best_profit_region(df)
    best_pay = get_best_payment_method(df)

    print(f"\nHIGHEST SALES MONTH : Month {best_sales_m['month']} (${best_sales_m['sales']:,.2f})")
    print(f"HIGHEST PROFIT MONTH: Month {best_profit_m['month']} (${best_profit_m['profit']:,.2f})")
    print(f"HIGHEST SALES REGION: {best_sales_r['region']} (${best_sales_r['sales']:,.2f})")
    print(f"HIGHEST PROFIT REGION: {best_profit_r['region']} (${best_profit_r['profit']:,.2f})")
    print(f"BEST PAYMENT METHOD : {best_pay['best_sales_method']} (${best_pay['highest_sales']:,.2f})")
    print("=" * 60 + "\n")
