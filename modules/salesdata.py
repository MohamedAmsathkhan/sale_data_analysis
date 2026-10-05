"""
Visualization Module
--------------------
Contains reusable plotting functions for displaying and saving data visualisations
using Matplotlib.
"""

import os
from typing import Optional
import matplotlib.pyplot as plt
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
    get_category_quantity,
    get_city_quantity,
    get_region_quantity,
    get_payment_quantity,
    get_product_avg_discount,
)


def plot_bar_chart(
    series: pd.Series,
    title: str,
    xlabel: str,
    ylabel: str,
    rotation: int = 0,
    figsize: tuple = (8, 5),
    show: bool = True,
    save_path: Optional[str] = None,
) -> None:
    """Generic helper function for rendering bar charts."""
    plt.figure(figsize=figsize)
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if rotation:
        plt.xticks(rotation=rotation)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()
    else:
        plt.close()


def plot_dual_bar_chart(
    series1: pd.Series,
    series2: pd.Series,
    label1: str,
    label2: str,
    title: str,
    xlabel: str,
    ylabel: str,
    figsize: tuple = (8, 5),
    show: bool = True,
    save_path: Optional[str] = None,
) -> None:
    """Generic helper for side-by-side dual bar charts (e.g. Sales vs Profit)."""
    plt.figure(figsize=figsize)
    x = range(len(series1.index))
    plt.bar(x, series1.values, width=0.4, label=label1)
    plt.bar([i + 0.4 for i in x], series2.values, width=0.4, label=label2)
    plt.xticks([i + 0.2 for i in x], series1.index)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()
    else:
        plt.close()


def plot_scatter_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str,
    xlabel: str,
    ylabel: str,
    figsize: tuple = (8, 5),
    show: bool = True,
    save_path: Optional[str] = None,
) -> None:
    """Generic helper for scatter plots."""
    plt.figure(figsize=figsize)
    plt.scatter(df[x_col], df[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()
    else:
        plt.close()


def plot_all_visualizations(
    df: pd.DataFrame, show_plots: bool = True, save_plots: bool = False, output_dir: str = "charts"
) -> None:
    """
    Renders/saves all dataset visual charts:
    - Product, City, Region, Category, Payment Method, Monthly Sales & Profit
    - Quantity Sold charts
    - Dual Sales vs Profit comparisons
    - Scatter plots (Sales vs Discount, Profit vs Sales)
    """
    if save_plots:
        os.makedirs(output_dir, exist_ok=True)

    def get_path(filename: str) -> Optional[str]:
        return os.path.join(output_dir, filename) if save_plots else None

    # 1. Product-wise Sales
    plot_bar_chart(
        get_product_sales(df),
        "Product-wise Sales",
        "Product",
        "Sales",
        rotation=45,
        show=show_plots,
        save_path=get_path("product_sales.png"),
    )

    # 2. City-wise Sales
    plot_bar_chart(
        get_city_sales(df),
        "City-wise Sales",
        "City",
        "Sales",
        rotation=45,
        show=show_plots,
        save_path=get_path("city_sales.png"),
    )

    # 3. Region-wise Sales vs Profit
    plot_dual_bar_chart(
        get_region_sales(df),
        get_region_profit(df),
        "Sales",
        "Profit",
        "Region-wise Sales vs Profit",
        "Region",
        "Amount",
        show=show_plots,
        save_path=get_path("region_sales_vs_profit.png"),
    )

    # 4. Category-wise Sales
    plot_bar_chart(
        get_category_sales(df),
        "Category-wise Sales",
        "Category",
        "Sales",
        show=show_plots,
        save_path=get_path("category_sales.png"),
    )

    # 5. Category-wise Profit
    plot_bar_chart(
        get_category_profit(df),
        "Category-wise Profit",
        "Category",
        "Profit",
        show=show_plots,
        save_path=get_path("category_profit.png"),
    )

    # 6. Payment Method-wise Sales
    plot_bar_chart(
        get_payment_sales(df),
        "Payment Method-wise Sales",
        "Payment Method",
        "Sales",
        show=show_plots,
        save_path=get_path("payment_sales.png"),
    )

    # 7. Monthly Sales
    plot_bar_chart(
        get_monthly_sales(df),
        "Monthly Sales",
        "Month",
        "Sales",
        show=show_plots,
        save_path=get_path("monthly_sales.png"),
    )

    # 8. Monthly Profit
    plot_bar_chart(
        get_monthly_profit(df),
        "Monthly Profit",
        "Month",
        "Profit",
        show=show_plots,
        save_path=get_path("monthly_profit.png"),
    )

    # 9. Product-wise Profit
    plot_bar_chart(
        get_product_profit(df),
        "Product-wise Profit",
        "Product",
        "Profit",
        rotation=45,
        show=show_plots,
        save_path=get_path("product_profit.png"),
    )

    # 10. City-wise Profit
    plot_bar_chart(
        get_city_profit(df),
        "City-wise Profit",
        "City",
        "Profit",
        rotation=45,
        show=show_plots,
        save_path=get_path("city_profit.png"),
    )

    # 11. Region-wise Profit
    plot_bar_chart(
        get_region_profit(df),
        "Region-wise Profit",
        "Region",
        "Profit",
        show=show_plots,
        save_path=get_path("region_profit.png"),
    )

    # 12. Payment Method-wise Profit
    plot_bar_chart(
        get_payment_profit(df),
        "Payment Method-wise Profit",
        "Payment Method",
        "Profit",
        show=show_plots,
        save_path=get_path("payment_profit.png"),
    )

    # 13. Product-wise Quantity Sold
    plot_bar_chart(
        get_product_quantity(df),
        "Product-wise Quantity Sold",
        "Product",
        "Quantity Sold",
        rotation=45,
        show=show_plots,
        save_path=get_path("product_quantity.png"),
    )

    # 14. Monthly Sales vs Profit
    plot_dual_bar_chart(
        get_monthly_sales(df),
        get_monthly_profit(df),
        "Sales",
        "Profit",
        "Monthly Sales vs Profit",
        "Month",
        "Amount",
        show=show_plots,
        save_path=get_path("monthly_sales_vs_profit.png"),
    )

    # 15. Overall Sales vs Profit
    plt.figure(figsize=(7, 5))
    plt.bar(["Sales", "Profit"], [get_total_sales(df), get_total_profit(df)])
    plt.title("Overall Sales vs Profit")
    plt.xlabel("Metric")
    plt.ylabel("Amount")
    plt.tight_layout()
    if save_plots:
        plt.savefig(get_path("overall_sales_vs_profit.png"))
    if show_plots:
        plt.show()
    else:
        plt.close()

    # 16. Product-wise Average Discount
    plot_bar_chart(
        get_product_avg_discount(df),
        "Product-wise Average Discount",
        "Product",
        "Average Discount",
        rotation=45,
        show=show_plots,
        save_path=get_path("product_avg_discount.png"),
    )

    # 17. Category-wise Quantity Sold
    plot_bar_chart(
        get_category_quantity(df),
        "Category-wise Quantity Sold",
        "Category",
        "Quantity Sold",
        show=show_plots,
        save_path=get_path("category_quantity.png"),
    )

    # 18. City-wise Quantity Sold
    plot_bar_chart(
        get_city_quantity(df),
        "City-wise Quantity Sold",
        "City",
        "Quantity Sold",
        rotation=45,
        show=show_plots,
        save_path=get_path("city_quantity.png"),
    )

    # 19. Region-wise Quantity Sold
    plot_bar_chart(
        get_region_quantity(df),
        "Region-wise Quantity Sold",
        "Region",
        "Quantity Sold",
        show=show_plots,
        save_path=get_path("region_quantity.png"),
    )

    # 20. Payment Method-wise Quantity Sold
    plot_bar_chart(
        get_payment_quantity(df),
        "Payment Method-wise Quantity Sold",
        "Payment Method",
        "Quantity Sold",
        show=show_plots,
        save_path=get_path("payment_quantity.png"),
    )

    # 21. Sales vs Discount
    plot_scatter_chart(
        df,
        "Discount",
        "Sales",
        "Sales vs Discount",
        "Discount",
        "Sales",
        show=show_plots,
        save_path=get_path("sales_vs_discount.png"),
    )

    # 22. Profit vs Sales
    plot_scatter_chart(
        df,
        "Sales",
        "Profit",
        "Profit vs Sales",
        "Sales",
        "Profit",
        show=show_plots,
        save_path=get_path("profit_vs_sales.png"),
    )
