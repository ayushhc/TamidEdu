#Ayush Chintalapani
#Advik Nakirikanti

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

california = fetch_california_housing()

df = pd.DataFrame(california.data, columns=california.feature_names)

df['target'] = california.target

X_train, X_test, y_train, y_test = train_test_split(df[california.feature_names], df['target'], test_size=0.2, random_state=42)

lr = LinearRegression()

lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Squared Error: ', mse)
print('R-squared: ', r2)