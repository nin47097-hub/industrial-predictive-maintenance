import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


df = pd.read_csv("ml/dataset/all_machines.csv")

df = df.drop(columns=["timestamp", "failure_type"])


X = df.drop(columns=["failure"])
y = df["failure"]


categorical_columns = [
    "machine_id",
    "production_line",
    "machine_type"
]


X = pd.get_dummies(
    X,
    columns=categorical_columns
)


numerical_columns = X.select_dtypes(
    include=["int64", "float64"]
).columns

X[numerical_columns] = X[numerical_columns].fillna(
    X[numerical_columns].median()
)



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)



y_pred = model.predict(X_test)

y_probability = model.predict_proba(X_test)

failure_probability = y_probability[:, 1] * 100

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print(
    "Failure probabilities:",
    failure_probability[:10]
)


joblib.dump(
    model,
    "ml/models/failure_model.pkl"
)



joblib.dump(
    list(X.columns),
    "ml/models/failure_features.pkl"
)


print("Failure model saved successfully.")