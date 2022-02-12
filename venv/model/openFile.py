#model.openFile.py
#
# Opens file, readed each row with ',' as delmiters, and returns the information
#   as a list of rows.

import csv

# Open the CSV fileName, put each row into dictionary info, and return info.
# >>> Time complexity: O(N)
# >>> Space complexity: O(N)

def openFile(fileName):
    info = {}
    
    with open(fileName) as csvfile:
        inputFile = csv.reader(csvfile)
        x = 0
        for row in inputFile:
            info[x] = row
            x += 1
    csvfile.close()
    return info