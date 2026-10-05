"""
Quantity & Discount Analysis Module
-----------------------------------
Contains functions to evaluate unit sales quantity breakdown by product, category,
city, region, and payment method, along with discount statistics.
"""

from typing import Dict, Any
import pandas as pd


def get_total_quantity(df: pd.DataFrame) -> int:
    """Calculates overall total quantity sold."""
    return int(df["Quantity"].sum())


def get_product_quantity(df: pd.DataFrame) -> pd.Series:
    """Calculates total quantity sold aggregated by Product."""
    return df.groupby("Product")["Quantity"].sum()


def get_category_quantity(df: pd.DataFrame) -> pd.Series:
    """Calculates total quantity sold aggregated by Category."""
    return df.groupby("Category")["Quantity"].sum()


def get_city_quantity(df: pd.DataFrame) -> pd.Series:
    """Calculates total quantity sold aggregated by City."""
    return df.groupby("City")["Quantity"].sum()


def get_region_quantity(df: pd.DataFrame) -> pd.Series:
    """Calculates total quantity sold aggregated by Region."""
    return df.groupby("Region")["Quantity"].sum()


def get_payment_quantity(df: pd.DataFrame) -> pd.Series:
    """Calculates total quantity sold aggregated by Payment Method."""
    return df.groupby("Payment_Method")["Quantity"].sum()


def get_discount_stats(df: pd.DataFrame) -> Dict[str, float]:
    """Returns average, minimum, and maximum discount rates."""
    return {
        "mean_discount": float(df["Discount"].mean()),
        "max_discount": float(df["Discount"].max()),
        "min_discount": float(df["Discount"].min()),
    }


def get_product_avg_discount(df: pd.DataFrame) -> pd.Series:
    """Calculates average discount rate for each product."""
    return df.groupby("Product")["Discount"].mean()


def print_quantity_discount_report(df: pd.DataFrame) -> None:
    """Prints a structured summary report of quantity and discount metrics."""
    p_qty = get_product_quantity(df)
    cat_qty = get_category_quantity(df)
    c_qty = get_city_quantity(df)
    r_qty = get_region_quantity(df)
    pay_qty = get_payment_quantity(df)
    disc_stats = get_discount_stats(df)
    p_disc = get_product_avg_discount(df)

    print("=" * 60)
    print("               QUANTITY & DISCOUNT ANALYSIS REPORT")
    print("=" * 60)
    print(f"TOTAL QUANTITY SOLD: {get_total_quantity(df):,}")

    print("\n--- PRODUCT-WISE QUANTITY ---")
    print(p_qty)
    print(f"MOST SOLD PRODUCT: {p_qty.idxmax()} ({p_qty.max():,} units)")

    print("\n--- CATEGORY-WISE QUANTITY ---")
    print(cat_qty)
    print(f"MOST SOLD CATEGORY: {cat_qty.idxmax()} ({cat_qty.max():,} units)")

    print("\n--- CITY-WISE QUANTITY ---")
    print(c_qty)
    print(f"MOST SOLD CITY: {c_qty.idxmax()} ({c_qty.max():,} units)")

    print("\n--- REGION-WISE QUANTITY ---")
    print(r_qty)
    print(f"MOST SOLD REGION: {r_qty.idxmax()} ({r_qty.max():,} units)")

    print("\n--- PAYMENT METHOD-WISE QUANTITY ---")
    print(pay_qty)
    print(f"MOST USED PAYMENT METHOD: {pay_qty.idxmax()} ({pay_qty.max():,} units)")

    print("\n--- DISCOUNT METRICS ---")
    print(f"AVERAGE DISCOUNT: {disc_stats['mean_discount'] * 100:.2f}%")
    print(f"HIGHEST DISCOUNT: {disc_stats['max_discount'] * 100:.2f}%")
    print(f"LOWEST DISCOUNT : {disc_stats['min_discount'] * 100:.2f}%")

    print("\n--- PRODUCT-WISE AVERAGE DISCOUNT ---")
    print(p_disc)
    print("=" * 60 + "\n")
