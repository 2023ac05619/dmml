import mlflow
import pickle

# Ensure directory exists
os.makedirs("model_training", exist_ok=True)

with open("model_training/churn_model.pkl", "rb") as file:
    model = pickle.load(file)

mlflow.start_run()
mlflow.log_metric("accuracy", accuracy)
mlflow.sklearn.log_model(model, "model")
mlflow.end_run()

print("✅ Model tracking complete.")
