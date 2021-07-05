#selects the stocks that are very volatile 

import numpy as np
import pandas as pd 
import statistics as stat

f = open('/Users/ivykim/Downloads/algothon21-main/prices250.txt')
Dataset = []
for X in f:
     Day = X.strip().split()
     Dataset.append(Day)

goodstock = []
for Stock in range(0, 100):
    Stockprice = []
    for X in Dataset:
        Day_Price = float(X[Stock])
        Stockprice.append(Day_Price)
    if stat.variance(Stockprice) > 1.5 :
        Day = 1
        Dailydiff = []
        while Day != 250:
            Today = Stockprice[Day]
            Yesterday = Stockprice[Day-1]
            Diff = Today - Yesterday
            #Diff = "{:.4f}".format(diff)
            Dailydiff.append(Diff)
            Day += 1

        Posneg = []
        Day = 1
        while Day < len(Dailydiff):
            Y = Dailydiff[Day]
            if float(Y) > 0 :
                X = 1
                Posneg.append(X)
                Day += 1 
            if float(Y) == 0 :
                X = 0
                Posneg.append(X)
                Day += 1 
            else:
                X = -1
                Posneg.append(X)
                Day += 1 
        while 0 in Posneg:
           Posneg.remove(0)
        X = 0
        for k in range(0, len(Posneg)-1):
            if Posneg[k+1] == Posneg[k]*(-1):
                X = X +1
            else:
                X = X+0
        if X > 180 :
            goodstock.append(Stock)
        else:
            1
    else: 
        Stock +=1
print(goodstock)
