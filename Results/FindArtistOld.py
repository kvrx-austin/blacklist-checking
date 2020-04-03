# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 11:02:26 2017

@author: CSweet
"""


while(True):
    print("")
    var = input("Please Enter An Artist: ")
    
    foundAResult = False
    
    for line in open("CleanComboArtist.txt", "r"):
        if var.lower() in line.lower():
            print("")
            print("The artist " + var + " was found. One moment...")
            
            Hot100Counter = 1
            Hot100Found = False
            
            for HotLine in open("Hot100Artist.txt", "r"):
                if var.lower() in HotLine.lower():
                    foundAResult = True
                    break
                else:
                    Hot100Counter+=1
            
            if not Hot100Found:
                Top200Counter = 1
                for TopLine in open("Top200Artist.txt", "r"):
                    if var.lower() in TopLine.lower():
                        foundAResult = True
                        break
                    else:
                        Top200Counter += 1
            
            if Hot100Found:
                TimeAgo = (int)((Hot100Counter/100)/52)
                
                if TimeAgo > 1:
                    print(var + " had a Hot 100 hit about " + str(TimeAgo) + " years ago. (Matched with artist " + line + ".)")
                
                else:
                    TimeAgo = (int)(Hot100Counter/100)
                    print(var + " had a Hot 100 hit about " + str(TimeAgo) + " weeks ago. (Matched with artist " + line + ".)")
            
            else:
                TimeAgo = (int)((Top200Counter/200)/52)
                
                if TimeAgo > 1:
                    print(var + " had a Billboard 200 hit about " + str(TimeAgo) + " years ago. (Matched with artist " + line + ".)")
                
                else:
                    TimeAgo = (int)(Top200Counter/200)
                    print(var + " had a Billboard 200 hit about " + str(TimeAgo) + " weeks ago. (Matched with artist " + line + ".)")
        
    if not foundAResult:
        print("")
        print("The artist was not found in the Hot 100 or Billboard 200 charts.")