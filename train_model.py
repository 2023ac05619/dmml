import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
import mlflow
import pickle
import os

os.makedirs("model_tracking", exist_ok=True)

df = pd.read_csv("feature_engineering/processed_data.csv")

# Print available columns
print("✅ Available columns:", df.columns.tolist())

# Drop non-feature columns
if "customer_id" in df.columns and "churn" in df.columns:
    X = df.drop(columns=["customer_id", "churn"])
    y = df["churn"]
else:
    print("❌ ERROR: Required columns are missing from dataset!")
    exit()

# Convert categorical features to numeric
X = pd.get_dummies(X, drop_first=True)

# Handle missing values
imputer = SimpleImputer(strategy="median")
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ensure y_train and y_test are numeric
y_train = y_train.astype(int)
y_test = y_test.astype(int)  # Ensure y_test is integer

# Apply SMOTE
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_resampled, y_train_resampled)

# Evaluate Model
y_pred = model.predict(X_test)
y_pred = y_pred.astype(int)  # Ensure predictions are integer

# Compute accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.2f}")

# MLflow Tracking
if mlflow.active_run():
    mlflow.end_run()
mlflow.start_run()
mlflow.log_metric("model_accuracy", accuracy)

# Save trained model
with open("model_tracking/churn_model.pkl", "wb") as file:
    pickle.dump(model, file)

# Log model in MLflow
mlflow.sklearn.log_model(model, "churn_model")

mlflow.end_run()
print("✅ Model tracking completed with MLflow!")
