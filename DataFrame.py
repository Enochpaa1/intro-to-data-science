import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 22, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

#Indexing and Selection

# Select specific rows and columns using .loc
print("\nSelect by Label (loc):")
print(df.loc[1])  # Select row with index 1

# Select using .iloc (position based indexing)
print("\nSelect by Position (iloc):")
print(df.iloc[0, 1])  # First row, second column


#Data Cleaning

# Add missing values to the DataFrame
df['Salary'] = [50000, None, 75000, 62000]

# Fill missing values with a default value
df['Salary'].fillna(0, inplace=True)

print("\nData After Cleaning:")
print(df)


#Grouping and aggregation

# Add missing values to the DataFrame
df['Salary'] = [50000, None, 75000, 62000]

# Fill missing values with a default value
df['Salary'].fillna(0, inplace=True)

print("\nData After Cleaning:")
print(df)


#Merging and Joining

# Add missing values to the DataFrame
df['Salary'] = [50000, None, 75000, 62000]

# Fill missing values with a default value
df['Salary'].fillna(0, inplace=True)

print("\nData After Cleaning:")
print(df)

