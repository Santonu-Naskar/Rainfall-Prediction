# import the libraries
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data= pd.read_csv("1.csv")
df = pd.DataFrame(data, columns= ['SUBDIVISION','YEAR','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','ANNUAL','Jan-Feb','Mar-May','Jun-Sep','Oct-Dec'])

select_color = df.loc[df['SUBDIVISION'] == 'ANDAMAN & NICOBAR ISLANDS']
print (select_color)



# # read the cleaned data
# data = pd.read_csv("2a.csv")
#
#
# X = data['YEAR']
# X = X.values.reshape(-1, 1)
# Y = data["JAN"]
# Y = Y.values.reshape(-1, 1)
# print(X)
# print(Y)
# #
# # # day_index = 2021
# # # days = [i for i in range(Y.size)]
# #
# clf = LinearRegression()
# clf.fit(X, Y)
#
# inp = np.array(2021)
# #
# inp = inp.reshape(1, -1)
#
# # Print output
# print('The precipitation in inches for the input is:', clf.predict(inp))




