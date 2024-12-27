# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Insert the correct path to your dataset file
file_path = r'C:\Users\Admin\Downloads\archive\score.csv'  # Ensure the file extension matches your file type (.csv)

# Load your dataset
df = pd.read_csv(file_path)

# Display the first few rows and the column names to confirm the data is loaded correctly
print("First few rows of the dataset:")
print(df.head())
print("\nColumn names in the dataset:")
print(df.columns)

# Manually set the correct column names based on the dataset structure
interval_column = 'Hours'    # Column representing study hours
frequency_column = 'Scores'  # Column representing the corresponding scores or count

# Check if the column names set above are correct
if interval_column not in df.columns or frequency_column not in df.columns:
    print(f"Error: Column names '{interval_column}' or '{frequency_column}' do not exist in the data.")
    print("Please update the column names in the code based on the dataset's structure.")
else:
    # Plotting a Histogram
    plt.figure(figsize=(10, 5))
    sns.histplot(data=df, x=interval_column, weights=frequency_column, bins=len(df), color='skyblue')
    plt.title('Histogram of Daily Study Hours')
    plt.xlabel('Study Hours')
    plt.ylabel('Scores')
    plt.show()

    # Plotting a Bar Chart
    plt.figure(figsize=(10, 5))
    sns.barplot(x=interval_column, y=frequency_column, data=df, palette='viridis')
    plt.title('Bar Chart of Daily Study Hours vs. Scores')
    plt.xlabel('Study Hours')
    plt.ylabel('Scores')
    plt.show()

    # Plotting a Horizontal Bar Chart
    plt.figure(figsize=(10, 5))
    sns.barplot(y=interval_column, x=frequency_column, data=df, palette='magma')
    plt.title('Horizontal Bar Chart of Daily Study Hours vs. Scores')
    plt.xlabel('Scores')
    plt.ylabel('Study Hours')
    plt.show()

    # Plotting a Scatter Plot
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=interval_column, y=frequency_column, data=df, color='blue', s=100, marker='o')
    plt.title('Scatter Plot of Study Hours vs. Scores')
    plt.xlabel('Study Hours')
    plt.ylabel('Scores')
    plt.grid(True)
    plt.show()

    # Plotting a Line Plot
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=interval_column, y=frequency_column, data=df, marker='o', linestyle='-', color='red')
    plt.title('Line Plot of Study Hours vs. Scores')
    plt.xlabel('Study Hours')
    plt.ylabel('Scores')
    plt.grid(True)
    plt.show()

    # Optional: Plotting a Box Plot if you want to visualize the distribution of Scores
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=df[frequency_column], color='lightgreen')
    plt.title('Box Plot of Scores')
    plt.xlabel('Scores')
    plt.show()
