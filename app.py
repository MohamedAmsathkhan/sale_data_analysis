"""
Sales Analysis Dashboard - Streamlit Application
=================================================
A clean, interactive, and professional Sales Analysis Dashboard built with Streamlit and Plotly.
Designed for executive presentation and portfolio demonstration.
"""

import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as px_go
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Sales Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished aesthetic
st.markdown("""
<style>
    /* Global Styles */
    .main {
        background-color: #f8fafc;
    }
    .stAppViewContainer {
        background-color: #f8fafc;
    }
    /* Metric Cards */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.6rem !important;
        font-weight: 700 !important;
        color: #0f172a !important;
    }
    /* Section Headers */
    .dashboard-header {
        background: linear-gradient(90deg, #1e293b 0%, #0f172a 100%);
        color: white;
        padding: 24px 32px;
        border-radius: 16px;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.15);
    }
    .dashboard-title {
        font-size: 2rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.02em;
    }
    .dashboard-subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
        margin-top: 4px;
        margin-bottom: 0;
    }
    .card-header {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
        color: #f8fafc;
    }
    section[data-testid="stSidebar"] .stMarkdown h1, 
    section[data-testid="stSidebar"] .stMarkdown h2, 
    section[data-testid="stSidebar"] .stMarkdown h3,
    section[data-testid="stSidebar"] label {
        color: #f1f5f9 !important;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data() -> pd.DataFrame:
    """Loads dataset and performs initial preprocessing."""
    candidates = [
        "Sales_Data_Analysis_Full(1).csv",
        os.path.join("sale_data_analysis", "Sales_Data_Analysis_Full(1).csv"),
        os.path.join("..", "Sales_Data_Analysis_Full(1).csv")
    ]
    filepath = None
    for c in candidates:
        if os.path.exists(c):
            filepath = c
            break

    if not filepath:
        st.error("Dataset 'Sales_Data_Analysis_Full(1).csv' not found.")
        st.stop()

    df = pd.read_csv(filepath)
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])
    df["Month_Num"] = df["Order_Date"].dt.month
    df["Month_Name"] = df["Order_Date"].dt.strftime("%b")
    df["Year_Month"] = df["Order_Date"].dt.strftime("%Y-%m")
    
    # Sort dataset chronologically
    df = df.sort_values("Order_Date").reset_index(drop=True)
    return df


df_raw = load_data()

# ----------------------------------------------------
# SIDEBAR FILTERS / SLICERS
# ----------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/color/96/dashboard-layout.png", width=64)
    st.title("Filter Controls")
    st.markdown("Use slicers below to filter all metrics and charts in real-time.")
    
    if st.button("🔄 Reset All Filters", use_container_width=True):
        st.rerun()

    st.markdown("---")

    # 1. Date / Month Filter
    st.subheader("📅 Date / Month Range")
    min_date = df_raw["Order_Date"].min().date()
    max_date = df_raw["Order_Date"].max().date()
    
    date_range = st.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    # 2. Category Filter
    all_categories = sorted(df_raw["Category"].unique().tolist())
    selected_categories = st.multiselect(
        "📂 Category",
        options=all_categories,
        default=all_categories
    )

    # 3. Region Filter
    all_regions = sorted(df_raw["Region"].unique().tolist())
    selected_regions = st.multiselect(
        "🗺️ Region",
        options=all_regions,
        default=all_regions
    )

    # 4. Product Filter
    # Dynamically scope products based on selected categories
    available_products = sorted(
        df_raw[df_raw["Category"].isin(selected_categories) if selected_categories else True]["Product"].unique().tolist()
    )
    selected_products = st.multiselect(
        "📦 Product",
        options=available_products,
        default=available_products
    )

    # 5. Payment Method Filter
    all_payments = sorted(df_raw["Payment_Method"].unique().tolist())
    selected_payments = st.multiselect(
        "💳 Payment Method",
        options=all_payments,
        default=all_payments
    )
    
    st.markdown("---")
    st.caption("Sales Data Analysis Portfolio Project | Mohamed Amsathkhan")

# Filter DataFrame based on selections
df_filtered = df_raw.copy()

# Date filter evaluation
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
    df_filtered = df_filtered[
        (df_filtered["Order_Date"].dt.date >= start_date) & 
        (df_filtered["Order_Date"].dt.date <= end_date)
    ]

if selected_categories:
    df_filtered = df_filtered[df_filtered["Category"].isin(selected_categories)]
else:
    df_filtered = df_filtered.iloc[0:0]  # empty

if selected_regions:
    df_filtered = df_filtered[df_filtered["Region"].isin(selected_regions)]
else:
    df_filtered = df_filtered.iloc[0:0]

if selected_products:
    df_filtered = df_filtered[df_filtered["Product"].isin(selected_products)]
else:
    df_filtered = df_filtered.iloc[0:0]

if selected_payments:
    df_filtered = df_filtered[df_filtered["Payment_Method"].isin(selected_payments)]
else:
    df_filtered = df_filtered.iloc[0:0]


# ----------------------------------------------------
# MAIN HEADER
# ----------------------------------------------------
st.markdown("""
<div class="dashboard-header">
    <h1 class="dashboard-title">📈 Sales Analysis Dashboard</h1>
    <p class="dashboard-subtitle">Interactive Data Insights & Performance Metrics | Portfolio Presentation</p>
</div>
""", unsafe_allow_html=True)

if df_filtered.empty:
    st.warning("⚠️ No data matches the selected filter criteria. Please adjust your filters in the sidebar.")
    st.stop()


# ----------------------------------------------------
# KPI CARDS SECTION (5 Mandatory + 2 Key Indicators)
# ----------------------------------------------------
total_sales = df_filtered["Sales"].sum()
total_profit = df_filtered["Profit"].sum()
total_quantity = df_filtered["Quantity"].sum()
num_products = df_filtered["Product"].nunique()
num_orders = df_filtered["Order_ID"].nunique()
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0.0
avg_order_val = (total_sales / num_orders) if num_orders > 0 else 0.0

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="💰 Total Sales",
        value=f"₹{total_sales:,.2f}",
        help="Sum of total revenue generated"
    )

with col2:
    st.metric(
        label="💵 Total Profit",
        value=f"₹{total_profit:,.2f}",
        delta=f"{profit_margin:.1f}% Margin",
        help="Sum of net profit across orders"
    )

with col3:
    st.metric(
        label="📦 Total Quantity",
        value=f"{total_quantity:,}",
        help="Total number of product units sold"
    )

with col4:
    st.metric(
        label="🏷️ Number of Products",
        value=f"{num_products}",
        help="Count of unique product items sold"
    )

with col5:
    st.metric(
        label="🛒 Number of Orders",
        value=f"{num_orders:,}",
        delta=f"₹{avg_order_val:,.0f} AOV",
        help="Count of total transaction orders"
    )

st.markdown("<br>", unsafe_allow_html=True)


# ----------------------------------------------------
# CHARTS SECTION (7 Required Visualizations)
# ----------------------------------------------------

# Corporate visual color palette
COLOR_PRIMARY = "#3b82f6"     # Blue
COLOR_SUCCESS = "#10b981"     # Emerald / Green
COLOR_ACCENT = "#8b5cf6"      # Purple / Violet
COLOR_WARNING = "#f59e0b"     # Amber / Orange
COLOR_DANGER = "#ef4444"      # Red
PALETTE = ["#3b82f6", "#10b981", "#6366f1", "#f59e0b", "#ec4899", "#14b8a6", "#8b5cf6"]

tab_charts, tab_trends, tab_data = st.tabs(["📊 Executive Visualizations", "📈 Monthly Trends", "📋 Data Explorer & Export"])

with tab_charts:
    # Row 1: Category Analysis (Sales & Profit)
    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="card-header">1. Sales by Category</div>', unsafe_allow_html=True)
        cat_sales = (
            df_filtered.groupby("Category")["Sales"]
            .sum()
            .reset_index()
            .sort_values("Sales", ascending=False)
        )
        fig_cat_sales = px.bar(
            cat_sales,
            x="Category",
            y="Sales",
            text_auto=".2s",
            color="Category",
            color_discrete_sequence=PALETTE,
        )
        fig_cat_sales.update_layout(
            showlegend=False,
            height=340,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis_title="Sales (₹)",
            xaxis_title="Category",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_cat_sales, use_container_width=True)

    with c2:
        st.markdown('<div class="card-header">2. Profit by Category</div>', unsafe_allow_html=True)
        cat_profit = (
            df_filtered.groupby("Category")["Profit"]
            .sum()
            .reset_index()
            .sort_values("Profit", ascending=False)
        )
        fig_cat_profit = px.bar(
            cat_profit,
            x="Category",
            y="Profit",
            text_auto=".2s",
            color="Category",
            color_discrete_sequence=PALETTE,
        )
        fig_cat_profit.update_layout(
            showlegend=False,
            height=340,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis_title="Profit (₹)",
            xaxis_title="Category",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_cat_profit, use_container_width=True)

    st.markdown("<hr style='margin: 20px 0; border-color: #e2e8f0;'>", unsafe_allow_html=True)

    # Row 2: Region & Payment Method
    c3, c4 = st.columns(2)

    with c3:
        st.markdown('<div class="card-header">3. Sales by Region</div>', unsafe_allow_html=True)
        region_sales = (
            df_filtered.groupby("Region")["Sales"]
            .sum()
            .reset_index()
            .sort_values("Sales", ascending=False)
        )
        fig_region = px.bar(
            region_sales,
            x="Region",
            y="Sales",
            text_auto=".2s",
            color="Region",
            color_discrete_sequence=["#2563eb", "#059669", "#d97706", "#7c3aed"],
        )
        fig_region.update_layout(
            showlegend=False,
            height=340,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis_title="Sales (₹)",
            xaxis_title="Region",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_region, use_container_width=True)

    with c4:
        st.markdown('<div class="card-header">7. Payment Method-wise Sales</div>', unsafe_allow_html=True)
        pay_sales = (
            df_filtered.groupby("Payment_Method")["Sales"]
            .sum()
            .reset_index()
            .sort_values("Sales", ascending=False)
        )
        fig_pay = px.pie(
            pay_sales,
            names="Payment_Method",
            values="Sales",
            hole=0.45,
            color_discrete_sequence=PALETTE,
        )
        fig_pay.update_traces(textinfo="percent+label", hoverinfo="label+value+percent")
        fig_pay.update_layout(
            height=340,
            margin=dict(l=20, r=20, t=30, b=20),
            showlegend=True,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_pay, use_container_width=True)

    st.markdown("<hr style='margin: 20px 0; border-color: #e2e8f0;'>", unsafe_allow_html=True)

    # Row 3: Product Breakdown
    st.markdown('<div class="card-header">4. Sales by Product</div>', unsafe_allow_html=True)
    prod_sales = (
        df_filtered.groupby("Product")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=True)
    )
    fig_prod = px.bar(
        prod_sales,
        x="Sales",
        y="Product",
        orientation="h",
        text_auto=".2s",
        color="Sales",
        color_continuous_scale="Viridis",
    )
    fig_prod.update_layout(
        showlegend=False,
        height=380,
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis_title="Total Sales (₹)",
        yaxis_title="Product",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig_prod, use_container_width=True)


with tab_trends:
    # Monthly Trends (Sales & Profit)
    # Group by Month order
    months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    monthly_agg = (
        df_filtered.groupby(["Month_Num", "Month_Name"])[["Sales", "Profit"]]
        .sum()
        .reset_index()
        .sort_values("Month_Num")
    )
    
    t1, t2 = st.columns(2)

    with t1:
        st.markdown('<div class="card-header">5. Monthly Sales Trend</div>', unsafe_allow_html=True)
        fig_m_sales = px.line(
            monthly_agg,
            x="Month_Name",
            y="Sales",
            markers=True,
            line_shape="spline",
            color_discrete_sequence=["#2563eb"],
        )
        fig_m_sales.update_traces(line_width=3, marker_size=8)
        fig_m_sales.update_layout(
            height=360,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis_title="Sales (₹)",
            xaxis_title="Month",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_m_sales, use_container_width=True)

    with t2:
        st.markdown('<div class="card-header">6. Monthly Profit Trend</div>', unsafe_allow_html=True)
        fig_m_profit = px.line(
            monthly_agg,
            x="Month_Name",
            y="Profit",
            markers=True,
            line_shape="spline",
            color_discrete_sequence=["#059669"],
        )
        fig_m_profit.update_traces(line_width=3, marker_size=8)
        fig_m_profit.update_layout(
            height=360,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis_title="Profit (₹)",
            xaxis_title="Month",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_m_profit, use_container_width=True)

    # Dual Overlay Trend Chart
    st.markdown("<hr style='margin: 20px 0; border-color: #e2e8f0;'>", unsafe_allow_html=True)
    st.markdown('<div class="card-header">📊 Combined Monthly Sales vs Profit Comparison</div>', unsafe_allow_html=True)
    
    fig_dual = px_go.Figure()
    fig_dual.add_trace(px_go.Scatter(
        x=monthly_agg["Month_Name"], y=monthly_agg["Sales"],
        mode="lines+markers", name="Sales",
        line=dict(color="#2563eb", width=3)
    ))
    fig_dual.add_trace(px_go.Scatter(
        x=monthly_agg["Month_Name"], y=monthly_agg["Profit"],
        mode="lines+markers", name="Profit",
        line=dict(color="#059669", width=3)
    ))
    fig_dual.update_layout(
        height=380,
        margin=dict(l=20, r=20, t=30, b=20),
        yaxis_title="Amount (₹)",
        xaxis_title="Month",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig_dual, use_container_width=True)


with tab_data:
    st.markdown('<div class="card-header">🔍 Interactive Dataset Explorer</div>', unsafe_allow_html=True)
    
    # Search / Quick Filter
    search_term = st.text_input("Search Orders, Products, Cities, etc.", "")
    
    df_display = df_filtered.copy()
    if search_term:
        mask = df_display.astype(str).apply(lambda row: row.str.contains(search_term, case=False).any(), axis=1)
        df_display = df_display[mask]

    st.write(f"Displaying **{len(df_display)}** of **{len(df_raw)}** total order records.")
    
    df_table = df_display[["Order_ID", "Order_Date", "Product", "Category", "City", "Region", "Quantity", "Unit_Price", "Discount", "Sales", "Profit", "Payment_Method"]].copy()
    df_table["Order_Date"] = df_table["Order_Date"].dt.strftime("%Y-%m-%d")

    st.dataframe(
        df_table,
        use_container_width=True,
        height=400
    )

    # Download Filtered CSV
    csv_bytes = df_display.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Dataset (CSV)",
        data=csv_bytes,
        file_name="filtered_sales_data.csv",
        mime="text/csv",
    )
