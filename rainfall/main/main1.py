from tkinter import *
from tkinter.messagebox import showinfo
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# function call
def cal():
    print(var1.get())
    data = pd.read_csv("2a.csv")
    df = pd.DataFrame(data,
                      columns=['SUBDIVISION', 'YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP',
                               'OCT', 'NOV', 'DEC'])

    data= df.loc[df['SUBDIVISION'] == var1.get()]

    x = data['YEAR']
    x = x.values.reshape(-1, 1)
    print(x)
    # x=x.drop(['Unnamed: 0'],axis=1)
    if (var=='123'):
        showinfo("Invalid input", "please select a month")
    y = data[var.get()]
    y = y.values.reshape(-1, 1)
    #
    # # day_index = 2021
    # # days = [i for i in range(Y.size)]
    #
    clf = LinearRegression()
    clf.fit(x, y)

    v = int(Year.get())
    if (v<=0 and v>10000 ):
        showinfo("Invalid input", "please use a valid year")
    inp = np.array(v)
    inp = inp.reshape(1, -1)
    # Print output
    showinfo("output",f"The precipitation in inches for the input is:,{clf.predict(inp)}")

#GUI
root=Tk()
root.geometry("600x600")
# root.title("rainfall prediction")

Label(root, text="Enter year and choose any one of these",font="any 15 underline",fg="#f58d25").grid(row=0,column=3,ipady=10)
Label(root, text="    Year =",font="any 13 bold",foreground="#853535").grid(row=1,column=1)
Year=Entry(root,justify=LEFT,bg="#cafad2",font="any 12 bold",fg="red")
Year.grid(row=1,column=2,ipady=5,pady=17,ipadx=15)


var=StringVar()
var.set("123")
Radiobutton(root,text="Jan",variable=var, value="JAN",font="any 12",foreground="blue").grid(row=3,column=2)
Radiobutton(root,text="Feb",variable=var, value="FEB",font="any 12",foreground="blue").grid(row=4,column=2)
Radiobutton(root,text="Mar",variable=var, value="MAR",font="any 12",foreground="blue").grid(row=5,column=2)
Radiobutton(root,text="Apr",variable=var, value="APR",font="any 12",foreground="blue").grid(row=6,column=2)
Radiobutton(root,text="May",variable=var, value="MAY",font="any 12",foreground="blue").grid(row=7,column=2)
Radiobutton(root,text="Jun",variable=var, value="JUN",font="any 12",foreground="blue").grid(row=8,column=2)

obj=['ANDAMAN & NICOBAR ISLANDS', 'ARUNACHAL PRADESH', 'ASSAM & MEGHALAYA', 'NAGA MANI MIZO TRIPURA', 'GANGETIC WEST BENGAL', 'ORISSA', 'JHARKHAND', 'BIHAR', 'EAST UTTAR PRADESH', 'WEST UTTAR PRADESH', 'UTTARAKHAND', 'HARYANA DELHI & CHANDIGARH', 'PUNJAB', 'HIMACHAL PRADESH', 'JAMMU & KASHMIR', 'WEST RAJASTHAN' , 'EAST RAJASTHAN', 'WEST MADHYA PRADESH', 'EAST MADHYA PRADESH', 'GUJARAT REGION', 'SAURASHTRA & KUTCH', 'KONKAN & GOA', 'MADHYA MAHARASHTRA', 'MATATHWADA', 'VIDARBHA', 'CHHATTISGARH', 'COASTAL ANDHRA PRADESH', 'TELANGANA', 'RAYALSEEMA', 'TAMIL NADU', 'COASTAL KARNATAKA', 'NORTH INTERIOR KARNATAKA', 'SOUTH INTERIOR KARNATAKA', 'KERALA', 'LAKSHADWEEP',]
var1=StringVar()
var.set('ANDAMAN & NICOBAR ISLANDS')

OptionMenu(root,var1,*obj).grid(row=9,column=2)
Label(root, text="      Select -> :)",font="any 13 bold",foreground="#853535").grid(row=9,column=1)
Button(text="Calculate Now", command=cal, activebackground = "yellow",border=5).grid(row=11,column=2,pady=20,ipadx=25)
root.mainloop()
