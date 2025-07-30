import pandas as pd

# Load the parsed CSV file
df = pd.read_csv("security_parsed.csv")

# Print structure
print("\n📁 Columns:")
print(df.columns)

print("\n🧾 First 5 Rows:")
print(df.head())

print("\n🔢 Total Events:")
print(len(df))
