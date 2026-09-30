# 📊 Sales Data Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive%20Dashboard-red)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-purple)
![License](https://img.shields.io/badge/License-MIT-green)

A beginner-level end-to-end Data Analysis mini project completed as part of the Internship Assignment. This repository contains the complete pipeline: synthetic dataset generation with quality issues, automated data cleaning scripts, exploratory analysis notebook, interactive Streamlit sales dashboard, business insights report, project report, and presentation slides.

---

## 📌 Project Overview
The objective of this project is to analyze a multi-category sales dataset across 5 regions (North, South, East, West, Central) and 4 product categories (Electronics, Furniture, Office Supplies, Clothing), execute data cleaning workflows, calculate key KPIs, visualize sales performance, and generate actionable business recommendations.

---

## 📂 Project Repository Structure

```
sales_data_analysis_dashboard/
├── data/
│   ├── raw_sales_data.csv          # Raw generated dataset with duplicates & nulls
│   └── cleaned_sales_data.csv      # Cleaned & preprocessed sales dataset
├── scripts/
│   ├── generate_raw_data.py        # Python script to generate raw synthetic dataset
│   └── clean_and_analyze.py        # Data cleaning, KPI calculation & pipeline script
├── notebooks/
│   └── sales_analysis.ipynb        # Step-by-step EDA and matplotlib chart notebook
├── reports/
│   ├── BUSINESS_INSIGHTS.md        # 5+ detailed strategic business insights
│   ├── PROJECT_REPORT.md           # Full technical project report
│   └── summary_metrics.json        # JSON metrics summary for verification
├── presentation/
│   └── PRESENTATION.html           # Interactive HTML slide deck presentation
├── app.py                          # Streamlit interactive dashboard application
├── requirements.txt                # Python package dependencies
└── README.md                       # Main repository documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone or Download Repository
```bash
git clone https://github.com/your-username/sales_data_analysis_dashboard.git
cd sales_data_analysis_dashboard
```

### 2. Install Required Dependencies
Ensure you have Python 3.10+ installed, then run:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project Pipeline & Dashboard

### Step 1: Execute Data Pipeline
Generate the raw dataset and run the data cleaning script:
```bash
python scripts/generate_raw_data.py
python scripts/clean_and_analyze.py
```

### Step 2: Launch Interactive Streamlit Dashboard
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to view and interact with the dynamic dashboard filters and Plotly charts.

### Step 3: View Presentation Slide Deck
Open `presentation/PRESENTATION.html` in any web browser to view the interactive presentation slides.

---

## 📊 Key Performance Indicators (FY 2025)

| Metric | Value |
|---|---|
| **Total Sales Revenue** | **$599,289.65** |
| **Total Cleaned Orders** | **1,193** |
| **Average Order Value (AOV)** | **$502.34** |
| **Total Units Sold** | **6,421 units** |
| **Top Revenue Product** | **Standing Desk ($160,396.72)** |
| **Top Revenue Region** | **West Region ($142,510.15)** |

---

## 💡 Top Business Insights Summary

1. **Product Bundling Strategy**: Electronics and Furniture generate over **75%** of overall dollar revenue. Bundling low-cost consumables (office supplies) with standing desks or monitors will increase basket sizes.
2. **Regional Expansion**: The West and North regions lead overall sales by 30%+ over Central. Reallocating digital advertising to Central will help unlock untapped regional market share.
3. **Fulfillment & Cancellation Rates**: ~12% of gross orders were marked as Returned or Cancelled. Implementing post-purchase automated notifications will reduce order drop-offs.
4. **Day-of-Week Purchase Peaks**: Purchasing intent peaks on Fridays and Mondays. B2B marketing emails dispatched on Thursday afternoons align best with corporate buying windows.
5. **Discount Governance**: Cap baseline promotional discounts at 10% to prevent unnecessary profit margin erosion.

---

## 📜 Deliverables Checklist (per Internship Assignment PDF)

- [x] **Original Dataset** (`data/raw_sales_data.csv`)
- [x] **Cleaned Dataset** (`data/cleaned_sales_data.csv`)
- [x] **Analysis File / Python Notebook** (`notebooks/sales_analysis.ipynb`)
- [x] **Final Dashboard** (`app.py`)
- [x] **Minimum 5 Business Insights** (`reports/BUSINESS_INSIGHTS.md`)
- [x] **Project Report** (`reports/PROJECT_REPORT.md`)
- [x] **Final Presentation** (`presentation/PRESENTATION.html`)
- [x] **GitHub Repository Setup** (`README.md` & structure)
