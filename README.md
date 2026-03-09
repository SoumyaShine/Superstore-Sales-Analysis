# 📊 Superstore Sales & Profit Analysis

A data analysis project built using **Python** and **Power BI** to analyze sales performance, profitability, and discount impact across product categories and regions.

---

## 📌 Project Overview

This project analyzes the popular Superstore Sales dataset to uncover key business insights that can help improve profitability and guide business decisions.

**Key questions answered:**
- Which product categories generate the most sales and profit?
- Which sub-categories are losing money?
- How do discounts impact profitability?
- Which regions and customer segments perform best?

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python | Data cleaning, analysis, chart generation |
| Pandas | Data manipulation and aggregation |
| Matplotlib & Seaborn | Data visualization |
| Power BI | Interactive dashboard creation |

---

## 📂 Project Structure

```
Superstore-Sales-Analysis/
│
├── data/
│   ├── SampleSuperstore.csv        # Original dataset
│   └── cleaned_superstore.csv      # Cleaned dataset (used in Power BI)
│
├── charts/
│   ├── chart1_sales_by_category.png
│   ├── chart2_profit_by_subcategory.png
│   ├── chart3_discount_vs_profit.png
│   ├── chart4_sales_by_region.png
│   ├── chart5_sales_by_segment.png
│   └── chart6_profit_margin.png
│
├── dashboard/
│   └── dashboard.png               # Power BI dashboard screenshot
│
├── superstore_analysis.py          # Main Python analysis script
└── README.md
```

---

## 📈 Power BI Dashboard

![Dashboard](dashboard/dashboard.png)

**Dashboard features:**
- KPI Cards — Total Sales, Total Profit, Profit Margin %
- Sales by Category — bar chart with distinct colors
- Profit by Sub-Category — red/green conditional coloring
- Discount vs Profit Impact — scatter plot showing negative correlation
- Sales by Region — regional performance comparison
- Interactive slicers — filter by Category, Region, and Segment

---

## 🔍 Key Insights

**1. Technology is the most profitable category**
- Highest sales ($836K) and highest profit ($145K)
- Lowest average discount rate (13%)

**2. Furniture has high sales but very low profit**
- $741K in sales but only $18K profit
- Heavy discounting (17% average) is hurting margins

**3. Tables and Bookcases are loss-making**
- Tables: -$17,725 profit
- Bookcases: -$3,472 profit
- These sub-categories need urgent pricing review

**4. Discounts strongly hurt profitability**
- Discount-Profit correlation: -0.22
- Products with 50%+ discounts almost always generate losses
- Binders with high discounts are among worst performers

**5. West region leads in both sales and profit**
- West: $725K sales, $108K profit
- South has lowest sales ($391K) and needs attention

---

## ⚙️ How to Run

1. Clone this repository
2. Install required libraries:
```bash
pip install pandas matplotlib seaborn
```
3. Place `SampleSuperstore.csv` in the same folder
4. Run the analysis script:
```bash
python superstore_analysis.py
```
5. 6 chart PNG files and `cleaned_superstore.csv` will be generated
6. Open Power BI → load `cleaned_superstore.csv` → click Refresh

---

## 📊 Dataset

- **Source:** Superstore Sales Dataset (widely available on Kaggle)
- **Rows:** 9,994 (9,977 after removing 17 duplicates)
- **Columns:** 13 (Ship Mode, Segment, Region, Category, Sub-Category, Sales, Profit, Discount, Quantity, etc.)
- **No missing values** found in dataset

---

## 💡 Business Recommendations

1. **Reduce discounts** on Furniture — especially Tables and Bookcases
2. **Increase focus** on Technology products — highest profit margin
3. **Investigate Binders** — very high discount rates causing losses
4. **Target West region** strategies for other regions to replicate success
5. **Review pricing** for loss-making sub-categories before next quarter

---

## 👤 Author

**Soumya Malhotra**  
MCA Graduate | Aspiring Data Analyst  
📧 [Your Email]  
🔗 [Your LinkedIn URL]

---

*This project was built as part of my data analytics portfolio to demonstrate skills in Python, data cleaning, visualization, and business intelligence using Power BI.*
