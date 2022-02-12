#Objects.package.py

# Package class. Makes accessing package info easier
# >>> Time complexity: O(1)
# >>> Space complexity: O(1)

class package:
    def __init__(self, item):
        if item != '':
            self.packageID = int(item[0])
            self.address = item[1]
            self.city = item[2]
            self.state = item[3]
            self.zip = item[4]
            self.deadline = item[5]
            self.weight = float(item[6])
            self.notes = item[7]
            self.deliveryStatus = "At hub"
            self.locationID = 0


    def __str__(self):
        return '{:10}'.format("ID: " + self.packageID.__str__()) + '{:30.25}'.format(self.address) + '{:30}'.format("Deadline: " + str(self.deadline)) + '{:40}'.format(self.deliveryStatus)

    # Less than method, to sort the package list by ID
    # >>> Time complexity: O(1)
    # >>> Space complexity: O(1)
    def __lt__(self, other):
        if self.packageID < other.packageID:
            return True
        else:
            return False

    # Converts time to minutes. No packages have a PM time, so PM times are not accounted for.
    # >>> Time complexity: O(1)
    # >>> Space complexity: O(1)
    def convertTime(self):
        if self.deadline != 'EOD':
            s = self.deadline.find(':')
            hour = int(self.deadline[0: s]) - 8
            minute = int(self.deadline[s + 1: s + 3])
            return (hour * 60) + minute


# takes the hashtable and makes it easier to work with
# by making a package object list.
# >>> Time complexity: O(N^2)
# >>> Space complexity: O(N)
def newPackageList(hashTable):
    packageList = []
    for bucket in hashTable:
        for item in bucket:
            packageList.append(package(item[1]))
    return packageList


