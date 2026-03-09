"""
====================================================
  Superstore Sales & Profit Analysis
  Tools  : Python, Pandas, Matplotlib, Seaborn
  Dataset: SampleSuperstore.csv (9,994 rows)
  Columns: Ship Mode, Segment, Country, City, State,
           Postal Code, Region, Category, Sub-Category,
           Sales, Quantity, Discount, Profit
====================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# ─────────────────────────────────────────────────
# SECTION 1 — LOAD DATASET
# ─────────────────────────────────────────────────

df = pd.read_csv("SampleSuperstore.csv", encoding='latin-1')

print("=" * 50)
print("STEP 1: Dataset Loaded")
print(f"  Rows: {df.shape[0]}  |  Columns: {df.shape[1]}")
print("=" * 50)


# ─────────────────────────────────────────────────
# SECTION 2 — DATA CLEANING
# ─────────────────────────────────────────────────
# Check and remove duplicate rows.
# This dataset has no missing values, but we verify
# that to be safe before doing any analysis.

print("\nSTEP 2: Data Cleaning")

# 2a. Check for missing values
missing = df.isnull().sum()
if missing.sum() == 0:
    print("  ✓ No missing values found.")
else:
    print(f"  Missing values found:\n{missing[missing > 0]}")
    df.dropna(inplace=True)

# 2b. Remove duplicate rows (17 found in this dataset)
dupes = df.duplicated().sum()
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)
print(f"  Duplicate rows removed: {dupes}")
print(f"  ✓ Clean dataset: {df.shape[0]} rows remaining.")


# ─────────────────────────────────────────────────
# SECTION 3 — FEATURE ENGINEERING
# ─────────────────────────────────────────────────
# Creating a new useful column from existing data.
# Profit Margin tells us how much profit we earn
# for every dollar of sales — very useful for business.

df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100

print("\nSTEP 3: New column created → Profit Margin (%)")


# ─────────────────────────────────────────────────
# SECTION 4 — CORE BUSINESS METRICS
# ─────────────────────────────────────────────────

total_sales   = df['Sales'].sum()
total_profit  = df['Profit'].sum()
total_orders  = df.shape[0]
avg_discount  = df['Discount'].mean()
profit_margin = (total_profit / total_sales) * 100
correlation   = df['Discount'].corr(df['Profit'])

print("\n" + "=" * 50)
print("STEP 4: Core Business Metrics")
print("=" * 50)
print(f"  Total Sales          : ${total_sales:,.2f}")
print(f"  Total Profit         : ${total_profit:,.2f}")
print(f"  Total Transactions   : {total_orders}")
print(f"  Average Discount     : {avg_discount:.1%}")
print(f"  Overall Profit Margin: {profit_margin:.2f}%")
print(f"  Discount-Profit Corr : {correlation:.4f}  (negative = discounts hurt profit)")


# ─────────────────────────────────────────────────
# SECTION 5 — AGGREGATED INSIGHTS
# ─────────────────────────────────────────────────

# Sales and profit grouped by Category
category_summary = df.groupby('Category').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Avg_Discount=('Discount', 'mean')
).sort_values('Total_Sales', ascending=False)

# Sales and profit grouped by Region
region_summary = df.groupby('Region').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum')
).sort_values('Total_Sales', ascending=False)

# Sales by customer Segment (Consumer / Corporate / Home Office)
segment_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

# Profit by Sub-Category sorted low to high (to spot losses easily)
subcategory_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values()

# Top 10 worst loss-making individual transactions
loss_rows = df[df['Profit'] < 0].sort_values('Profit').head(10)[
    ['Category', 'Sub-Category', 'Sales', 'Discount', 'Profit']
]

print("\n\n----- Sales & Profit by Category -----")
print(category_summary.to_string())

print("\n----- Sales & Profit by Region -----")
print(region_summary.to_string())

print("\n----- Sales by Customer Segment -----")
print(segment_sales.to_string())

print("\n----- Profit by Sub-Category (Low to High) -----")
print(subcategory_profit.to_string())

print("\n----- Top 10 Worst Loss-Making Transactions -----")
print(loss_rows.to_string())


# ─────────────────────────────────────────────────
# SECTION 6 — VISUALIZATIONS
# ─────────────────────────────────────────────────
# 6 charts are generated and saved as PNG files.
# All charts use consistent colors and styling.

sns.set_theme(style='whitegrid', palette='muted')
TITLE_SIZE = 14
LABEL_SIZE = 11
COLOR_POS  = '#4CAF50'   # green → profit
COLOR_NEG  = '#F44336'   # red   → loss
COLOR_LIST = ['#2196F3', '#4CAF50', '#FF9800', '#9C27B0']

margins = (category_summary['Total_Profit'] / category_summary['Total_Sales'] * 100)

print("\nSTEP 6: Generating Charts...")

# ── Chart 1: Total Sales by Category ──────────────
fig, ax = plt.subplots(figsize=(7, 5))
cats  = category_summary.index.tolist()
sales = category_summary['Total_Sales'].tolist()
bars  = ax.bar(cats, sales, color=COLOR_LIST[:len(cats)], edgecolor='black', width=0.5)
# Value labels on top of each bar
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 5000,
            f"${bar.get_height()/1000:.0f}K",
            ha='center', fontsize=10, fontweight='bold')
ax.set_title("Total Sales by Category", fontsize=TITLE_SIZE, fontweight='bold')
ax.set_xlabel("Product Category", fontsize=LABEL_SIZE)
ax.set_ylabel("Total Sales ($)", fontsize=LABEL_SIZE)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
plt.tight_layout()
plt.savefig("chart1_sales_by_category.png", dpi=150)
plt.close()
print("  ✓ chart1_sales_by_category.png")


# ── Chart 2: Profit by Sub-Category (Red/Green) ───
# Red bars = loss-making sub-categories
colors = [COLOR_POS if v >= 0 else COLOR_NEG for v in subcategory_profit.values]
fig, ax = plt.subplots(figsize=(14, 6))
ax.bar(subcategory_profit.index, subcategory_profit.values, color=colors, edgecolor='black')
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_title("Profit by Sub-Category  (Green = Profit | Red = Loss)",
             fontsize=TITLE_SIZE, fontweight='bold')
ax.set_xlabel("Sub-Category", fontsize=LABEL_SIZE)
ax.set_ylabel("Total Profit ($)", fontsize=LABEL_SIZE)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("chart2_profit_by_subcategory.png", dpi=150)
plt.close()
print("  ✓ chart2_profit_by_subcategory.png")


# ── Chart 3: Discount vs Profit Scatter ───────────
# Negative trend line shows discounts reduce profit
fig, ax = plt.subplots(figsize=(8, 5))
sns.regplot(x='Discount', y='Profit', data=df,
            scatter_kws={'alpha': 0.3, 'color': '#2196F3'},
            line_kws={'color': COLOR_NEG, 'linewidth': 2}, ax=ax)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_title("Discount vs Profit  (Trend Line Shows Negative Impact)",
             fontsize=TITLE_SIZE, fontweight='bold')
ax.set_xlabel("Discount Rate", fontsize=LABEL_SIZE)
ax.set_ylabel("Profit ($)", fontsize=LABEL_SIZE)
plt.tight_layout()
plt.savefig("chart3_discount_vs_profit.png", dpi=150)
plt.close()
print("  ✓ chart3_discount_vs_profit.png")


# ── Chart 4: Sales by Region ──────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
reg_bars = ax.bar(region_summary.index, region_summary['Total_Sales'],
                  color=COLOR_LIST, edgecolor='black', width=0.5)
for bar in reg_bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 3000,
            f"${bar.get_height()/1000:.0f}K",
            ha='center', fontsize=10, fontweight='bold')
ax.set_title("Total Sales by Region", fontsize=TITLE_SIZE, fontweight='bold')
ax.set_xlabel("Region", fontsize=LABEL_SIZE)
ax.set_ylabel("Total Sales ($)", fontsize=LABEL_SIZE)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
plt.tight_layout()
plt.savefig("chart4_sales_by_region.png", dpi=150)
plt.close()
print("  ✓ chart4_sales_by_region.png")


# ── Chart 5: Sales by Customer Segment ────────────
# Shows which customer type drives most revenue
fig, ax = plt.subplots(figsize=(7, 5))
seg_bars = ax.bar(segment_sales.index, segment_sales.values,
                  color=['#2196F3', '#FF9800', '#9C27B0'], edgecolor='black', width=0.5)
for bar in seg_bars:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 5000,
            f"${bar.get_height()/1000:.0f}K",
            ha='center', fontsize=10, fontweight='bold')
ax.set_title("Total Sales by Customer Segment", fontsize=TITLE_SIZE, fontweight='bold')
ax.set_xlabel("Segment", fontsize=LABEL_SIZE)
ax.set_ylabel("Total Sales ($)", fontsize=LABEL_SIZE)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
plt.tight_layout()
plt.savefig("chart5_sales_by_segment.png", dpi=150)
plt.close()
print("  ✓ chart5_sales_by_segment.png")


# ── Chart 6: Profit Margin % by Category ──────────
# Shows how efficiently each category converts sales to profit
fig, ax = plt.subplots(figsize=(7, 5))
bar_colors = [COLOR_POS if v >= 0 else COLOR_NEG for v in margins]
ax.bar(margins.index, margins.values, color=bar_colors, edgecolor='black', width=0.5)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
for i, (cat, val) in enumerate(zip(margins.index, margins.values)):
    ax.text(i, val + 0.3, f"{val:.1f}%", ha='center', fontsize=11, fontweight='bold')
ax.set_title("Profit Margin % by Category", fontsize=TITLE_SIZE, fontweight='bold')
ax.set_xlabel("Category", fontsize=LABEL_SIZE)
ax.set_ylabel("Profit Margin (%)", fontsize=LABEL_SIZE)
plt.tight_layout()
plt.savefig("chart6_profit_margin.png", dpi=150)
plt.close()
print("  ✓ chart6_profit_margin.png")


# ─────────────────────────────────────────────────
# SECTION 7 — SAVE CLEANED DATASET FOR POWER BI
# ─────────────────────────────────────────────────
# This file is what you load into Power BI.
# After running this script, open Power BI and click Refresh.

df.to_csv("cleaned_superstore.csv", index=False)
print("  ✓ cleaned_superstore.csv saved — ready for Power BI refresh")

print("\n" + "=" * 50)
print("  Analysis Complete! All outputs generated.")
print("=" * 50)
