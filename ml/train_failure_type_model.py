import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
df = pd.read_csv("ml/dataset/all_machines.csv")
failure_data = df[df["failure"] == 1]




X = failure_data.drop(
    columns=["failure", "failure_type", "timestamp", "machine_id"]
)

y = failure_data["failure_type"]

categorical_columns = [
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
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Classification Report:")
print(classification_report(y_test, y_pred))


sample = X_test.iloc[[0]]



prediction = model.predict(sample)


print("\nPredicted Failure Type:")
print(prediction[0])



probability = model.predict_proba(sample)


print("\nFailure Type Probabilities:")

for failure_type, prob in zip(model.classes_, probability[0]):
    print(f"{failure_type}: {prob * 100:.2f}%")


joblib.dump(
    model,
    "ml/models/failure_type_model.pkl"
)

joblib.dump(
    list(X.columns),
    "ml/models/failure_type_features.pkl"
)