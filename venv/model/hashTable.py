# model.hashTable.py
#
# reads in data from a .csv file, that is seperated by rows.
# Each row represents a package.
#
#
# Determines if the amount of packages exceeds 100. If it doesn't, there are 10 buckets made in the Hash Table.
# If there are more than 100, there are 100 buckets made in the Hash Table. The amount of items that will be
# stored in each bucket grows with the amount of packages.
# 0-9, there is one bucket
# 10-99, there are 10 buckets
# 100-999, there are 100 buckets
# 1000-9999, there are 1000 buckets
#               ... and so forth.
# If there is exactly 10 ^ N packages, then each bucket will have exactly 1 package.
# If there are (10 ^ N) - 1, then there will be 9*(10^(N-1)) packages in each bucket, or simply just 9.
#               ^ (meaning if there are 9999 packages, each of the 1000 buckets will have 9 packages)
#
#
# This Hash Table is designed to grow with the amount of packages, regardless the amount of packages.
# The number of buckets is equivalent to the number of digits in the amount of total packages.
# The bucket that each package is inserted into is relevent to the unique ID number. The bucket can be
# found quickly by hash-function:   (ID) modulo (%) ((number of digits of total packages) - 1).
# The buckets are appended each time they have a number assigned to them. If one wants to search the hash table
# for an ID, the bucket will be known immediately. It will search through the bucket until the ID is matched.
# This algorithm of appending a bucket, then searching through a bucket to find a package is called Chaining.
#
# The best case scenario is there are exactly 10 ^ N packages, because there would be no searching through buckets.
# Each of the packages would be the only package in a bucket.
# Best case Scenario is O(1)
#
# The worst case scenario is there are (10 ^ N) - 1 packages. Each search would have to search up to 9 buckets.
# Assuming each package is at the end of the bucket, the worst case scenario is 9*(10^N-1)), which comes down
# to having Big O notation of O(N).
class hashTable:

    def __init__(self, size):
        # Assign number of buckets
        # Hash table is an array of tuple arrays. (key, packageInfo)
        # >>> Time complexity: O(N)
        # >>> Space complexity: O(N)
        self.buckets = 10 ** (len(str(size)) - 1)
        self.hashTable = [[] for i in range(self.buckets)]

    # Item[0] is the packageID. Insert - into HashTable array - the tuple (packageID, info)
    # >>> Time complexity: O(1)
    # >>> Space complexity: O(1)
    def insert(self, item):
        self.hashTable[int(item[0]) % self.buckets].append([int(item[0]), item])

    def __iter__(self):
        self.b = 0
        return self

    def __next__(self):
        for bucket in self.hashTable:
            if self.b <= len(self.hashTable):
                self.b += 1
                for item in bucket:
                    return item
            else:
                raise StopIteration

    # Update hash table address info
    # >>> Time complexity: O(N)
    # >>> Space complexity: O(1)
    def updateAddress(self, packageID, address, city, state, zip):
        for item in self.hashTable[packageID % self.buckets]:
            if packageID == item[0]:
                item[1][1] = address
                item[1][2] = city
                item[1][3] = state
                item[1][4] = zip

    # Delete entry from hash table
    # >>> Time complexity: O(N)
    # >>> Space complexity: O(1)
    def deleteEntry(self, packageID):
        for item in self.hashTable[packageID % self.buckets]:
            if packageID == item[0]:
                self.hashTable[packageID % self.buckets].remove(item)

    #Search the hash by packageID
    # >>> Time complexity: O(N)
    # >>> Space complexity: O(1)
    def search(self, packageID):
        for item in self.hashTable[packageID % self.buckets]:
            if packageID == item[0]:
                return item[1]



# Take data in from the .csv file, each row is a new entry into the table.
# >>> Time complexity: O(N)
# >>> Space complexity: O(N)
def newHashTable(data):
    newHash = hashTable(len(data))
    for item in data:
        newHash.insert(data.get(item))
    return newHash