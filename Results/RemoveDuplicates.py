# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 09:43:03 2017

@author: CSweet
"""

lines_seen = set() # holds lines already

outfile = open("CleanComboArtist2.txt", "w")

for line in open("CleanTop200Artist2.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)

for line in open("CleanHot100Artist2.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)

outfile.close()