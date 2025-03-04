import pandas as pd

# Ensure raw_data directory exists
os.makedirs("raw_data", exist_ok=True)

# Sample Data
data = {
    "customer_id": [101, 102, 103, 104, 105],
    "age": [32, 45, 29, 51, 38],
    "monthly_charges": [29.99, 59.99, 35.99, 70.99, 45.99],
    "tenure": [12, 24, 8, 36, 18],
    "churn": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("raw_data/customer_data.csv", index=False)

print("✅ customer_data.csv created successfully.")
