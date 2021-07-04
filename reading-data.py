import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

days = []
f = open('/Users/ivykim/Downloads/algothon21-main/prices250.txt')
    #days = f.readlines()

listlist = []
for line in f:
     Day = line.strip()
     Price_Day = Day.split()
     listlist.append(Price_Day)

Progress = []
Stock = 0 #choose the instrument
for list in listlist:
    Price = list[Stock]
    Progress.append(Price)

Stockmove = []
for str in Progress:
    Price = float(str)
    Stockmove.append(Price)

Daylist = range(1, 251)
plt.plot(Daylist, Stockmove)
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()

#count=0
#for day in days: 
    #count += 1
    #print(f'day {count}: {day}')

#listlist[1] gets 100 instruments on first day
