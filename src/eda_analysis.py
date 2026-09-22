import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_excel("data/Online_Retail_Cleaned.xlsx")

print("Dataset loaded successfully!")

# Display dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())
# -----------------------------
# SALES ANALYSIS
# -----------------------------

print("\n--- SALES ANALYSIS ---")

# Total revenue
total_sales = df["TotalPrice"].sum()
print(f"Total Sales Revenue: £{total_sales:,.2f}")

# Total number of unique orders
total_orders = df["InvoiceNo"].nunique()
print(f"Total Orders: {total_orders}")

# Total number of unique customers
total_customers = df["CustomerID"].nunique()
print(f"Total Customers: {total_customers}")

# Average order value
sales_per_order = df.groupby("InvoiceNo")["TotalPrice"].sum()
average_order_value = sales_per_order.mean()

print(f"Average Order Value: £{average_order_value:,.2f}")

# Average quantity per transaction
average_quantity = df["Quantity"].mean()
print(f"Average Quantity: {average_quantity:.2f}")
# -----------------------------
# TOP 10 BEST-SELLING PRODUCTS
# -----------------------------

print("\n--- TOP 10 BEST-SELLING PRODUCTS ---")

top_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)
# -----------------------------
# TOP 10 PRODUCTS BY REVENUE
# -----------------------------

print("\n--- TOP 10 PRODUCTS BY SALES REVENUE ---")

top_revenue_products = (
    df.groupby("Description")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_revenue_products)
# -----------------------------
# COUNTRY-WISE SALES ANALYSIS
# -----------------------------

print("\n--- TOP 10 COUNTRIES BY SALES REVENUE ---")

country_sales = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(country_sales)
# -----------------------------
# MONTHLY SALES TREND
# -----------------------------

print("\n--- MONTHLY SALES TREND ---")

# Make sure InvoiceDate is in datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create a Month column
df["Month"] = df["InvoiceDate"].dt.to_period("M")

# Calculate total sales for each month
monthly_sales = (
    df.groupby("Month")["TotalPrice"]
    .sum()
)

print(monthly_sales)
# -----------------------------
# TOP 10 CUSTOMERS BY REVENUE
# -----------------------------

print("\n--- TOP 10 CUSTOMERS BY SALES REVENUE ---")

top_customers = (
    df.groupby("CustomerID")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)
# -----------------------------
# MONTHLY SALES TREND GRAPH
# -----------------------------

print("\nCreating Monthly Sales Trend Graph...")

# Convert Month index to string for plotting
monthly_sales_plot = monthly_sales.copy()
monthly_sales_plot.index = monthly_sales_plot.index.astype(str)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales_plot.index,
    monthly_sales_plot.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Revenue (£)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("outputs/monthly_sales_trend.png", dpi=300, bbox_inches="tight")
plt.show()
# -----------------------------
# TOP 10 BEST-SELLING PRODUCTS GRAPH
# -----------------------------

print("\nCreating Top 10 Best-Selling Products Graph...")

plt.figure(figsize=(12, 6))

top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Best-Selling Products")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig("outputs/top_10_best_selling_products.png", dpi=300, bbox_inches="tight")
plt.show()
# -----------------------------
# TOP 10 COUNTRIES BY SALES REVENUE GRAPH
# -----------------------------

print("\nCreating Top 10 Countries by Sales Revenue Graph...")

plt.figure(figsize=(12, 6))

country_sales.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Sales Revenue")
plt.xlabel("Sales Revenue (£)")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig("outputs/top_10_countries_by_revenue.png", dpi=300, bbox_inches="tight")
plt.show()
# -----------------------------
# TOP 10 CUSTOMERS BY REVENUE GRAPH
# -----------------------------

print("\nCreating Top 10 Customers by Revenue Graph...")

plt.figure(figsize=(12, 6))

# Convert CustomerID to string for better chart labels
top_customers_plot = top_customers.copy()
top_customers_plot.index = top_customers_plot.index.astype(str)

top_customers_plot.sort_values().plot(kind="barh")

plt.title("Top 10 Customers by Sales Revenue")
plt.xlabel("Sales Revenue (£)")
plt.ylabel("Customer ID")
plt.tight_layout()

plt.savefig("outputs/top_10_customers_by_revenue.png", dpi=300, bbox_inches="tight")
plt.show()
# -----------------------------
# TOP 10 PRODUCTS BY REVENUE GRAPH
# -----------------------------

print("\nCreating Top 10 Products by Revenue Graph...")

plt.figure(figsize=(12, 6))

top_revenue_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales Revenue")
plt.xlabel("Sales Revenue (£)")
plt.ylabel("Product")
plt.tight_layout()

# Save graph
plt.savefig(
    "outputs/top_10_products_by_revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
# -----------------------------
# SAVE ANALYSIS SUMMARY
# -----------------------------

print("\nSaving Analysis Summary...")

summary_data = {
    "Metric": [
        "Total Sales Revenue",
        "Total Orders",
        "Total Customers",
        "Average Order Value",
        "Average Quantity"
    ],
    "Value": [
        round(total_sales, 2),
        total_orders,
        total_customers,
        round(average_order_value, 2),
        round(average_quantity, 2)
    ]
}

summary_df = pd.DataFrame(summary_data)

summary_df.to_csv(
    "outputs/analysis_summary.csv",
    index=False
)

print("\nAnalysis Summary:")
print(summary_df)

print("\nAnalysis summary saved successfully!")
# -----------------------------
# EXPORT DETAILED ANALYSIS RESULTS
# -----------------------------

print("\nExporting detailed analysis results...")

# Top 10 best-selling products
top_products.reset_index().to_csv(
    "outputs/top_10_best_selling_products.csv",
    index=False
)

# Top 10 products by revenue
top_revenue_products.reset_index().to_csv(
    "outputs/top_10_products_by_revenue.csv",
    index=False
)

# Top 10 countries by revenue
country_sales.reset_index().to_csv(
    "outputs/top_10_countries_by_revenue.csv",
    index=False
)

# Top 10 customers by revenue
top_customers.reset_index().to_csv(
    "outputs/top_10_customers_by_revenue.csv",
    index=False
)

# Monthly sales trend
monthly_sales.reset_index().to_csv(
    "outputs/monthly_sales_trend.csv",
    index=False
)

print("Detailed analysis CSV files saved successfully!")
# -----------------------------
# RFM CUSTOMER ANALYSIS
# -----------------------------

print("\n--- RFM CUSTOMER ANALYSIS ---")

# Make sure InvoiceDate is datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Reference date = one day after the latest transaction
reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Create RFM table
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (reference_date - x.max()).days,
    "InvoiceNo": "nunique",
    "TotalPrice": "sum"
}).reset_index()

# Rename columns
rfm.columns = [
    "CustomerID",
    "Recency",
    "Frequency",
    "Monetary"
]

print("\nFirst 10 RFM Records:")
print(rfm.head(10))

print("\nRFM Statistical Summary:")
print(rfm[["Recency", "Frequency", "Monetary"]].describe())

# Save RFM analysis
rfm.to_csv(
    "outputs/rfm_customer_analysis.csv",
    index=False
)

print("\nRFM customer analysis saved successfully!")
# -----------------------------
# RFM SCORING AND SEGMENTATION
# -----------------------------

print("\n--- RFM CUSTOMER SEGMENTATION ---")

# Create RFM scores from 1 to 4
# Lower Recency is better, so labels are reversed
rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    4,
    labels=[4, 3, 2, 1]
).astype(int)

# Higher Frequency is better
rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)

# Higher Monetary value is better
rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)

# Calculate total RFM score
rfm["RFM_Score"] = (
    rfm["R_Score"] +
    rfm["F_Score"] +
    rfm["M_Score"]
)

# Assign customer segments
def customer_segment(score):
    if score >= 10:
        return "Best Customers"
    elif score >= 8:
        return "Loyal Customers"
    elif score >= 6:
        return "Potential Loyalists"
    elif score >= 4:
        return "At Risk"
    else:
        return "Lost Customers"


rfm["Customer_Segment"] = rfm["RFM_Score"].apply(customer_segment)

print("\nCustomer Segmentation Results:")
print(rfm.head(10))

print("\nCustomers in Each Segment:")
print(rfm["Customer_Segment"].value_counts())

# Save final RFM segmentation
rfm.to_csv(
    "outputs/rfm_customer_segments.csv",
    index=False
)

print("\nRFM customer segmentation saved successfully!")
# -----------------------------
# CUSTOMER SEGMENTATION GRAPH
# -----------------------------

print("\nCreating Customer Segmentation Graph...")

segment_counts = rfm["Customer_Segment"].value_counts()

plt.figure(figsize=(10, 6))

segment_counts.plot(kind="bar")

plt.title("Customer Segmentation Based on RFM Analysis")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

# Save graph
plt.savefig(
    "outputs/customer_segmentation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Customer segmentation graph saved successfully!")
# -----------------------------
# PREPARE DATA FOR SALES FORECASTING
# -----------------------------

print("\n--- PREPARING SALES FORECASTING DATA ---")

# Create a forecasting dataframe from monthly sales
forecast_data = monthly_sales.reset_index()

# Convert Month period to timestamp
forecast_data["Month"] = forecast_data["Month"].dt.to_timestamp()

# Rename the sales column
forecast_data.rename(
    columns={"TotalPrice": "MonthlySales"},
    inplace=True
)

# Sort by month
forecast_data = forecast_data.sort_values("Month")

print("\nMonthly Forecasting Data:")
print(forecast_data)

# Save forecasting dataset
forecast_data.to_csv(
    "outputs/monthly_sales_forecasting_data.csv",
    index=False
)

print("\nForecasting data saved successfully!")