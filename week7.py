# Step 1: Install the ucimlrepo library
#!pip install ucimlrepo

# Step 2: Import required libraries
import pandas as pd
from ucimlrepo import fetch_ucirepo, list_datasets
import matplotlib.pyplot as plt
import seaborn as sns

# Step 3: List available datasets (optional)
print("Available datasets:")
print(list_datasets())

# Step 4: Load the Iris dataset
try:
    iris = fetch_ucirepo(name='iris')  # Fetch the Iris dataset by name
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
except Exception as e:
    print(f"Error loading dataset: {e}")
    df = None  # Set df to None if loading fails

# Step 5: Check if df is defined before proceeding
if df is not None:
    # Display the first few rows
    print("First few rows of the dataset:")
    print(df.head())

    # Step 6: Display data types and check for missing values
    print("\nData Types and Missing Values:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Step 7: Basic Data Analysis
    # Compute basic statistics
    print("\nBasic Statistics of Numerical Columns:")
    print(df.describe())

    # Group by species and compute the mean
    grouped = df.groupby('species').mean()
    print("\nMean Values by Species:")
    print(grouped)

    # Step 8: Data Visualization
    # Set style for seaborn
    sns.set(style="whitegrid")

    # Bar chart for average petal length by species
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='species', y='petal length (cm)', ci=None)
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.xticks(ticks=[0, 1, 2], labels=iris.target_names)
    plt.show()

    # Histogram for petal length
    plt.figure(figsize=(10, 6))
    sns.histplot(df['petal length (cm)'], bins=20, kde=True)
    plt.title('Distribution of Petal Length')
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Frequency')
    plt.show()

    # Scatter plot for sepal length vs. petal length
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set1')
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species', labels=iris.target_names)
    plt.show()
else:
    print("Dataset could not be loaded. Please check the error message above.")
