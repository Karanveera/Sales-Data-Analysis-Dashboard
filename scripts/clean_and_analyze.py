import os
import json
import pandas as pd
import numpy as np

def clean_and_analyze_sales_data(raw_path, cleaned_path, summary_json_path):
    print("--- Starting Data Cleaning & Analysis Pipeline ---")
    
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw dataset not found at {raw_path}. Run generate_raw_data.py first.")
    
    df_raw = pd.read_csv(raw_path)
    initial_shape = df_raw.shape
    print(f"Loaded Raw Dataset: {initial_shape[0]} rows, {initial_shape[1]} columns")

    # 1. Identify Data Quality Issues
    initial_duplicates = df_raw.duplicated().sum()
    initial_nulls = df_raw.isnull().sum().to_dict()
    print(f"Initial Duplicates Found: {initial_duplicates}")
    print(f"Initial Null Counts: {initial_nulls}")

    df = df_raw.copy()

    # 2. String Whitespace Cleaning
    string_cols = ['Region', 'Category', 'Product_Name', 'Order_Status', 'Payment_Method', 'Customer_Name']
    for col in string_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].replace({'nan': np.nan, 'None': np.nan, '': np.nan})

    # 3. Deduplication
    df = df.drop_duplicates().reset_index(drop=True)
    dedup_shape = df.shape
    print(f"Rows after removing duplicates: {dedup_shape[0]} (Removed {initial_duplicates} duplicates)")

    # 4. Handle Missing Values
    df['Customer_Name'] = df['Customer_Name'].fillna('Unknown Customer')
    df['Discount'] = df['Discount'].fillna(0.0)
    df['Payment_Method'] = df['Payment_Method'].fillna('Unspecified')

    # 5. Date Parsing & Standardization
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='mixed', errors='coerce')
    missing_dates = df['Order_Date'].isnull().sum()
    if missing_dates > 0:
        print(f"Warning: {missing_dates} dates could not be parsed. Dropping rows with invalid dates.")
        df = df.dropna(subset=['Order_Date']).reset_index(drop=True)

    # 6. Data Type & Anomaly Correction
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')
    df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')

    # Remove invalid non-positive quantity or price anomalies
    anomaly_rows = df[(df['Quantity'] <= 0) | (df['Unit_Price'] <= 0)]
    print(f"Anomalous records (Quantity <= 0 or Unit_Price <= 0): {len(anomaly_rows)}")
    df = df[(df['Quantity'] > 0) & (df['Unit_Price'] > 0)].reset_index(drop=True)

    # 7. Feature Engineering
    # Total_Sales = Quantity * Unit_Price * (1 - Discount)
    df['Total_Sales'] = (df['Quantity'] * df['Unit_Price'] * (1 - df['Discount'])).round(2)
    df['Year'] = df['Order_Date'].dt.year
    df['Month'] = df['Order_Date'].dt.month
    df['Month_Name'] = df['Order_Date'].dt.strftime('%b')
    df['Year_Month'] = df['Order_Date'].dt.strftime('%Y-%m')
    df['Day_of_Week'] = df['Order_Date'].dt.day_name()

    # Save Cleaned Dataset
    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned dataset saved successfully to {cleaned_path} with {len(df)} rows.")

    # 8. Analytical Summaries & KPI Calculations
    total_sales = round(float(df['Total_Sales'].sum()), 2)
    total_orders = int(df['Order_ID'].nunique())
    total_units_sold = int(df['Quantity'].sum())
    avg_order_value = round(total_sales / total_orders, 2) if total_orders > 0 else 0
    total_customers = int(df['Customer_ID'].nunique())

    # Filter for Completed / Shipped orders if needed for analysis
    valid_sales_df = df[df['Order_Status'].isin(['Completed', 'Shipped'])]
    effective_sales = round(float(valid_sales_df['Total_Sales'].sum()), 2)

    # Top Selling Products
    top_products = df.groupby('Product_Name').agg(
        Total_Revenue=('Total_Sales', 'sum'),
        Units_Sold=('Quantity', 'sum'),
        Order_Count=('Order_ID', 'nunique')
    ).reset_index().sort_values(by='Total_Revenue', ascending=False).head(5)

    # Regional Sales Breakdown
    regional_sales = df.groupby('Region').agg(
        Total_Sales=('Total_Sales', 'sum'),
        Order_Count=('Order_ID', 'nunique')
    ).reset_index().sort_values(by='Total_Sales', ascending=False)

    # Category Sales Breakdown
    category_sales = df.groupby('Category').agg(
        Total_Sales=('Total_Sales', 'sum'),
        Order_Count=('Order_ID', 'nunique')
    ).reset_index().sort_values(by='Total_Sales', ascending=False)

    # Monthly Sales Trend
    monthly_sales = df.groupby(['Year_Month', 'Month_Name']).agg(
        Total_Sales=('Total_Sales', 'sum'),
        Order_Count=('Order_ID', 'nunique')
    ).reset_index().sort_values(by='Year_Month')

    summary_metrics = {
        'initial_raw_records': initial_shape[0],
        'cleaned_records': len(df),
        'duplicates_removed': int(initial_duplicates),
        'total_sales_revenue': total_sales,
        'effective_completed_sales_revenue': effective_sales,
        'total_orders': total_orders,
        'total_units_sold': total_units_sold,
        'average_order_value': avg_order_value,
        'total_customers': total_customers,
        'top_products': top_products.to_dict(orient='records'),
        'regional_sales': regional_sales.to_dict(orient='records'),
        'category_sales': category_sales.to_dict(orient='records'),
        'monthly_sales': monthly_sales.to_dict(orient='records')
    }

    os.makedirs(os.path.dirname(summary_json_path), exist_ok=True)
    with open(summary_json_path, 'w') as f:
        json.dump(summary_metrics, f, indent=4)
        
    print("--- Pipeline Completed Successfully ---")
    print(f"Summary KPI Metrics:")
    print(f"  Total Sales Revenue: ${total_sales:,.2f}")
    print(f"  Total Orders: {total_orders:,}")
    print(f"  Average Order Value: ${avg_order_value:,.2f}")
    print(f"  Top Product by Revenue: {top_products.iloc[0]['Product_Name']} (${top_products.iloc[0]['Total_Revenue']:,.2f})")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_p = os.path.join(base_dir, "data", "raw_sales_data.csv")
    cleaned_p = os.path.join(base_dir, "data", "cleaned_sales_data.csv")
    summary_p = os.path.join(base_dir, "reports", "summary_metrics.json")
    
    clean_and_analyze_sales_data(raw_p, cleaned_p, summary_p)
