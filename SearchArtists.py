# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:39:07 2017

@author: Christian Sweet
"""
#Billboard 200.
#Run 1 missing 1990-03-10, some bad corruption in that week.
#Run 2 clears through 1983-11-12, need 1983-11-05.
#Run 3 clears through 1976-07-17, need 1976-07-10, 1976-07-03.
#Run 4 clears through 1967-09-16, need 1967-09-09.
#Run 5 clears through 1967-05-06. (No longer 200 a week, differs.)
#Run 6 clears through 1963-08-24. Done!

#Billboard missing 1976-07-10

#Hot 100.
#Full File.


import billboard

chartHot100 = billboard.ChartData('hot-100')
chartTop200 = billboard.ChartData('billboard-200')

fileHot100 = open("Hot100Artist.txt", "a")
fileTop200 = open("Top200Artist.txt", "a")

while chartHot100.previousDate:
        print(chartHot100.date + " " + str(len(chartHot100)))
        
        for i in range(len(chartHot100)):
            fileTop200.write(chartHot100[i].artist + "\n")
                
        chartHot100 = billboard.ChartData('hot-100', chartHot100.previousDate)

print("\n Finished compiling hot 100. " + '\n')

while chartTop200.previousDate:
        print(chartTop200.date + " " + str(len(chartTop200)))
        
        for i in range(len(chartTop200)):
            fileTop200.write(chartTop200[i].artist + "\n")
                
        chartTop200 = billboard.ChartData('billboard-200', chartTop200.previousDate)

print("\n Finished compiling top 200. " + '\n')