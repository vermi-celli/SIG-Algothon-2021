import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import random as rdm

days = []
f = open('/Users/ivykim/Downloads/algothon21-main/prices250.txt')
    #days = f.readlines()

listlist = []
for line in f:
     Day = line.strip()
     Price_Day = Day.split()
     listlist.append(Price_Day)

#for grp in list_groups:
    #plt.figure()
    #plt.plot(grp)
    #plt.show()


k=0
while k != 10:
    Count = rdm.randint(0, 99)
    Stock = Count
    Progress = []
    Stockmove = []
    for type in listlist:
        Price = type[Stock]
        Progress.append(Price)
    for x in Progress:
        Price = float(x)
        Stockmove.append(Price)
    Daylist = range(1, 251)
    plt.figure(Count)
    plt.plot(Daylist, Stockmove)
    plt.xlabel('Day')
    plt.ylabel('Price')
    plt.title('Stock'+str(Count))
    plt.savefig("/Users/ivykim/Documents/Algothon/Stock" + str(Count) + ".png")
    k = k+1

#count=0
#for day in days: 
    #count += 1
    #print(f'day {count}: {day}')

#listlist[1] gets 100 instruments on first day