import pandas as pd

df = pd.read_csv(r"C:\Users\LAW LIBRARY\Downloads\KaggleV2-May-2016.csv\KaggleV2-May-2016.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

# Handle missing values (better way)
df['age'] = df['age'].fillna(df['age'].median())
df['gender'] = df['gender'].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates()

# Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert dates safely
df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')
df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')

# Standardize data
df['gender'] = df['gender'].str.upper()
df['no_show'] = df['no_show'].replace({'No': 0, 'Yes': 1})

# Remove invalid age
df = df[df['age'] >= 0]

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("✅ Done - Cleaned Dataset Ready")
