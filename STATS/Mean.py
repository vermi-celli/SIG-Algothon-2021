import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import random as rdm
import statistics as stat


days = []
f = open('/Users/ivykim/Downloads/algothon21-main/prices250.txt')
    #days = f.readlines()

listlist = []
for line in f:
     Day = line.strip()
     Price_Day = Day.split()
     listlist.append(Price_Day)

print("Stock | Mean |Sample Variance | Population Variance | Sample St.dev | Population St.dev")
Count = 0
while Count != 100:
    Stock = Count
    Progress = []
    Stockmove = []
    for type in listlist:
        Price = type[Stock]
        Progress.append(Price)
        Progress = list(map(float, Progress))
    print ("Stock %(number)s: %(mean).3f %(var).5f %(pvar).5f %(sdev).5f %(psdev).5f" % 
        {"number": Count+1, "mean": stat.mean(Progress), "var":stat.variance(Progress), "pvar":stat.pvariance(Progress), "sdev":stat.stdev(Progress), "psdev":stat.pstdev(Progress)})
    Count = Count +1




