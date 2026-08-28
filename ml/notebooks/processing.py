import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("ml/dataset/all_machines.csv")

df = df.drop(columns=["timestamp", "failure_type"])

y = df["failure"]

X = df.drop(columns=["failure"])

categorical_columns = [
    "machine_id",
    "production_line",
    "machine_type"
]

x = pd.get_dummies(
    X,
    columns=categorical_columns
)

numerical_columns = x.select_dtypes(
    include=["int64", "float64"]
).columns

x[numerical_columns] = x[numerical_columns].fillna(
    x[numerical_columns].median()
)

print("Remaining missing values:", x.isnull().sum().sum())



X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)