import pandas as pd
import glob
import os

# Folder containing the CSV files
folder = "ml/dataset"

# Find all CSV files
files = glob.glob(os.path.join(folder, "*.csv"))

# Don't include all_machines.csv if it already exists
files = [
    file for file in files
    if not file.endswith("all_machines.csv")
]

print("CSV files found:", len(files))

# Read all files
dataframes = []

for file in files:
    print("Loading:", os.path.basename(file))

    df = pd.read_csv(file)

    dataframes.append(df)

# Combine everything
all_data = pd.concat(
    dataframes,
    ignore_index=True
)

# Save combined dataset
output_file = os.path.join(
    folder,
    "all_machines.csv"
)

all_data.to_csv(
    output_file,
    index=False
)

print("\n==============================")
print("COMBINATION COMPLETE")
print("==============================")

print("Number of files:", len(files))
print("Total rows:", len(all_data))
print("Total columns:", len(all_data.columns))

print("\nColumns:")
print(all_data.columns.tolist())

print("\nSaved to:")
print(output_file)