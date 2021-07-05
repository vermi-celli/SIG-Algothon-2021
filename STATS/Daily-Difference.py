#print out daily differences for selected stock

import numpy as np
import pandas as pd 

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

Day = 1
Dailydiff = []
while Day != 250:
    Today = Stockprice[Day]
    Yesterday = Stockprice[Day-1]
    Diff = Today - Yesterday
    #Diff = "{:.4f}".format(diff)
    Dailydiff.append(Diff)
    Day += 1

print(Dailydiff)
