# Sales Data Analysis & Executive Dashboard

## 📌 Project Overview
This project performs an end-to-end analysis of sales data using Python, Pandas, Matplotlib, Streamlit, and Chart.js. The codebase is organized into a clean, modular architecture with dedicated modules for data loading, sales performance, profit margins, quantity breakdowns, top performer tracking, and visual dashboards.

---

## 📊 Dashboard Features & Key Metrics

### Mandatory KPIs:
1. **Total Sales**: `₹28,827,073.00`
2. **Total Profit**: `₹6,461,656.66` (**22.4% Profit Margin**)
3. **Total Quantity**: `2,998 Units`
4. **Number of Products**: `10 Products`
5. **Number of Orders**: `1,000 Orders`

### 📈 Included Charts (7 Required Visualizations):
1. **Sales by Category** (Bar chart)
2. **Profit by Category** (Bar chart)
3. **Sales by Region** (Bar chart across West, East, South, North)
4. **Sales by Product** (Horizontal Bar chart sorted descending)
5. **Monthly Sales Trend** (Line trend for Jan – Dec)
6. **Monthly Profit Trend** (Line trend for Jan – Dec)
7. **Payment Method-wise Sales** (Donut chart for payment channels)

### 🎛️ Interactive Filters & Slicers:
- **Category**
- **Region**
- **Product**
- **Payment Method**
- **Date / Month**

---

## 🚀 How to Run

### 1. Launch Interactive Streamlit Dashboard
```bash
python main.py --dashboard
```
*or*
```bash
streamlit run app.py
```

### 2. Launch Standalone Web Dashboard in Browser
```bash
python main.py --html-dashboard
```

### 3. Run Standard Modular CLI Analysis
```bash
python main.py
```

---

## 👨‍💻 Author
**Mohamed Amsathkhan**
