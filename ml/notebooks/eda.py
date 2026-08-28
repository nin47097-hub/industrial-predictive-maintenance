import pandas as pd

# Load dataset
df = pd.read_csv("ml/dataset/all_machines.csv")

# -----------------------------------
# 1. Basic information
# -----------------------------------

print("Dataset shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

# -----------------------------------
# 2. Column information
# -----------------------------------

print("\nColumn information:")
print(df.info())

# -----------------------------------
# 3. Missing values
# -----------------------------------

print("\nMissing values:")
print(df.isnull().sum())

# -----------------------------------
# 4. Failure distribution
# -----------------------------------

print("\nFailure distribution:")
print(df["failure"].value_counts())

print("\nFailure percentage:")
print(df["failure"].value_counts(normalize=True) * 100)

# -----------------------------------
# 5. Failure types
# -----------------------------------

print("\nFailure types:")
print(df["failure_type"].value_counts())

# -----------------------------------
# 6. Machine distribution
# -----------------------------------

print("\nRecords per machine:")
print(df["machine_id"].value_counts())

# -----------------------------------
# 7. Machine failure distribution
# -----------------------------------

print("\nFailures by machine:")
print(
    df.groupby("machine_id")["failure"]
      .sum()
      .sort_values(ascending=False)
)

# -----------------------------------
# 8. Numerical statistics
# -----------------------------------

print("\nNumerical statistics:")
print(df.describe())