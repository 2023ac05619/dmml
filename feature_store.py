import pandas as pd
import os

# Create necessary directories
os.makedirs("feature_engineering", exist_ok=True)

# Load dataset
file_path = "raw_data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)

# ✅ Print dataset overview
print(f"✅ Loaded dataset with shape: {df.shape}")
print(f"✅ Available columns: {df.columns.tolist()}")

# ✅ Ensure `customerID` is properly renamed and included
if "customerID" in df.columns:
    df.rename(columns={"customerID": "customer_id"}, inplace=True)

# ✅ Ensure `Churn` is included and converted to binary values
if "Churn" in df.columns:
    df["churn"] = df["Churn"].map({"No": 0, "Yes": 1})
    df.drop(columns=["Churn"], inplace=True)

# ✅ Ensure `customer_id` remains as a string
df["customer_id"] = df["customer_id"].astype(str)

# ✅ Handle Missing Values
print("🔍 Checking for missing values before processing...")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# Fill missing numerical values with the median
num_cols = df.select_dtypes(include=["number"]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill missing categorical values with "Unknown"
cat_cols = df.select_dtypes(include=["object"]).columns
df[cat_cols] = df[cat_cols].fillna("Unknown")

# ✅ Ensure `TotalCharges` is numeric
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# ✅ Convert categorical columns to dummies while keeping `customer_id` and `churn`
categorical_cols = [col for col in df.columns if df[col].dtype == "object" and col not in ["customer_id"]]
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# ✅ Save processed data
processed_file_path = "feature_engineering/processed_data.csv"
df.to_csv(processed_file_path, index=False)
print(f"✅ Processed data saved at {processed_file_path}")

# ✅ Print Final Summary
print(f"✅ Final dataset shape: {df.shape}")
print(f"✅ Final column types:\n{df.dtypes}")
