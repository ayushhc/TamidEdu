# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Loading Boston Housing dataset
boston = load_boston()

# Creating a Pandas dataframe from the dataset
df = pd.DataFrame(boston.data, columns=boston.feature_names)

# Adding the target variable to the dataframe
df['target'] = boston.target

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[boston.feature_names], df['target'], test_size=0.2, random_state=42)

# Creating a list of regression models
models = [
    LinearRegression(),
    Lasso(),
    Ridge(),
    ElasticNet()
]

# Training and evaluating each model
for model in models:
    # Training the model on the training data
    model.fit(X_train, y_train)

    # Making predictions on the testing data
    y_pred = model.predict(X_test)

    # Evaluating the model performance
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Printing the model's name, mean squared error, and R-squared value
    print(model.__class__.__name__)
    print('Mean Squared Error: ', mse)
    print('R-squared: ', r2)