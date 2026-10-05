"""
Sales Analysis Module
---------------------
Contains routines for computing sales metrics grouped by product, city, region,
month, category, and payment method.
"""

from typing import Dict, Any
import pandas as pd


def get_total_sales(df: pd.DataFrame) -> float:
    """Calculates overall total sales amount."""
    return float(df["Sales"].sum())


def get_product_sales(df: pd.DataFrame) -> pd.Series:
    """Calculates total sales aggregated by Product."""
    return df.groupby("Product")["Sales"].sum()


def get_city_sales(df: pd.DataFrame) -> pd.Series:
    """Calculates total sales aggregated by City."""
    return df.groupby("City")["Sales"].sum()


def get_region_sales(df: pd.DataFrame) -> pd.Series:
    """Calculates total sales aggregated by Region."""
    return df.groupby("Region")["Sales"].sum()


def get_monthly_sales(df: pd.DataFrame) -> pd.Series:
    """Calculates total sales aggregated by Month."""
    if "Month" not in df.columns:
        df["Order_Date"] = pd.to_datetime(df["Order_Date"])
        df["Month"] = df["Order_Date"].dt.month
    return df.groupby("Month")["Sales"].sum()


def get_payment_sales(df: pd.DataFrame) -> pd.Series:
    """Calculates total sales aggregated by Payment Method."""
    return df.groupby("Payment_Method")["Sales"].sum()


def get_category_sales(df: pd.DataFrame) -> pd.Series:
    """Calculates total sales aggregated by Category."""
    return df.groupby("Category")["Sales"].sum()


def get_sales_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Computes key statistical metrics for sales (product & city stats).
    """
    p_sales = get_product_sales(df)
    c_sales = get_city_sales(df)

    return {
        "total_sales": get_total_sales(df),
        "min_product_sales": float(p_sales.min()),
        "max_product_sales": float(p_sales.max()),
        "avg_product_sales": float(p_sales.mean()),
        "highest_selling_product": p_sales.idxmax(),
        "lowest_selling_product": p_sales.idxmin(),
        "highest_sales_city": c_sales.idxmax(),
        "lowest_sales_city": c_sales.idxmin(),
        "avg_city_sales": float(c_sales.mean()),
    }


def print_sales_report(df: pd.DataFrame) -> None:
    """Prints a structured summary report of sales analysis."""
    p_sales = get_product_sales(df)
    c_sales = get_city_sales(df)
    r_sales = get_region_sales(df)
    m_sales = get_monthly_sales(df)
    pay_sales = get_payment_sales(df)
    cat_sales = get_category_sales(df)
    summary = get_sales_summary(df)

    print("=" * 60)
    print("                    SALES ANALYSIS REPORT")
    print("=" * 60)
    print(f"TOTAL SALES: ${summary['total_sales']:,.2f}")

    print("\n--- PRODUCT-WISE SALES ---")
    print(p_sales)
    print(f"HIGHEST SELLING PRODUCT: {p_sales.idxmax()} (${p_sales.max():,.2f})")
    print(f"LOWEST SELLING PRODUCT : {p_sales.idxmin()} (${p_sales.min():,.2f})")

    print("\n--- CITY-WISE SALES ---")
    print(c_sales)
    print(f"HIGHEST SALES CITY : {c_sales.idxmax()} (${c_sales.max():,.2f})")
    print(f"LOWEST SALES CITY  : {c_sales.idxmin()} (${c_sales.min():,.2f})")

    print("\n--- REGION-WISE SALES ---")
    print(r_sales)
    print(f"HIGHEST SALES REGION: {r_sales.idxmax()} (${r_sales.max():,.2f})")

    print("\n--- CATEGORY-WISE SALES ---")
    print(cat_sales)
    print(f"HIGHEST SALES CATEGORY: {cat_sales.idxmax()} (${cat_sales.max():,.2f})")

    print("\n--- MONTHLY SALES ---")
    print(m_sales)
    print(f"HIGHEST SALES MONTH: Month {m_sales.idxmax()} (${m_sales.max():,.2f})")

    print("\n--- PAYMENT METHOD-WISE SALES ---")
    print(pay_sales)
    print(f"HIGHEST PAYMENT METHOD SALES: {pay_sales.idxmax()} (${pay_sales.max():,.2f})")
    print("=" * 60 + "\n")
