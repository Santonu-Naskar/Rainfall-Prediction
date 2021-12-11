
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("1.csv")

# drop (delete) the unnecessary columns in the data
data = data.drop(
    ['ANNUAL','Jan-Feb','Mar-May','Jun-Sep','Oct-Dec'], axis=1)
#
data=data.replace(np.nan,0.0)
data = data.replace('', 0.0)

# Save the data in a csv file
data.to_csv('2a.csv')