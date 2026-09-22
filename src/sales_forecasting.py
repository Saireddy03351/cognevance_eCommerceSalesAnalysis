import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# -----------------------------
# LOAD FORECASTING DATA
# -----------------------------

df = pd.read_csv("outputs/monthly_sales_forecasting_data.csv")

df["Month"] = pd.to_datetime(df["Month"])
df = df.sort_values("Month").reset_index(drop=True)

print("Forecasting data loaded successfully!")
print(df)


# -----------------------------
# CREATE TIME FEATURE
# -----------------------------

df["Time"] = np.arange(len(df))

X = df[["Time"]]
y = df["MonthlySales"]


# -----------------------------
# TRAIN / TEST SPLIT
# -----------------------------

# Keep chronological order for time-series data
split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]


# -----------------------------
# TRAIN LINEAR REGRESSION MODEL
# -----------------------------

model = LinearRegression()

model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully!")


# -----------------------------
# MAKE PREDICTIONS
# -----------------------------

y_pred = model.predict(X_test)

results = pd.DataFrame({
    "Month": df.loc[X_test.index, "Month"],
    "ActualSales": y_test.values,
    "PredictedSales": y_pred
})

print("\nActual vs Predicted Sales:")
print(results)


# -----------------------------
# MODEL EVALUATION
# -----------------------------

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n--- MODEL PERFORMANCE ---")
print(f"MAE: {mae:,.2f}")
print(f"RMSE: {rmse:,.2f}")
print(f"R2 Score: {r2:.4f}")


# -----------------------------
# SAVE RESULTS
# -----------------------------

results.to_csv(
    "outputs/sales_forecasting_predictions.csv",
    index=False
)

print("\nForecasting predictions saved successfully!")
# -----------------------------
# FORECAST NEXT 3 MONTHS
# -----------------------------

print("\n--- FUTURE SALES FORECAST ---")

future_periods = 3

# Create future time values
future_time = np.arange(
    len(df),
    len(df) + future_periods
).reshape(-1, 1)

# Predict future sales
future_predictions = model.predict(future_time)

# Create future month dates
last_month = df["Month"].max()

future_months = pd.date_range(
    start=last_month + pd.DateOffset(months=1),
    periods=future_periods,
    freq="MS"
)

# Create future forecast dataframe
future_forecast = pd.DataFrame({
    "Month": future_months,
    "PredictedSales": future_predictions
})

print(future_forecast)

# Save future predictions
future_forecast.to_csv(
    "outputs/future_sales_forecast.csv",
    index=False
)

print("\nFuture sales forecast saved successfully!")


# -----------------------------
# FORECAST VISUALIZATION
# -----------------------------

plt.figure(figsize=(12, 6))

# Historical sales
plt.plot(
    df["Month"],
    df["MonthlySales"],
    marker="o",
    label="Historical Sales"
)

# Future predicted sales
plt.plot(
    future_forecast["Month"],
    future_forecast["PredictedSales"],
    marker="o",
    linestyle="--",
    label="Forecasted Sales"
)

plt.title("Monthly Sales Forecast")
plt.xlabel("Month")
plt.ylabel("Sales Revenue (£)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save graph
plt.savefig(
    "outputs/sales_forecast.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nSales forecast graph saved successfully!")