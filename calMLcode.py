# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load California Housing dataset
california = fetch_california_housing()

# Convert to Pandas dataframe
df = pd.DataFrame(california.data, columns=california.feature_names)

# Add target variable to dataframe
df['target'] = california.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[california.feature_names], df['target'], test_size=0.2, random_state=42)

# Create a Linear Regression model object
lr = LinearRegression()

# Train the model on the training data
lr.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = lr.predict(X_test)

# Evaluate the model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the model's mean squared error and R-squared value
print('Mean Squared Error: ', mse)
print('R-squared: ', r2)