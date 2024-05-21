import pandas as pd

# Step 1: Data Collection
# Hypothetical student dataset
data = {
    'Student ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [15, 16, 15, 17, 16],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'Grade Level': [10, 11, 10, 12, 11],
    'Math Score': [85, 90, 78, 92, None],  # Intentionally added missing value
    'Science Score': [88, 85, 82, 90, 86],
    'English Score': [80, 85, 75, 88, 82],
}

df = pd.DataFrame(data)

# Step 2: Data Preparation
# Handling missing values
df.fillna(df.mean(), inplace=True)

# Removing duplicates (no duplicates in this example)

# Step 3: Data Analysis
# Descriptive statistics
print("Descriptive Statistics:")
print(df.describe())

# Correlation analysis
print("\nCorrelation Matrix:")
print(df.corr())

# Group comparisons
print("\nMean Scores by Gender:")
print(df.groupby('Gender').mean())

# Step 4: Data Presentation (Optional)
# Visualizations, reports, etc.
