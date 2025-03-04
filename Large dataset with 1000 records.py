import pandas as pd
import numpy as np
import os

# Ensure directory exists
os.makedirs("raw_data", exist_ok=True)

# Generate 1000 customer records
num_samples = 1000
data = {
    "customer_id": np.arange(2000, 2000 + num_samples),
    "age": np.random.randint(18, 75, size=num_samples),
    "monthly_charges": np.random.uniform(10, 150, size=num_samples).round(2),
    "tenure": np.random.randint(1, 72, size=num_samples),
    "churn": np.random.choice([0, 1], size=num_samples, p=[0.65, 0.35])  # 65% No churn, 35% Churn
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("raw_data/customer_data_large.csv", index=False)

print("✅ Large dataset with 1000 records created successfully.")
