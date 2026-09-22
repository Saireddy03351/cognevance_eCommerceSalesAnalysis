import pandas as pd

# Load the e-commerce dataset
df = pd.read_excel("data/Online Retail.xlsx")

print("Dataset loaded successfully!")
print("Rows and columns:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
df = df.drop_duplicates()
df = df.dropna(subset=["CustomerID"])
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df[df["UnitPrice"] > 0]
print("Rows after cleaning:", df.shape)
df.to_excel("data/Online_Retail_Cleaned.xlsx", index=False)