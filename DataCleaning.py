import pandas as pd

df = pd.DataFrame
# Add missing values to the DataFrame
df['Salary'] = [50000, None, 75000, 62000]

# Fill missing values with a default value
df['Salary'].fillna(0, inplace=True)

print("\nData After Cleaning:")
print(df)
