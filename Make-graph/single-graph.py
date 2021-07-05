# use this file to look at specific stocks one at a time
#replace number in line 20, remember that python reads numbers from 0


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

f = open('/Users/ivykim/Downloads/algothon21-main/prices250.txt')

Stock = input("Enter stock number: ")
Stock = int(Stock)
Dataset = []
for X in f:
     Day = X.strip().split()
     Dataset.append(Day)
Stockprice = []
for X in Dataset:
    Day_Price = float(X[Stock])
    Stockprice.append(Day_Price)

Daylist = range(1, 251)
plt.plot(Daylist, Stockprice)
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()
