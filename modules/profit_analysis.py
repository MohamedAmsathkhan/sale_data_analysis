"""
Profit Analysis Module
---------------------
Contains functions to evaluate total profit, profit margins, and profit breakdowns
across product, city, region, month, category, payment method, and discount levels.
"""

from typing import Dict, Any
import pandas as pd


def get_total_profit(df: pd.DataFrame) -> float:
    """Calculates overall total profit."""
    return float(df["Profit"].sum())


def get_product_profit(df: pd.DataFrame) -> pd.Series:
    """Calculates total profit aggregated by Product."""
    return df.groupby("Product")["Profit"].sum()


def get_city_profit(df: pd.DataFrame) -> pd.Series:
    """Calculates total profit aggregated by City."""
    return df.groupby("City")["Profit"].sum()


def get_region_profit(df: pd.DataFrame) -> pd.Series:
    """Calculates total profit aggregated by Region."""
    return df.groupby("Region")["Profit"].sum()


def get_monthly_profit(df: pd.DataFrame) -> pd.Series:
    """Calculates total profit aggregated by Month."""
    if "Month" not in df.columns:
        df["Order_Date"] = pd.to_datetime(df["Order_Date"])
        df["Month"] = df["Order_Date"].dt.month
    return df.groupby("Month")["Profit"].sum()


def get_payment_profit(df: pd.DataFrame) -> pd.Series:
    """Calculates total profit aggregated by Payment Method."""
    return df.groupby("Payment_Method")["Profit"].sum()


def get_category_profit(df: pd.DataFrame) -> pd.Series:
    """Calculates total profit aggregated by Category."""
    return df.groupby("Category")["Profit"].sum()


def get_overall_profit_margin(df: pd.DataFrame) -> float:
    """Calculates overall profit margin percentage: (Total Profit / Total Sales) * 100."""
    total_sales = df["Sales"].sum()
    if total_sales == 0:
        return 0.0
    return float((df["Profit"].sum() / total_sales) * 100)


def get_product_avg_profit(df: pd.DataFrame) -> pd.Series:
    """Calculates average profit per transaction for each product."""
    return df.groupby("Product")["Profit"].mean()


def get_discount_avg_profit(df: pd.DataFrame) -> pd.Series:
    """Calculates average profit for each discount level."""
    return df.groupby("Discount")["Profit"].mean()


def get_profit_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """Returns key profit summary metrics."""
    p_profit = get_product_profit(df)
    c_profit = get_city_profit(df)

    return {
        "total_profit": get_total_profit(df),
        "profit_margin": get_overall_profit_margin(df),
        "highest_profit_product": p_profit.idxmax(),
        "highest_product_profit": float(p_profit.max()),
        "highest_profit_city": c_profit.idxmax(),
        "highest_city_profit": float(c_profit.max()),
    }


def print_profit_report(df: pd.DataFrame) -> None:
    """Prints a structured summary report of profit analysis."""
    p_profit = get_product_profit(df)
    c_profit = get_city_profit(df)
    r_profit = get_region_profit(df)
    m_profit = get_monthly_profit(df)
    pay_profit = get_payment_profit(df)
    cat_profit = get_category_profit(df)
    margin = get_overall_profit_margin(df)

    print("=" * 60)
    print("                   PROFIT ANALYSIS REPORT")
    print("=" * 60)
    print(f"TOTAL PROFIT         : ${get_total_profit(df):,.2f}")
    print(f"OVERALL PROFIT MARGIN: {margin:.2f}%")

    print("\n--- PRODUCT-WISE PROFIT ---")
    print(p_profit)
    print(f"HIGHEST PROFIT PRODUCT: {p_profit.idxmax()} (${p_profit.max():,.2f})")

    print("\n--- CITY-WISE PROFIT ---")
    print(c_profit)
    print(f"HIGHEST PROFIT CITY   : {c_profit.idxmax()} (${c_profit.max():,.2f})")

    print("\n--- REGION-WISE PROFIT ---")
    print(r_profit)
    print(f"HIGHEST PROFIT REGION : {r_profit.idxmax()} (${r_profit.max():,.2f})")

    print("\n--- CATEGORY-WISE PROFIT ---")
    print(cat_profit)
    print(f"HIGHEST PROFIT CATEGORY: {cat_profit.idxmax()} (${cat_profit.max():,.2f})")

    print("\n--- MONTHLY PROFIT ---")
    print(m_profit)
    print(f"HIGHEST PROFIT MONTH   : Month {m_profit.idxmax()} (${m_profit.max():,.2f})")

    print("\n--- PAYMENT METHOD-WISE PROFIT ---")
    print(pay_profit)
    print(f"HIGHEST PROFIT PAYMENT METHOD: {pay_profit.idxmax()} (${pay_profit.max():,.2f})")
    print("=" * 60 + "\n")
