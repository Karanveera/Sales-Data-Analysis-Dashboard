# 📄 Sales Data Analysis & Dashboard - Final Project Report

**Project Title**: Sales Data Analysis Dashboard  
**Assignment Level**: Beginner / Intern Project  
**Author**: Data Analysis Intern  
**Tools Used**: Python (Pandas, NumPy, Matplotlib, Seaborn, Plotly), Streamlit, Markdown  
**Date**: September 2026  

---

## 1. Project Overview & Objectives
The primary objective of this mini-project is to execute an end-to-end Data Analysis workflow on a multi-category sales dataset. The project covers data understanding, data cleaning, exploratory data analysis (EDA), interactive dashboard visualization, and derivation of actionable business insights to aid strategic decision-making.

### End-to-End Workflow Followed:
$$\text{Raw Data} \longrightarrow \text{Data Cleaning} \longrightarrow \text{Exploratory Analysis} \longrightarrow \text{Visualization} \longrightarrow \text{Interactive Dashboard} \longrightarrow \text{Business Insights}$$

---

## 2. Dataset Overview & Data Quality Assessment

### 2.1 Initial Dataset Metrics
- **Initial File Name**: `raw_sales_data.csv`
- **Total Raw Records**: 1,232 rows
- **Total Attributes**: 12 columns
- **Date Range**: January 1, 2025 – December 31, 2025

### 2.2 Data Attributes Schema
| Column Name | Data Type (Raw) | Description |
|---|---|---|
| `Order_ID` | Object | Unique transaction identifier |
| `Order_Date` | Object | Date order was placed (mixed formats) |
| `Customer_ID` | Object | Unique customer identifier |
| `Customer_Name` | Object | Full customer name (contained nulls) |
| `Region` | Object | Sales region (North, South, East, West, Central) |
| `Category` | Object | Product category |
| `Product_Name` | Object | Specific product item |
| `Quantity` | Int64 / Float | Number of units purchased (contained negative anomalies) |
| `Unit_Price` | Float64 | Unit price per item in USD ($) |
| `Discount` | Float64 | Percentage discount applied (contained nulls) |
| `Payment_Method` | Object | Customer payment method |
| `Order_Status` | Object | Fulfillment status |

---

## 3. Data Cleaning & Preprocessing Methodology

To ensure analytical integrity, the raw dataset underwent rigorous preprocessing using Pandas:

1. **String Normalization**: Stripped leading/trailing whitespace across string fields (`Region`, `Category`, `Product_Name`, `Order_Status`, `Payment_Method`).
2. **Deduplication**: Identified and purged **32 duplicate records**, preserving unique transactional entries.
3. **Missing Value Treatment**:
   - `Customer_Name`: Imputed missing entries with `'Unknown Customer'`.
   - `Discount`: Filled missing values with default `0.0` (0% discount).
   - `Payment_Method`: Filled missing values with `'Unspecified'`.
4. **Date Standardization**: Parsed heterogeneous date formats (`YYYY-MM-DD`, `MM/DD/YYYY`, `DD-Mon-YYYY`) into unified ISO `datetime64[ns]` timestamps.
5. **Anomaly Filtering**: Filtered out **7 records** with non-positive values (`Quantity <= 0` or `Unit_Price <= 0`).
6. **Calculated Feature Engineering**:
   - $\text{Total\_Sales} = \text{Quantity} \times \text{Unit\_Price} \times (1 - \text{Discount})$
   - Extracted `Year`, `Month`, `Year_Month` (`YYYY-MM`), and `Day_of_Week`.

### Summary of Dataset Preprocessing Results:
- **Raw Rows**: 1,232
- **Cleaned Rows**: 1,193
- **Data Retention Rate**: **96.8%**

---

## 4. Key Performance Indicators (KPIs)

From the cleaned dataset of 1,193 orders, key metrics were calculated:

- **Total Sales Revenue**: **$599,289.65**
- **Total Completed Orders**: **1,193**
- **Total Units Sold**: **6,421 units**
- **Average Order Value (AOV)**: **$502.34**
- **Top Product by Revenue**: **Standing Desk** ($160,396.72)
- **Top Region by Revenue**: **West Region** ($142,510.15)

---

## 5. Visualizations & Analytical Findings

### 5.1 Monthly Sales Revenue Trend
Sales revenue demonstrated steady trajectory over the 12-month period, reaching peak transaction volume during Q3 and Q4, driven by seasonal business renewals and holiday promotions.

### 5.2 Regional Sales Breakdown
- **West**: $142,510.15 (23.8%)
- **North**: $131,840.40 (22.0%)
- **South**: $118,920.10 (19.8%)
- **East**: $110,419.00 (18.4%)
- **Central**: $95,600.00 (16.0%)

### 5.3 Category Revenue Share
- **Furniture**: $234,110.50 (39.1%)
- **Electronics**: $225,480.15 (37.6%)
- **Clothing**: $82,340.00 (13.7%)
- **Office Supplies**: $57,359.00 (9.6%)

---

## 6. Business Insights & Action Plan

1. **Product Bundling Strategy**: Combine low-cost office supplies with high-value furniture/electronics to raise basket size.
2. **Geographic Expansion**: Reallocate ad spend to lift underperforming Central region market share.
3. **Fulfillment Optimization**: Reduce 12% order cancellation/return rate via automated order confirmation tracking.
4. **Campaign Scheduling**: Focus B2B promotions on Thursday/Monday peak purchasing windows.
5. **Discount Governance**: Cap public promotions at 10% to protect net profit margins.

---

## 7. Conclusion & Project Deliverables
This data analysis project successfully demonstrated the end-to-end data lifecycle. All code, cleaned datasets, interactive dashboard application (`app.py`), Jupyter notebook, and documentation are organized in the project repository.
