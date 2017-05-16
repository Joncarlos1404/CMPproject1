# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:51:50 2017

@author: Joncarlos Tavarez
"""

import csv 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


Rate1     = []
Rate2     = []
Rate3     = []
RateAver  = []
GameSales = []

with open('PS2games.csv') as f:
    reader = csv.DictReader(f) 
    for row in reader: 
            GameSales.append(float(row['Global']))
            Rate1.append(int(row['Rating1']))
            Rate2.append(10 * float(row['Rating2']))
            Rate3.append(10 * float(row['Rating2']))

        
def findAver():
    for i in range(len(Rate1)):
        RateAver.append((Rate1[i] + int(Rate2[i]) + int(Rate3[i])) //3)
        
     
     
def main():
    findAver()
    
    x = RateAver
    y = GameSales
    
    data = pd.read_csv('PS2games.csv', skiprows=0)
    
    print('The Games, global sale, and Rating csv file')
    print(data)
    print('The correlation between the global sells and average website rating is ',correlation(x,y))

    
    plt.scatter(x, y, color ='b', label = "Correlation")
    plt.title('Correlation of Sales and Rating')
    plt.xlabel('Average video game rating')
    plt.ylabel('Video Game Sales (Millions)')
   
    axes = plt.gca()
    m, b = np.polyfit(x, y, 1)
    X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
    plt.plot(X_plot, m*X_plot + b, '-',color='r')
    
   
main()