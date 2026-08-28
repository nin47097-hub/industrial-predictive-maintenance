import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)



df = pd.read_csv("ml/dataset/all_machines.csv")


features = [
    "temperature",
    "vibration",
    "load_percentage",
    "operating_hours",
    "maintenance_count"
]



df[features] = df[features].fillna(
    df[features].median()
)



temperature_risk = np.clip(
    (df["temperature"] - 50) / 60 * 25,
    0,
    25
)



vibration_risk = np.clip(
    (df["vibration"] - 1) / 9 * 25,
    0,
    25
)



load_risk = np.clip(
    (df["load_percentage"] - 50) / 50 * 15,
    0,
    15
)


hours_risk = np.clip(
    (df["operating_hours"] - 4500) / 10000 * 15,
    0,
    15
)



maintenance_risk = np.clip(
    df["maintenance_count"] / 10 * 10,
    0,
    10
)



total_risk = (
    temperature_risk
    + vibration_risk
    + load_risk
    + hours_risk
    + maintenance_risk
)



df["health_score"] = 100 - total_risk

df["health_score"] = df["health_score"].clip(0, 100)


X = df[features]

y = df["health_score"]



print("Missing values in X:")
print(X.isnull().sum())

print("\nMissing values in y:")
print(y.isnull().sum())



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



model = LinearRegression()


model.fit(X_train, y_train)
import joblib

joblib.dump(
    model,
    "ml/models/health_model.pkl"
)

joblib.dump(
    features,
    "ml/models/health_features.pkl"
)

print("Health model saved successfully.")



y_pred = model.predict(X_test)




mae = mean_absolute_error(
    y_test,
    y_pred
)

mse = mean_squared_error(
    y_test,
    y_pred
)

r2 = r2_score(
    y_test,
    y_pred
)


print("\nModel Results")

print("MAE:", mae)

print("MSE:", mse)

print("R2 Score:", r2)




sample = X_test.iloc[[0]]

predicted_health = model.predict(sample)[0]

print("\nPredicted Health:", predicted_health)