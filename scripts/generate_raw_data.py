import os
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_raw_sales_data(output_path, num_records=1200):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    random.seed(42)
    np.random.seed(42)

    categories_products = {
        'Electronics': [
            ('Wireless Headphones', 99.99),
            ('Smart Watch', 199.99),
            ('Bluetooth Speaker', 49.99),
            ('4K Monitor', 349.99),
            ('USB-C Hub', 29.99),
            ('Mechanical Keyboard', 89.99)
        ],
        'Furniture': [
            ('Ergonomic Office Chair', 249.99),
            ('Standing Desk', 499.99),
            ('Bookshelf', 119.99),
            ('Desk Lamp', 34.99),
            ('File Cabinet', 89.99)
        ],
        'Office Supplies': [
            ('Paper Reams (5-Pack)', 24.99),
            ('Gel Pen Set (12-pack)', 12.99),
            ('Whiteboard Markers', 8.99),
            ('Stapler & Clips Set', 14.99),
            ('Notebook Pack', 18.99)
        ],
        'Clothing': [
            ('Cotton Hoodie', 45.00),
            ('Running Shoes', 85.00),
            ('Casual Polo Shirt', 32.00),
            ('Winter Jacket', 120.00),
            ('Denim Jeans', 55.00)
        ]
    }

    regions = ['North', 'South', 'East', 'West', 'Central']
    payment_methods = ['Credit Card', 'PayPal', 'Debit Card', 'Bank Transfer', 'Cash']
    statuses = ['Completed', 'Completed', 'Completed', 'Completed', 'Shipped', 'Returned', 'Cancelled']
    
    first_names = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Sam', 'Chris', 'Pat', 'Riley', 'Casey', 'Avery', 'Dakota', 'Reese', 'Quinn', 'Skyler', 'Cameron']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez']

    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)
    date_delta = (end_date - start_date).days

    data = []
    
    for i in range(1, num_records + 1):
        order_id = f"ORD-{10000 + i}"
        
        # Date generation with occasional string format variation
        random_days = random.randint(0, date_delta)
        order_date_dt = start_date + timedelta(days=random_days)
        
        # Inject inconsistent date formats
        rand_fmt = random.random()
        if rand_fmt < 0.70:
            order_date_str = order_date_dt.strftime('%Y-%m-%d')
        elif rand_fmt < 0.88:
            order_date_str = order_date_dt.strftime('%m/%d/%Y')
        else:
            order_date_str = order_date_dt.strftime('%d-%b-%Y')

        cust_id = f"CUST-{random.randint(101, 350):04d}"
        cust_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        
        # 4% chance of missing customer name
        if random.random() < 0.04:
            cust_name = None

        category = random.choice(list(categories_products.keys()))
        product, base_price = random.choice(categories_products[category])
        
        # Trailing spaces in region or category occasionally
        region = random.choice(regions)
        if random.random() < 0.05:
            region = region + " "
        if random.random() < 0.05:
            category = " " + category

        quantity = random.randint(1, 10)
        # Minor anomaly: negative quantity or price error (0.5% chance)
        if random.random() < 0.005:
            quantity = -1 * quantity

        unit_price = base_price
        
        discount = round(random.choice([0.0, 0.05, 0.10, 0.15, 0.20, 0.25]), 2)
        # 5% missing discount
        if random.random() < 0.05:
            discount = np.nan

        payment = random.choice(payment_methods)
        # 3% missing payment method
        if random.random() < 0.03:
            payment = None

        status = random.choice(statuses)

        data.append({
            'Order_ID': order_id,
            'Order_Date': order_date_str,
            'Customer_ID': cust_id,
            'Customer_Name': cust_name,
            'Region': region,
            'Category': category,
            'Product_Name': product,
            'Quantity': quantity,
            'Unit_Price': unit_price,
            'Discount': discount,
            'Payment_Method': payment,
            'Order_Status': status
        })

    df = pd.DataFrame(data)

    # Inject explicit duplicate rows (approx 30 duplicates)
    duplicate_rows = df.sample(n=32, random_state=42)
    df = pd.concat([df, duplicate_rows], ignore_index=True)

    # Shuffle dataset
    df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)

    df.to_csv(output_path, index=False)
    print(f"Generated raw sales dataset with {len(df)} records at {output_path}")

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    generate_raw_sales_data(os.path.join(out_dir, "raw_sales_data.csv"))
