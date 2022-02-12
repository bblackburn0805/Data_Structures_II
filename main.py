# Brandon Blackburn, StudentID #001015925
# main.py

from model.openFile import openFile
from model.hashTable import newHashTable
from model.mainMenu import mainMenu
from Objects.location import newLocationList

# Location of data files
WGUPS_FILENAME = "venv/data/WGUPS.csv"
PACKAGES_FILENAME = "venv/data/packages.csv"

# Opens WGUPS location .csv file. Returns data with delimiter ','
data = openFile(WGUPS_FILENAME)
# Data is entered into a function of the location object.
# Returns a list of Location objects. Objects.location.py
# >>> Time complexity: O(N)
# >>> Space complexity: O(N)
locationList = newLocationList(data)

# Opens package .csv file. Returns data with delimiter ','
# Makes a new hash table with the data, then updates the incorrect address
# >>> Time complexity: O(N)
# >>> Space complexity: O(N)
data = openFile(PACKAGES_FILENAME)
packageHash = newHashTable(data)
packageHash.updateAddress(9, '410 S State St', 'Salt Lake City', 'UT', '84111')
mainMenu(locationList, packageHash.hashTable)
