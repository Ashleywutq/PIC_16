# -*- coding: utf-8 -*-

"""
Assignment_3F_PIC16
Ashley Wu
ID 204612415
"""

import csv
import re

with open ('data.csv','rb') as infile:
    reader = csv.reader(infile)
    reader=list(reader)
    
    #change first line names
    reader[0][0] = 'First'
    reader[0][1] = 'M.I.'
    reader[0].append('Last')
    reader[0].append('Phone')
    newlist=[]
    newlist.append(reader[0])
    
    #delete wrong numbers and format the right numbers to phone column
    for row in reader:
        pattern = r"(\d{3})\)?\.?\s?-?(\d{3})\s?-?\.?(\d{4})"
        search_num = re.search(pattern, row[1])
        if search_num != None:
            row.append('0')
            append_string= "(" + search_num.group(1) + ") " + search_num.group(2) + "-"+\
            search_num.group(3)
            row.append(append_string)
            newlist.append(row)
    
    #format the name 
    for row in newlist:
        if row != newlist[0]:
            search_pattern = re.search(r",",row[0])
            if search_pattern == None:
                pattern1 = r"(\w+)\s(\w+\.)?\s?(\w+)"
                search_pattern1 = re.search(pattern1, row[0])
                row[0] = search_pattern1.group(1) or ""
                row[1] = search_pattern1.group(2) or ""
                row[2] = search_pattern1.group(3) or ""
              
            else:
                pattern2 = r"(\w+),\s(\w+)\s?(\w+\.)?"
                search_pattern2 = re.search(pattern2, row[0])
                row[0] = search_pattern2.group(2) or ""
                row[1] = search_pattern2.group(3) or ""
                row[2] = search_pattern2.group(1) or ""
               

with open ('data2.csv','wb') as outfile:
    writer=csv.writer(outfile,delimiter=',',quotechar='', quoting=csv.QUOTE_NONE)
    for row in newlist:
        writer.writerow(row)

    