# E-Commerce Sales Analysis & Forecasting

## Project Overview

This project performs an end-to-end analysis of an e-commerce retail dataset using Python. It covers data cleaning, exploratory data analysis (EDA), sales performance analysis, customer segmentation using RFM analysis, data visualization, and baseline sales forecasting using Linear Regression.

The objective is to transform raw transaction data into meaningful business insights and demonstrate a complete data-analysis workflow.

---

## Objectives

- Clean and preprocess the e-commerce transaction dataset
- Perform Exploratory Data Analysis (EDA)
- Calculate important sales metrics
- Identify best-selling products
- Identify products generating the highest revenue
- Analyze country-wise sales performance
- Analyze monthly sales trends
- Identify high-value customers
- Perform RFM customer segmentation
- Build a baseline sales forecasting model
- Forecast future monthly sales
- Create and export visualizations and analysis results

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- OpenPyXL
- Visual Studio Code
- Git
- GitHub

---

## Project Structure

```text
cognevance_eCommerceSalesAnalysis/
│
├── data/
│   ├── Online Retail.xlsx
│   └── Online_Retail_Cleaned.xlsx
│
├── outputs/
│   ├── analysis_summary.csv
│   ├── monthly_sales_trend.csv
│   ├── monthly_sales_trend.png
│   ├── top_10_best_selling_products.csv
│   ├── top_10_best_selling_products.png
│   ├── top_10_products_by_revenue.csv
│   ├── top_10_products_by_revenue.png
│   ├── top_10_countries_by_revenue.csv
│   ├── top_10_countries_by_revenue.png
│   ├── top_10_customers_by_revenue.csv
│   ├── top_10_customers_by_revenue.png
│   ├── rfm_customer_analysis.csv
│   ├── rfm_customer_segments.csv
│   ├── customer_segmentation.png
│   ├── monthly_sales_forecasting_data.csv
│   ├── sales_forecasting_predictions.csv
│   ├── future_sales_forecast.csv
│   └── sales_forecast.png
│
├── reports/
│
├── src/
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   └── sales_forecasting.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Data Cleaning

The raw retail dataset is cleaned before analysis. The preprocessing process includes:

- Removing duplicate records
- Handling missing customer IDs
- Converting invoice dates to datetime format
- Removing cancelled transactions
- Removing invalid product prices
- Creating a `TotalPrice` feature

After cleaning, the dataset contains approximately **392,692 records**.

---

## Exploratory Data Analysis

The project analyzes important e-commerce metrics including:

- Total Sales Revenue
- Total Orders
- Total Customers
- Average Order Value
- Average Quantity
- Top 10 Best-Selling Products
- Top 10 Products by Revenue
- Top 10 Countries by Revenue
- Top 10 Customers by Revenue
- Monthly Sales Trends

---

## RFM Customer Segmentation

RFM analysis is used to understand customer purchasing behavior.

### Recency
Measures how recently a customer made a purchase.

### Frequency
Measures how frequently a customer places orders.

### Monetary
Measures how much money a customer spends.

Customers are classified into segments such as:

- Best Customers
- Loyal Customers
- Potential Loyalists
- At Risk
- Lost Customers

This analysis can support customer retention and targeted marketing strategies.

---

## Sales Forecasting

A **Linear Regression** model is implemented as a baseline approach for monthly sales forecasting.

The dataset is split chronologically into training and testing data to avoid using future observations to predict earlier observations.

Model performance is evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The model is also used to generate a **three-month future sales forecast**.

> **Note:** The available dataset contains a relatively short monthly sales history. Therefore, the Linear Regression forecast is treated as a baseline demonstration rather than a highly reliable long-term forecasting model.

---

## Visualizations

The project generates visualizations for:

1. Monthly Sales Trend
2. Top 10 Best-Selling Products
3. Top 10 Products by Sales Revenue
4. Top 10 Countries by Sales Revenue
5. Top 10 Customers by Revenue
6. RFM Customer Segmentation
7. Monthly Sales Forecast

The generated charts are saved automatically in the `outputs/` directory.

---

## Installation

Clone the repository and install the required Python libraries:

```bash
pip install -r requirements.txt
```

---

## How to Run

### 1. Run Data Cleaning

```bash
python src/data_cleaning.py
```

### 2. Run Exploratory Data Analysis

```bash
python src/eda_analysis.py
```

### 3. Run Sales Forecasting

```bash
python src/sales_forecasting.py
```

---

## Business Applications

The analysis can help an e-commerce business:

- Understand overall sales performance
- Monitor monthly sales trends
- Identify high-performing products
- Identify high-value customers
- Compare sales performance across countries
- Segment customers based on purchasing behavior
- Support customer-retention strategies
- Support marketing and inventory decisions
- Explore future sales trends

---

## Future Improvements

Future versions of the project could include:

- More historical sales data
- Advanced time-series forecasting models
- Product-level forecasting
- Customer churn prediction
- Machine-learning-based customer clustering
- Interactive Power BI or Tableau dashboards
- Automated reporting

---

## Conclusion

This project demonstrates a complete Python-based e-commerce analytics workflow, from raw-data cleaning through exploratory analysis, visualization, RFM customer segmentation, and baseline sales forecasting.

The project shows how transaction data can be transformed into useful business insights using data-analysis and machine-learning techniques.