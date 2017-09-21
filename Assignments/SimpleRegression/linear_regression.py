# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:58:22 2017

@author: Keerthi
"""

#A simple regression program showing relation between intrest and median home price
#Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
#Importing the dataset values from Data.csv file
dataset = pd.read_csv('Data.csv')
y = dataset.iloc[:,1].values
x = dataset.iloc[:,:-1].values
#Splitting the dataset file exactly half into train set and test test
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 1/4, random_state = 0)
#Importing LinearRegression function
from sklearn.linear_model import LinearRegression
#Fitting the function to test set
regressor = LinearRegression()
regressor.fit(x_train,y_train)
#Predicting the test set values
y_pred = regressor.predict(x_test)
#Scattering the points of x_test,y_test with blue colour
plt.scatter(x_test,y_test, color = 'green')
#Plotting graph between x_test and y_pred
plt.plot(x_train,regressor.predict(x_train),color = 'green')
#Giving title to the plotted graph
plt.title('Intrest vs Median home price for test set')
#Naming xlabel as Intrest
plt.xlabel('Intrest')
#Naming ylabel as Median home price
plt.ylabel('Median home price')
#Function to show the graph
plt.show()
#Scattering the points of x_train,y_train with blue colour
plt.scatter(x_train,y_train, color = 'blue')
#Plotting graph between x_train and y_pred
plt.plot(x_train,regressor.predict(x_train),color = 'blue')
#Giving title to the plotted graph
plt.title('Intrest vs Median home price for train set')
#Naming xlabel as Intrest
plt.xlabel('Intrest')
#Naming ylabel as Median home price
plt.ylabel('Median home price')
#Function to show the graph
plt.show()

