
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("1.csv")

# drop (delete) the unnecessary columns in the data
data = data.drop(
    ['SUBDIVISION'], axis=1)

data.fillna(0, inplace=True)
# data = data.replace('', 1.0)

# Save the data in a csv file
data.to_csv('2a.csv')