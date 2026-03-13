import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("houseprice.csv")
X = data[['SquareFeet', 'Bedrooms']]
y = data['Price']

#split the data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split( X,y,test_size=0.2, random_state=42)

#choosing a regression model
from sklearn.linear_model import LinearRegression
model= LinearRegression()

#traiin the model
model.fit(X_train,y_train)

SquareFeet=int(input("enter square feet "))
Bedrooms=int(input("enter no. of beadrooms"))

#predictinon
prediction=model.predict([[SquareFeet,Bedrooms]])
print("HOUSE PRICE PREDICTED",prediction[0])
