# 📊 Superstore Sales & Profit Analysis

Identified a **₹14.8L revenue leak** across product lines by analyzing 
9,977 sales transactions — uncovering exactly where the business was 
silently losing money and quantifying the impact of aggressive 
discounting on profitability.

---

## 📌 Project Overview

This project digs into the Superstore Sales dataset to answer one core 
business question: **Why is this company losing money despite high sales?**

**Key questions answered:**
- Which product categories generate the most sales AND profit?
- Which sub-categories are silently draining profit?
- How much money are discounts actually costing the business?
- Which regions and segments drive the most value?

---

## 💰 Business Impact Summary

| Finding | Impact |
|---------|--------|
| Tables sub-category losing money | -$17,725 profit (₹14.8L loss) |
| Bookcases sub-category losing money | -$3,472 profit |
| Discount-Profit correlation proved | -0.22 (discounts hurt profit) |
| Technology margin vs Furniture | 17.4% vs 2.5% — 7x difference |

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
│   ├── SampleSuperstore.csv
│   └── cleaned_superstore.csv
│
├── charts/
│   ├── chart1_sales_by_category.png
│   ├── chart2_profit_by_subcategory.png
│   ├── chart3_discount_vs_profit.png
│   ├── chart4_sales_by_region.png
│   ├── chart5_sales_by_segment.png
│   └── chart6_profit_margin.png
│
├── superstore_analysis.py
└── README.md
```

---

## 📈 Power BI Dashboard

**Dashboard features:**
- KPI Cards — Total Sales ($2.3M), Total Profit ($286K), Profit Margin (12.47%)
- Profit by Sub-Category — red/green conditional coloring revealing loss-makers
- Discount vs Profit scatter — visually proving negative correlation
- Sales by Category and Region — performance breakdown
- Interactive slicers — filter by Category, Region, and Segment instantly

---

## 🔍 Key Insights

**1. ₹14.8L Revenue Leak Found — Tables and Bookcases**
- Tables: -$17,725 profit despite strong sales volume
- Bookcases: -$3,472 profit
- Root cause: excessive discounting (avg 17%+ on Furniture)
- Recommendation: immediate pricing review on these sub-categories

**2. Discounts Are Destroying Profit**
- Proved -0.22 correlation between discount rate and profit
- Products with 50%+ discounts almost always generate losses
- Binders at 80% discount = worst performing product

**3. Technology Is the Clear Winner**
- $836K sales, $145K profit, 17.4% margin
- Lowest average discount rate (13%)
- Should be the growth focus for the business

**4. Furniture Has a Fundamental Problem**
- $741K in sales but only $18K profit (2.5% margin)
- 7x less profitable than Technology
- Heavy discounting strategy is not sustainable

**5. West Region Leads, South Needs Attention**
- West: $725K sales, $108K profit
- South: $391K sales — lowest performing region

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

- **Source:** Superstore Sales Dataset (Kaggle)
- **Rows:** 9,994 (9,977 after removing 17 duplicates)
- **Columns:** 13 including Sales, Profit, Discount, Category, Region

---

## 💡 Business Recommendations

1. **Stop excessive discounting** on Tables and Bookcases immediately
2. **Shift focus to Technology** — 7x more profitable than Furniture
3. **Cap discounts at 20%** — data shows anything above hurts profitability
4. **Replicate West region strategy** in South and Central regions
5. **Discontinue or reprice** loss-making sub-categories next quarter

---

## 👤 Author

**Soumya Malhotra**
MCA Graduate | Aspiring Data Analyst
📧 soumyamalhotra1720@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/soumya-malhotra1720)
🔗 [GitHub](https://github.com/SoumyaShine)
