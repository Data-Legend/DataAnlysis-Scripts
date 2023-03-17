# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the dataset and create a Pandas dataframe
# Replace the dataset path with the path to your dataset or a URL
dataset_path = './data.csv'
dt = pd.read_csv(dataset_path)

# Step 3: Check the shape, data types and basic information of the dataframe
print("Shape of the dataframe: ", dt.shape)
print("\nData types of the dataframe: \n", dt.dtypes)
print("\nInfo of the dataframe: \n")
dt.info()

# Step 4: Check for missing and null values
missing_values = dt.isnull().sum()
print("\nMissing values in the dataframe: \n", missing_values)

# Step 5: Perform descriptive statistics
print("\nDescriptive statistics of the dataframe: \n", dt.describe(include='all'))

# Step 6: Visualize the dataset
# You can use Seaborn or Matplotlib to create visualization plots

# Example using Seaborn to create a pairplot
# If you have categorical columns, adjust this line accordingly
sns.pairplot(dt)
plt.show()

# Step 7: Perform Feature Engineering (if necessary)
# This step will depend on the dataset you are working with
# Examples include one-hot encoding, scaling, dropping features, etc.

# Step 8: Save the results
# If you want to save the cleaned dataframe to a new csv file:
dt.to_csv('cleaned_data.csv', index=False)
# If you want to save graphs or plots, use the savefig() function from matplotlib.pyplot
# Example for saving a seaborn pairplot:
# pairplot = sns.pairplot(dt)
# pairplot.savefig('pairplot.png')
