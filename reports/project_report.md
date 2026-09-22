# E-COMMERCE SALES ANALYSIS & FORECASTING

## Internship Project Report

**Internship Position:** Data Analysis with Python

**Organization:** Cognevance Technologies

**Project:** E-Commerce Sales Analysis, Customer Segmentation and Sales Forecasting Using Python

**Submitted By:**  
[BADDAM SAI]

**Technologies:**  
Python | Pandas | NumPy | Matplotlib | Scikit-learn | Git | GitHub

**GitHub Repository:**  
https://github.com/Saireddy03351/cognevance_eCommerceSalesAnalysis

---

## Project Highlights

- 392,692 cleaned transaction records
- £8,887,208.89 analyzed sales revenue
- 18,532 unique orders
- 4,338 unique customers
- Product, country and customer sales analysis
- RFM customer segmentation
- Monthly sales trend analysis
- Linear Regression baseline forecasting
- Three-month future sales forecast

---

# E-COMMERCE SALES ANALYSIS & FORECASTING

## Internship Project Report

### Project Title
**E-Commerce Sales Analysis, Customer Segmentation and Sales Forecasting Using Python**

### Technologies Used
Python, Pandas, NumPy, Matplotlib, Scikit-learn, OpenPyXL, Git and GitHub

---

# 1. Project Overview

E-commerce businesses generate large amounts of transactional data containing valuable information about products, customers, sales and purchasing behaviour.

The purpose of this project is to analyze an online retail transaction dataset using Python and transform raw transactional data into meaningful business insights.

The project follows an end-to-end data analysis workflow consisting of data cleaning, exploratory data analysis (EDA), sales analysis, data visualization, RFM customer segmentation and baseline sales forecasting.

The analysis identifies sales trends, best-selling products, high-revenue products, country-wise performance and high-value customers.

RFM (Recency, Frequency and Monetary) analysis is also implemented to segment customers according to their purchasing behaviour.

Finally, a Linear Regression model is used as a baseline approach to analyze monthly sales patterns and generate a short-term three-month sales forecast.

---

# 2. Project Objectives

The major objectives of this project are:

- To clean and preprocess the raw e-commerce transaction dataset.
- To remove duplicate, incomplete and invalid transaction records.
- To perform Exploratory Data Analysis on the cleaned dataset.
- To calculate important sales and customer metrics.
- To identify the top-selling products based on quantity sold.
- To identify products generating the highest sales revenue.
- To analyze sales performance across different countries.
- To analyze monthly sales trends.
- To identify high-value customers based on their purchases.
- To perform RFM customer analysis.
- To segment customers based on Recency, Frequency and Monetary values.
- To create meaningful sales and customer visualizations.
- To prepare monthly sales data for forecasting.
- To build and evaluate a baseline Linear Regression forecasting model.
- To generate a short-term future sales forecast.
- To export analysis results and visualizations for reporting and decision-making.

---

# 3. Scope of the Project

The project focuses on historical e-commerce transaction data and demonstrates how Python-based data analytics can be used to understand business performance.

The scope includes:

- Transaction-level data preprocessing
- Sales performance analysis
- Product performance analysis
- Geographic sales analysis
- Customer behaviour analysis
- Customer segmentation
- Sales trend visualization
- Baseline machine-learning forecasting

The forecasting component is intended as a baseline demonstration because the available dataset contains a relatively short monthly sales history. Therefore, forecast results should not be interpreted as precise long-term predictions.
---

# 4. Dataset Description

The project uses the **Online Retail** dataset containing transaction-level information from an e-commerce retail business.

Each row represents an individual product associated with a customer transaction.

## 4.1 Important Dataset Attributes

The dataset contains attributes such as:

- **InvoiceNo:** Unique invoice or transaction number.
- **StockCode:** Unique code assigned to a product.
- **Description:** Description or name of the product.
- **Quantity:** Number of units purchased.
- **InvoiceDate:** Date and time when the transaction occurred.
- **UnitPrice:** Price of one unit of the product.
- **CustomerID:** Unique identifier assigned to a customer.
- **Country:** Country associated with the transaction.

During preprocessing, an additional feature called **TotalPrice** was created.

**TotalPrice = Quantity × UnitPrice**

This feature represents the sales value of each transaction line.

After the cleaning process, the final dataset used for analysis contains:

**392,692 rows and 9 columns.**

---

# 5. Project Workflow

The project follows an end-to-end data analytics workflow:

**Raw Dataset**

↓  

**Data Cleaning and Preprocessing**

↓

**Cleaned Dataset**

↓

**Exploratory Data Analysis (EDA)**

↓

**Sales and Product Analysis**

↓

**Country and Customer Analysis**

↓

**Monthly Sales Trend Analysis**

↓

**RFM Customer Analysis**

↓

**Customer Segmentation**

↓

**Data Visualization**

↓

**Monthly Sales Data Preparation**

↓

**Linear Regression Forecasting**

↓

**Model Evaluation**

↓

**Three-Month Future Sales Forecast**

↓

**Export Results and Visualizations**

This workflow separates data preparation, analysis, customer analytics and forecasting into logical stages.

---

# 6. Tools and Technologies Used

## 6.1 Python

Python is the primary programming language used to implement data preprocessing, analysis, visualization and forecasting.

## 6.2 Pandas

Pandas is used for:

- Reading Excel and CSV datasets
- Cleaning transaction data
- Handling missing values
- Grouping and aggregating data
- Calculating sales metrics
- Preparing RFM data
- Exporting analysis results

## 6.3 NumPy

NumPy is used for numerical operations and for preparing numerical time features required by the forecasting model.

## 6.4 Matplotlib

Matplotlib is used to create visualizations such as:

- Monthly sales trends
- Best-selling products
- Products by revenue
- Country-wise sales
- Customer revenue
- Customer segmentation
- Sales forecasting

## 6.5 Scikit-learn

Scikit-learn is used to implement the Linear Regression forecasting model and calculate model evaluation metrics.

## 6.6 OpenPyXL

OpenPyXL provides Excel file support for reading and writing `.xlsx` datasets through Pandas.

## 6.7 Visual Studio Code

Visual Studio Code is used as the primary development environment for writing, executing and organizing the Python project.

## 6.8 Git and GitHub

Git is used for version control, while GitHub is used to host and share the completed project repository.

---

# 7. Project Directory Structure

The project is organized into separate directories for source code, datasets, generated results and documentation.

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
│   ├── rfm_customer_analysis.csv
│   ├── rfm_customer_segments.csv
│   ├── customer_segmentation.png
│   ├── sales_forecasting_predictions.csv
│   ├── future_sales_forecast.csv
│   ├── sales_forecast.png
│   └── other analysis results
│
├── reports/
│   └── project_report.md
│
├── src/
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   └── sales_forecasting.py
│
├── .gitignore
├── README.md
└── requirements.txt
---

# 8. Data Cleaning and Preprocessing

Data cleaning is an important stage of the project because raw transaction data may contain missing values, duplicate records, cancelled orders and invalid prices.

The raw Online Retail dataset was processed using Pandas before performing exploratory analysis.

## 8.1 Loading the Dataset

The original Excel dataset was loaded into a Pandas DataFrame.

The initial dimensions and first few records were inspected to understand the structure of the dataset.

## 8.2 Removing Duplicate Records

Duplicate transaction records were removed using the Pandas `drop_duplicates()` function.

Removing duplicates prevents the same transaction from being counted multiple times during sales analysis.

## 8.3 Handling Missing Customer IDs

Transactions without a valid `CustomerID` were removed.

Customer identifiers are particularly important for:

- Customer-level sales analysis
- Identifying high-value customers
- RFM analysis
- Customer segmentation

Records without customer identifiers therefore cannot be reliably included in customer-level analysis.

## 8.4 Converting Invoice Date

The `InvoiceDate` column was converted into Pandas datetime format.

This enables time-based operations such as:

- Monthly sales aggregation
- Transaction ordering
- Recency calculation
- Sales trend analysis
- Forecasting data preparation

## 8.5 Creating TotalPrice

A new feature named `TotalPrice` was created using:

**TotalPrice = Quantity × UnitPrice**

This represents the revenue generated by each transaction line.

The feature is later used for:

- Total revenue calculation
- Product revenue analysis
- Country-wise revenue analysis
- Customer spending analysis
- Monetary value in RFM analysis

## 8.6 Removing Cancelled Transactions

Cancelled invoices were identified using invoice numbers beginning with the letter `C`.

These transactions were excluded from the analysis because they represent cancellations rather than completed sales.

## 8.7 Removing Invalid Prices

Transactions where `UnitPrice` was less than or equal to zero were removed.

This ensures that the sales analysis is based on transactions with positive product prices.

## 8.8 Saving the Cleaned Dataset

After preprocessing, the cleaned dataset was exported as:

`data/Online_Retail_Cleaned.xlsx`

The cleaned dataset contains:

**392,692 rows and 9 columns.**

This cleaned dataset is used for all subsequent exploratory analysis, customer segmentation and sales forecasting.

---

# 9. Data Quality Outcome

The preprocessing stage produced a structured dataset suitable for analysis.

The main improvements were:

- Duplicate transactions removed
- Missing customer identifiers removed
- Cancelled invoices excluded
- Invalid product prices excluded
- Invoice dates standardized
- Transaction-level revenue calculated
- Cleaned data exported for reproducibility

These preprocessing operations improve the consistency of the dataset and reduce the risk of misleading sales and customer analysis.
---

# 10. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed on the cleaned dataset to understand the overall characteristics of the e-commerce transactions and identify important sales patterns.

The analysis included:

- Dataset dimensions and structure
- Column names and data types
- Statistical summary
- Missing-value analysis
- Overall sales performance
- Product-level analysis
- Country-wise analysis
- Customer-level analysis
- Monthly sales trend analysis

The results of the analysis were also exported as CSV files and visualizations for reporting purposes.

---

# 11. Overall Sales Analysis

Several Key Performance Indicators (KPIs) were calculated to summarize the overall performance of the retail dataset.

The metrics include:

## 11.1 Total Sales Revenue

Total sales revenue was calculated by summing the `TotalPrice` column across all valid transactions.

This metric represents the total monetary value generated by the transactions included in the cleaned dataset.

## 11.2 Total Orders

The total number of orders was calculated by counting unique `InvoiceNo` values.

This prevents multiple product lines belonging to the same invoice from being counted as separate orders.

## 11.3 Total Customers

The number of unique `CustomerID` values was calculated to determine the total number of identifiable customers represented in the cleaned dataset.

## 11.4 Average Order Value

Average Order Value (AOV) was calculated by first determining the total revenue for each invoice and then calculating the average across all orders.

It can be expressed as:

**Average Order Value = Total Revenue / Number of Orders**

AOV provides an indication of the average amount of revenue generated by an order.

## 11.5 Average Quantity

The average quantity of products purchased per transaction line was also calculated to provide additional information about purchasing behaviour.

The calculated KPI values are stored in:

`outputs/analysis_summary.csv`

---

# 12. Product Analysis

Two different approaches were used to evaluate product performance.

## 12.1 Top 10 Best-Selling Products

Products were grouped by `Description`, and their quantities were summed.

The products were then sorted in descending order to identify the ten products with the highest total quantity sold.

This analysis helps identify products with strong sales volume.

The results are stored in:

`outputs/top_10_best_selling_products.csv`

A corresponding visualization is stored as:

`outputs/top_10_best_selling_products.png`

## 12.2 Top 10 Products by Sales Revenue

Products were also analyzed based on the total revenue they generated.

Transactions were grouped by product description, and `TotalPrice` was summed for each product.

The ten products generating the highest revenue were selected.

This analysis is different from quantity-based ranking because a product may sell fewer units but generate higher revenue due to its unit price.

The results and visualization are stored as:

`outputs/top_10_products_by_revenue.csv`

`outputs/top_10_products_by_revenue.png`

---

# 13. Country-Wise Sales Analysis

Sales performance was analyzed across different countries.

Transactions were grouped by `Country`, and total sales revenue was calculated using the `TotalPrice` column.

The countries were then sorted according to total revenue to identify the ten countries generating the highest sales.

The results are stored in:

`outputs/top_10_countries_by_revenue.csv`

The corresponding visualization is stored as:

`outputs/top_10_countries_by_revenue.png`

This analysis provides a geographic view of sales performance and can support market-level business analysis.

---

# 14. Customer Sales Analysis

Customer-level sales analysis was performed to identify high-value customers.

Transactions were grouped using `CustomerID`, and the total `TotalPrice` associated with each customer was calculated.

The customers were sorted by total spending, and the top ten customers by sales revenue were identified.

The results are stored in:

`outputs/top_10_customers_by_revenue.csv`

The visualization is stored as:

`outputs/top_10_customers_by_revenue.png`

Identifying customers with high historical spending can support customer relationship management and retention analysis.

---

# 15. Monthly Sales Trend Analysis

Monthly sales trends were analyzed using the `InvoiceDate` field.

The invoice date was converted into monthly periods, and total revenue was aggregated for each month.

This produced a time series showing how sales revenue changed throughout the available period.

The monthly results are stored in:

`outputs/monthly_sales_trend.csv`

The corresponding line chart is stored as:

`outputs/monthly_sales_trend.png`

Monthly trend analysis provides a foundation for understanding changes in historical sales and preparing the data for the forecasting stage.

---

# 16. EDA Visualizations

The exploratory analysis generated several visualizations:

1. Monthly Sales Trend
2. Top 10 Best-Selling Products
3. Top 10 Products by Sales Revenue
4. Top 10 Countries by Sales Revenue
5. Top 10 Customers by Sales Revenue

These visualizations provide an easier way to interpret patterns that may not be immediately apparent from raw tables.

All generated charts are stored in the `outputs/` directory.
---

# 17. RFM Customer Analysis

RFM analysis was performed to understand customer purchasing behaviour and identify different groups of customers based on their transaction history.

RFM represents three important customer metrics:

- **Recency (R):** How recently the customer made a purchase.
- **Frequency (F):** How frequently the customer placed orders.
- **Monetary (M):** How much money the customer spent.

The RFM analysis was performed using the cleaned transaction dataset.

## 17.1 Recency

Recency measures the number of days between a customer's most recent transaction and the reference date.

The reference date was defined as one day after the latest transaction date available in the dataset.

A lower Recency value indicates that the customer purchased more recently.

## 17.2 Frequency

Frequency represents the number of unique invoices associated with each customer.

A higher Frequency value indicates that the customer placed more orders during the analyzed period.

## 17.3 Monetary Value

Monetary value represents the total amount spent by each customer.

It was calculated by summing `TotalPrice` for every customer.

A higher Monetary value indicates greater historical customer spending.

The calculated RFM values were exported to:

`outputs/rfm_customer_analysis.csv`

---

# 18. RFM Scoring

To make the RFM metrics easier to compare, each customer was assigned separate Recency, Frequency and Monetary scores.

The customers were divided into four groups for each RFM dimension.

## 18.1 Recency Score

For Recency, lower values are considered better because they represent more recent purchases.

Therefore:

- Score 4 represents customers with better Recency.
- Score 1 represents customers with weaker Recency.

## 18.2 Frequency Score

For Frequency, higher values are considered better.

Customers who placed more orders receive higher Frequency scores.

## 18.3 Monetary Score

For Monetary value, customers with higher historical spending receive higher scores.

## 18.4 Combined RFM Score

The three individual scores were added together:

**RFM Score = R Score + F Score + M Score**

Since each component ranges from 1 to 4, the combined RFM score ranges from:

**Minimum Score = 3**

to

**Maximum Score = 12**

---

# 19. Customer Segmentation

Customers were classified into segments according to their combined RFM score.

The segmentation rules used in this project are:

| RFM Score | Customer Segment |
|-----------|------------------|
| 10–12 | Best Customers |
| 8–9 | Loyal Customers |
| 6–7 | Potential Loyalists |
| 4–5 | At Risk |
| 3 | Lost Customers |

These segment names provide a simple interpretation of customer purchasing behaviour based on the scoring rules implemented in this project.

The complete segmentation results were exported to:

`outputs/rfm_customer_segments.csv`

---

# 20. Interpretation of Customer Segments

## Best Customers

These customers have high combined RFM scores. They generally demonstrate a strong combination of recent purchasing activity, order frequency and historical spending.

## Loyal Customers

These customers have relatively strong RFM scores and represent customers with valuable historical purchasing behaviour.

## Potential Loyalists

These customers have moderate RFM scores and may show characteristics that place them between lower-engagement customers and highly valuable customer groups.

## At Risk

These customers have lower combined RFM scores according to the project's segmentation rules.

Their historical behaviour may indicate lower recency, frequency, monetary value, or a combination of these factors.

## Lost Customers

These customers receive the lowest combined RFM score under the implemented scoring approach.

They represent customers with comparatively weak combined RFM characteristics within the analyzed dataset.

---

# 21. Customer Segmentation Visualization

The number of customers belonging to each RFM segment was calculated and displayed using a bar chart.

The visualization is stored as:

`outputs/customer_segmentation.png`

This chart provides a visual overview of the distribution of customers across the five RFM segments.

RFM segmentation can support further business analysis such as customer retention, targeted marketing and customer relationship management.

However, the segment labels used in this project are analytical categories based on the defined RFM scoring thresholds and should not be interpreted as guaranteed predictions of future customer behaviour.
---

# 22. Sales Forecasting

After completing exploratory analysis and customer segmentation, monthly sales data was prepared for forecasting.

The purpose of this stage is to demonstrate a baseline machine-learning approach for analyzing historical sales trends and generating short-term future estimates.

---

# 23. Forecasting Data Preparation

Monthly sales revenue calculated during EDA was converted into a forecasting dataset.

The dataset contains:

- **Month:** Monthly time period
- **MonthlySales:** Total sales revenue generated during that month

The forecasting dataset was exported to:

`outputs/monthly_sales_forecasting_data.csv`

A numerical time feature named `Time` was created to represent the chronological sequence of months.

For example:

| Month | Time |
|-------|------|
| First Month | 0 |
| Second Month | 1 |
| Third Month | 2 |
| ... | ... |

This numerical feature was used as the independent variable for Linear Regression.

---

# 24. Train-Test Split

The forecasting data was divided chronologically into training and testing portions.

Approximately:

- **80% of the earliest observations** were used for training.
- **20% of the latest observations** were used for testing.

The chronological order was preserved because randomly shuffling time-series observations could allow future information to influence predictions for earlier periods.

---

# 25. Linear Regression Model

A Linear Regression model from Scikit-learn was used as the baseline forecasting algorithm.

The model attempts to estimate the relationship between time and monthly sales.

The general form of Linear Regression is:

**y = β₀ + β₁x**

Where:

- **y** = predicted monthly sales
- **x** = time index
- **β₀** = intercept
- **β₁** = regression coefficient

After training, the model was applied to the test period to generate predicted monthly sales.

Actual and predicted values were exported to:

`outputs/sales_forecasting_predictions.csv`

---

# 26. Model Evaluation

The forecasting model was evaluated using three metrics:

## 26.1 Mean Absolute Error (MAE)

Mean Absolute Error measures the average absolute difference between actual and predicted sales values.

A smaller MAE indicates that predictions are, on average, closer to the actual observations.

## 26.2 Root Mean Squared Error (RMSE)

Root Mean Squared Error measures prediction error while giving greater weight to larger errors.

A smaller RMSE generally indicates better predictive accuracy on the evaluated observations.

## 26.3 R² Score

The R² score measures how much of the variation in the test observations is explained by the fitted regression model.

An R² value closer to 1 indicates a stronger fit on the evaluated data.

A low or negative R² can occur when the model does not represent the observed sales pattern well.

Because this project contains a relatively small number of monthly observations, these evaluation metrics should be interpreted cautiously.

---

# 27. Future Sales Forecast

After training the baseline model, it was used to generate sales estimates for the next three monthly periods following the historical dataset.

The future forecast was exported to:

`outputs/future_sales_forecast.csv`

A visualization containing historical sales and future forecast values was also created and stored as:

`outputs/sales_forecast.png`

---

# 28. Forecasting Limitations

The forecasting component has several important limitations.

The available dataset contains only a relatively short monthly history. This provides a small number of observations for training and evaluating a forecasting model.

Linear Regression also assumes a simple linear relationship between time and sales. Real-world retail sales may instead contain:

- Seasonal patterns
- Holiday effects
- Promotions and discounts
- Product availability changes
- Economic conditions
- Customer behaviour changes
- Non-linear trends

Therefore, the three-month forecast in this project should be considered a **baseline demonstration of a forecasting workflow**, rather than a precise prediction of future business performance.

With additional historical data, future versions could evaluate methods such as time-series regression, exponential smoothing, ARIMA-family models, or other forecasting approaches using appropriate validation procedures.
---

# 29. Project Results

The completed analysis produced the following key results from the cleaned Online Retail dataset.

## 29.1 Overall Sales Performance

| Performance Metric | Result |
|--------------------|-------:|
| Total Sales Revenue | £8,887,208.89 |
| Total Orders | 18,532 |
| Total Customers | 4,338 |
| Average Order Value | £479.56 |
| Average Quantity per Transaction Line | 13.12 |

The cleaned transaction data generated approximately **£8.89 million in total sales revenue** across **18,532 unique orders**.

A total of **4,338 unique customers** were represented in the cleaned dataset.

The calculated **Average Order Value was £479.56**, while the average quantity per transaction line was **13.12 units**.

---

# 30. Sales Forecasting Results

The Linear Regression baseline model was evaluated on the chronologically held-out test observations.

The following evaluation results were obtained:

| Evaluation Metric | Result |
|-------------------|-------:|
| Mean Absolute Error (MAE) | £305,686.38 |
| Root Mean Squared Error (RMSE) | £308,494.23 |
| R² Score | -0.2383 |

## 30.1 Model Interpretation

The MAE indicates that the model's monthly predictions differed from the actual test values by approximately **£305,686 on average**.

The RMSE was approximately **£308,494**, indicating substantial prediction errors within the test period.

The R² score was **-0.2383**.

A negative R² indicates that, on the held-out test observations, the Linear Regression model performed worse than a simple baseline that predicts the mean of the test target values.

Therefore, the Linear Regression model should **not be considered a high-accuracy forecasting model for this dataset**.

This result is understandable because the dataset provides only a small number of monthly observations and retail sales can contain seasonality and other non-linear patterns that a simple linear trend cannot adequately represent.

---

# 31. Three-Month Future Forecast

The trained baseline model generated the following future estimates:

| Forecast Month | Predicted Sales |
|----------------|----------------:|
| January 2012 | £881,848.62 |
| February 2012 | £912,911.16 |
| March 2012 | £943,973.70 |

The model produces an increasing linear forecast across the three future months.

However, because the model achieved a negative R² score on the test data, these values should be interpreted as **baseline model outputs rather than reliable business forecasts**.

The future predictions demonstrate the technical forecasting workflow but should not be used for real-world planning without additional historical data and stronger model validation.

---

# 32. Key Findings

The analysis produced several important findings:

- The cleaned dataset contains **392,692 valid transaction records**.
- Total analyzed sales revenue was approximately **£8.89 million**.
- The dataset contains **18,532 unique orders**.
- **4,338 unique customers** were identified.
- Average Order Value was approximately **£479.56**.
- Product analysis identified the products with the highest sales volume and revenue.
- Country-level analysis identified the markets contributing the highest historical revenue.
- Customer-level analysis identified customers with the highest historical spending.
- Monthly aggregation revealed changes in sales performance over time.
- RFM analysis provided a structured method for grouping customers according to recency, frequency and monetary behaviour.
- The Linear Regression model provided a useful baseline forecasting implementation, but its **negative R² score shows that a simple linear trend does not adequately explain the held-out monthly sales observations**.

---

# 33. Business Applications

The analytical outputs from this project can support several types of business analysis.

## Product Performance

Best-selling and high-revenue product analysis can help businesses understand which products contribute strongly to transaction volume and historical revenue.

## Geographic Performance

Country-wise revenue analysis can help identify markets with stronger historical sales contribution.

## Customer Relationship Management

High-value customer analysis and RFM segmentation can help businesses organize customers into groups for further retention and engagement analysis.

## Sales Monitoring

Monthly sales trend analysis provides a simple method for monitoring historical changes in revenue.

## Forecasting

Forecasting can support planning when sufficient historical data and appropriately validated models are available.

In this project, the Linear Regression forecast serves primarily as a baseline demonstration and highlights the importance of evaluating model performance before relying on predictions.

---

# 34. Limitations

The project has several limitations:

- The dataset contains a relatively short historical period.
- Monthly aggregation results in only a small number of observations for forecasting.
- The Linear Regression model captures only a simple linear relationship between time and sales.
- Seasonal and holiday effects are not explicitly modeled.
- External factors such as promotions, economic conditions and inventory availability are not included.
- RFM segment labels are based on project-defined score thresholds rather than independently validated customer behaviour classes.
- Future sales estimates should therefore be interpreted cautiously.

---

# 35. Future Improvements

Future development of the project could include:

- Using several years of transaction data.
- Performing more robust time-series validation.
- Evaluating seasonal forecasting models.
- Comparing multiple forecasting algorithms.
- Performing product-level sales forecasting.
- Applying clustering algorithms for data-driven customer segmentation.
- Developing customer churn models.
- Creating interactive Power BI or Tableau dashboards.
- Automating analysis and report generation.

---

# 36. Conclusion

This project demonstrates an end-to-end e-commerce data analytics workflow using Python.

Raw transaction data was cleaned and transformed into a structured dataset containing **392,692 valid records**. Exploratory analysis was then used to examine sales performance, products, countries, customers and monthly trends.

The analysis identified **£8,887,208.89 in sales revenue**, **18,532 unique orders**, and **4,338 customers**. RFM analysis was used to provide a structured view of customer purchasing behaviour and to create customer segments.

A Linear Regression model was implemented as a baseline monthly sales forecasting approach. Its test performance produced an MAE of **£305,686.38**, RMSE of **£308,494.23**, and R² of **-0.2383**. These results demonstrate that the simple linear model has limited predictive capability for the available monthly data.

Overall, the project demonstrates practical skills in **data cleaning, exploratory data analysis, visualization, customer analytics, machine learning, model evaluation, Git and GitHub** while also showing the importance of interpreting analytical and predictive results according to their limitations.
---

# 37. GitHub Repository

The complete source code, datasets, generated outputs and project documentation are maintained in the GitHub repository below:

**Repository Name:** cognevance_eCommerceSalesAnalysis

**GitHub Repository:**  
https://github.com/Saireddy03351/cognevance_eCommerceSalesAnalysis

The repository contains:

- Raw and cleaned datasets
- Data cleaning source code
- Exploratory Data Analysis source code
- RFM customer analysis and segmentation
- Sales forecasting source code
- Generated CSV analysis results
- Data visualizations
- Project README
- Python dependencies
- Project documentation

Git and GitHub were used for version control and project sharing.

---

# 38. Project Deliverables

The final project includes the following deliverables:

1. Python source code for data cleaning.
2. Python source code for exploratory data analysis.
3. Python source code for sales forecasting.
4. Original Online Retail dataset.
5. Cleaned Online Retail dataset.
6. Sales analysis results in CSV format.
7. RFM customer analysis and segmentation results.
8. Sales forecasting results.
9. Product, customer, country and sales trend visualizations.
10. GitHub repository containing the complete project.
11. Final project documentation.

---

# 39. Final Summary

The E-Commerce Sales Analysis & Forecasting project demonstrates how Python can be used to transform raw transactional data into meaningful analytical outputs.

The project covers the complete workflow from data preprocessing through exploratory analysis, customer segmentation and baseline sales forecasting.

The final implementation demonstrates practical knowledge of Python, Pandas, NumPy, Matplotlib, Scikit-learn, data preprocessing, EDA, RFM analysis, machine learning, model evaluation, Git and GitHub.

The project also demonstrates the importance of evaluating forecasting models objectively. Although the Linear Regression model successfully generated future estimates, its negative R² score indicates that more historical data and more suitable time-series methods would be required for dependable forecasting.