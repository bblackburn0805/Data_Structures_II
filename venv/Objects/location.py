# Objects.location.py
#
# Allows for easy storage and access of locations
# >>> Time complexity: O(N)
# >>> Space complexity: O(1)

class location:
    def __init__(self, row, id):
        self.locationID = id
        if row != 0:
            self.distances = []
            x = 1
            s = row[0]
            zipStart = int(s.find('(')) + 1
            zipEnd = int(s.find(')'))
            self.zip = int(s[zipStart : zipEnd])
            self.address = s[0:zipStart - 2]

            # Set the distances array
            while(x < len(row)):
                if row[x] != '':
                    self.distances.append(float(row[x]))
                else:
                    self.distances.append(0)
                x += 1

    def __str__(self):
        return self.address


# Return a location list from .csv data.
# >>> Time complexity: O(N^2)
# >>> Space complexity: O(N)
def newLocationList(data):
    locationList = []
    x = 0
    for item in data:
        locationList.append(location(data.get(item), x))
        x += 1

    # The list of locations put together makes an ajacency matrix.
    # Since the distance is the same from point A to B
    # and then B to A, the matrix can be reflected.
    # Here we have a temporary arrray, invertedDistances,
    # which will store the values from the matrix from
    # top to bottom. Once it has all of one column, it then
    # pastes it into the row.
    # >>> Time complexity: O(N^2)
    # >>> Space complexity: O(N)
    invertedDistances = [float] * len(locationList)
    x = 0
    while x < len(locationList) - 1:
        y = 0
        for place in locationList:
            invertedDistances[y] = place.distances[x]
            y += 1
        locationList[x].distances = invertedDistances.copy()
        x += 1
    return locationList

#Standard search function, find lcoation by address. Return locationID
# >>> Time complexity: O(N)
# >>> Space complexity: O(1)
def searchLocation(search, locationList):
    for location in locationList:
        if location.address == search:
            return location.locationID