import pandas as pd
import os

os.makedirs("data_preparation", exist_ok=True)

df = pd.read_csv("raw_data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Convert TotalCharges to numeric (fixes error)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Convert Churn column to numeric (0 or 1)
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# Fill missing values (numeric-only)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Save cleaned data
df.to_csv("data_preparation/cleaned_data.csv", index=False)
print("✅ Data cleaning complete.")
