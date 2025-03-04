import pandas as pd
import os
import logging

# Logging setup
logging.basicConfig(filename="logs/ingestion.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

os.makedirs("raw_data", exist_ok=True)

def load_data(file_path):
    """ Load customer data from CSV """
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Successfully loaded data from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None

# Run Data Ingestion
df = load_data("raw_data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
df.head()
