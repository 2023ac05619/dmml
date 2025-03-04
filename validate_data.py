import pandas as pd
import os

os.makedirs("data_validation", exist_ok=True)

def validate_data(df):
    """ Validate missing values and schema consistency """
    validation_report = {
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": df.duplicated().sum(),
        "data_types": df.dtypes.to_dict(),
    }

    report_df = pd.DataFrame(validation_report.items(), columns=["Check", "Value"])
    report_df.to_csv("data_validation/data_quality_report.csv", index=False)
    print("✅ Data validation complete.")

df = pd.read_csv("raw_data/customer_data.csv")
validate_data(df)
