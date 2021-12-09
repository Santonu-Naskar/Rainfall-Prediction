
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("weather_data_nyc_centralpark_2016(1).csv")

# drop (delete) the unnecessary columns in the data
data = data.drop(
    [ 'date','snow fall','snow depth'], axis=1)

data=data.replace('T',0)
data = data.replace('-', 0.0)

# Save the data in a csv file
data.to_csv('final.csv')