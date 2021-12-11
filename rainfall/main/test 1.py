# import the libraries
from tkinter.messagebox import showinfo
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# data= pd.read_csv("1.csv")
# df = pd.DataFrame(data, columns= ['SUBDIVISION','YEAR','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','ANNUAL','Jan-Feb','Mar-May','Jun-Sep','Oct-Dec'])
#
# select_color = df.loc[df['SUBDIVISION'] == 'ANDAMAN & NICOBAR ISLANDS']
# print (select_color)

# Import module
from tkinter import *

# Create object
# root = Tk()
#
# # Adjust size
# root.geometry( "200x200" )
#
# # Change the label text
# def show():
# 	label.config( text = clicked.get() )
#
# # Dropdown menu options
# options = [
# 	"Monday",
# 	"Tuesday",
# 	"Wednesday",
# 	"Thursday",
# 	"Friday",
# 	"Saturday",
# 	"Sunday"
# ]
#
# # datatype of menu text
# clicked = StringVar()
#
# # initial menu text
# clicked.set( "Monday" )
#
# # Create Dropdown menu
# drop = OptionMenu( root , clicked , *options )
# drop.pack()
#
# # Create button, it will change label text
# button = Button( root , text = "click Me" , command = show ).pack()
#
# # Create Label
# label = Label( root , text = " " )
# label.pack()
#
# # Execute tkinter
# root.mainloop()
#


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

# df=pd.read_csv("final.csv")
# list_of_column_names = list(df.columns)
# print(list_of_column_names)

# ip = np.array([[1901],[1]])
# ip = ip.reshape(1, -1)
# print(ip[0][1])


data = pd.read_csv("2a.csv")
# # if (var1.get() == '123'):
# #     showinfo("Invalid input", "please select a state")
# df = pd.DataFrame(data,
#                   columns=['SUBDIVISION', 'YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP',
#                            'OCT', 'NOV', 'DEC'])
#
# data = df.loc[df['SUBDIVISION'] == ]

x = data['YEAR']
x = x.values.reshape(-1, 1)
# x=x.drop(['Unnamed: 0'],axis=1)
# if (var.get() == '123'):
#     showinfo("Invalid input", "please select a month")
y = data['JAN']
y = y.values.reshape(-1, 1)

clf = LinearRegression()
clf.fit(x, y)

v = 2000
# if (v <= 0 and v > 10000):
#     showinfo("Invalid input", "please use a valid year")
inp = np.array(v)
inp = inp.reshape(1, -1)
# Print output
# showinfo("output", f"The precipitation in inches for the input is:,{clf.predict(inp)}")
# ip = np.array(1901)
# ip = ip.reshape(1, -1)
# c=clf.predict(inp)
# print(c[0][0])
# x=clf.predict(ip)
# plt.plot(c[0][0],x[0][0])
# plt.show()
x_axis=([1901,v])
print(x_axis)
# x1=[1,2]
# y1=[1,2]
#
# plt.plot(x1,y1,color='r')
# plt.show()
