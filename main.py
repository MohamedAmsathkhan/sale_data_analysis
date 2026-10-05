"""
Main Execution Script for Sales Data Analysis
---------------------------------------------
Executes the modular data analysis pipeline: loading data, generating text reports,
extracting top performers & insights, and displaying visual charts.
"""

import argparse
import os
import sys


def run_full_analysis(
    csv_file: str = "Sales_Data_Analysis_Full(1).csv",
    show_plots: bool = True,
    save_plots: bool = False,
) -> None:
    """Runs the complete end-to-end sales analysis pipeline."""
    from modules import (
        load_dataset,
        print_data_inspection,
        print_sales_report,
        print_profit_report,
        print_quantity_discount_report,
        print_top_performers_report,
        generate_insights_and_conclusion,
        plot_all_visualizations,
    )

    print("=" * 70)
    print("             SALES DATA ANALYSIS - MODULAR PIPELINE")
    print("=" * 70)
    
    # Step 1: Load Data
    print(f"\n[+] Loading dataset from '{csv_file}'...")
    df = load_dataset(csv_file)
    print(f"[✓] Successfully loaded dataset with {len(df)} records.\n")

    # Step 2: Data Inspection
    print("[+] Step 1/6: Running Data Inspection...")
    print_data_inspection(df)

    # Step 3: Sales Analysis
    print("[+] Step 2/6: Running Sales Analysis...")
    print_sales_report(df)

    # Step 4: Profit Analysis
    print("[+] Step 3/6: Running Profit Analysis...")
    print_profit_report(df)

    # Step 5: Quantity & Discount Analysis
    print("[+] Step 4/6: Running Quantity & Discount Analysis...")
    print_quantity_discount_report(df)

    # Step 6: Top Performers & Insights
    print("[+] Step 5/6: Generating Top Performers & Executive Insights...")
    print_top_performers_report(df)
    generate_insights_and_conclusion(df)

    # Step 7: Visualizations
    if show_plots or save_plots:
        print("[+] Step 6/6: Rendering Data Visualizations...")
        plot_all_visualizations(df, show_plots=show_plots, save_plots=save_plots)
        print("[✓] Data Visualizations Complete.")

    print("\n[✓] ALL ANALYSIS MODULES EXECUTED SUCCESSFULLY.")


def main() -> None:
    """CLI parser entry point."""
    parser = argparse.ArgumentParser(
        description="Sales Data Analysis - Modular Processing Tool"
    )
    parser.add_argument(
        "--csv-file",
        type=str,
        default="Sales_Data_Analysis_Full(1).csv",
        help="Path to CSV dataset file (default: Sales_Data_Analysis_Full(1).csv)",
    )
    parser.add_argument(
        "--no-plots",
        action="store_true",
        help="Disable displaying matplotlib chart windows",
    )
    parser.add_argument(
        "--save-plots",
        action="store_true",
        help="Save generated charts as PNG files in 'charts/' directory",
    )
    parser.add_argument(
        "--dashboard",
        action="store_true",
        help="Launch the interactive Streamlit Sales Analysis Dashboard",
    )
    parser.add_argument(
        "--html-dashboard",
        action="store_true",
        help="Open the standalone HTML Sales Analysis Dashboard in web browser",
    )

    args = parser.parse_args()

    if args.dashboard:
        import subprocess
        print("[+] Launching Streamlit Interactive Sales Dashboard...")
        app_path = "app.py" if os.path.exists("app.py") else os.path.join("sale_data_analysis", "app.py")
        subprocess.run(["streamlit", "run", app_path])
        return

    if args.html_dashboard:
        import webbrowser
        html_path = os.path.abspath("dashboard.html" if os.path.exists("dashboard.html") else os.path.join("sale_data_analysis", "dashboard.html"))
        print(f"[+] Opening standalone HTML Sales Dashboard: {html_path}")
        webbrowser.open(f"file:///{html_path}")
        return

    show_plots = not args.no_plots
    run_full_analysis(
        csv_file=args.csv_file, show_plots=show_plots, save_plots=args.save_plots
    )


if __name__ == "__main__":
    main()
