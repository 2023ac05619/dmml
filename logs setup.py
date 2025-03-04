import os
import logging

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Logging setup
logging.basicConfig(
    filename="logs/ingestion.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("✅ Logging setup complete. Logs will be stored in logs/ingestion.log")

# Example log message
logging.info("Data ingestion script started.")
