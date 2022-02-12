# Algorithms.routing.py
#
# Contains setPath and selectShortestPath methods


from Objects.package import *
from Objects.truck import *


# Sets the truck attributes: destinationID, currentDelivery
# Used to determine where the truck is going next.
def setPath(truck, locationList):

    path = []
    shortestPath = []
    priority = []
    selectedPackage = 0
    path.clear()
    shortestPath.clear()
    # If truck is out of packages, set the path to the hub. destinationID is set to 0, which is the locationID of the hub.
    #>>> Time complexity: O(1)
    #>>> Space complexity: O(1)
    if len(truck.packages) == 0:
        min = selectShortestPath(0, truck.currentLocationID, locationList, path)
        shortestPath = path.copy()
        selectedPackage = 0
        truck.destinationID = 0
        truck.currentDelivery = 'None'

    # If the truck has packages left, it will attempt to find the package that is the closest to deliver. Min is set
    # at 1000 miles (guaranteed to be replaced), and keeps track of which package has the least distance from current location.
    # The packages with a deadline are added to a priority list. If there are no deadline packages, the priority list
    # is set as the normal list of packages on the truck.
    #>>> Time complexity: O(N)
    #>>> Space complexity: O(N)
    else:
        min = 1000
        for selected in truck.packages:
            if selected.deadline != 'EOD':
                priority.append(selected)
        if len(priority) == 0:
            priority = truck.packages

        # For each package in the priority list, the shorest distance to the destination is calculated and is stored in
        # miles. If the miles for this package has the lowest distance, min is replaced by this packages distance,
        # selectedPackage is set to this package, and the path is copied into shorestPath.
        # Once the shortest distance is determined, it updates the truck's destinationID, currentDelivery, path, and mileage.
        # >>> Time complexity: O(N)
        # >>> Space complexity: O(N)
        for selected in priority:
            miles = selectShortestPath(selected.locationID, truck.currentLocationID, locationList, path)
            if (miles < min):
                min = miles
                shortestPath.clear()
                shortestPath.append(path.copy())
                selectedPackage = selected
                truck.destinationID = selectedPackage.locationID
                truck.currentDelivery = selectedPackage
    truck.path = shortestPath.copy()
    truck.mileage += min


# My algorithm to determine the shortest path. It uses a greedy algorithm to determine a path that has the shortest
# distances to arrive to the destination. It then compares distances of that path to the direct path, and returns which
# one is shorter.
# In the adjacency matrix of the locationList, each locationID is numbered and is in order. If the current location ID is
# less than the destination location ID, then the algorithm checks to the right of the current location and checks every
# location with an ID higher than the current until the destination is reached. The algorithm searches left if the
# destination ID is less than the current ID. X represents which direction it is searching. 1 = right, -1 = left. 0 = Here.
#>>> Time complexity: O(1)
#>>> Space complexity: O(1)
def selectShortestPath(destination, current, locationList, path):
    if current < destination:
        x = 1
    elif current > destination:
        x = -1
    elif current == destination:
        return 0
    direct = locationList[current].distances[destination]
    miles = 0
    tempLoc = int(current)

    # Search direction (x) is determined, tempLoc is where our driver is currently thinking about going. tempLoc is used
    # to track where he is going until the destination is reached. It is initialized as the next location in x direction.
    #>>> Time complexity: O(N^2) - for N locations in x direction, it must check N - ? distances. O(N * N -2) = O(N^2)
    #>>> Space complexity: O(1)
    while (tempLoc != destination):
        min = locationList[tempLoc].distances[tempLoc+x]
        minID = tempLoc + x
        pointer = minID

        # Pointer is a placemark that moves in x direction and is used to select the distance to the next location in line.
        # Using the location object's distance list, the distance to the next location is found. Once the pointer has reached
        # the destination, the total distance is evaluated and if it is lower than the current min, the distance is set
        # as the new min and the pointer is set to the minID location.
        # Onced tempLoc has reached the destination, the minimum distance of each location towards the destination has
        # beed added up. This path distance is compared to the direct path distance, and will return either the
        # path the pointer has created, or the direct path.
        # >>> Time complexity: O(N)
        # >>> Space complexity: O(N)
        while(pointer != destination):
            pointer += x
            distance = locationList[tempLoc].distances[pointer]
            if distance <= min:
                minID = pointer
                min = distance
        tempLoc = minID
        path.append(tempLoc)
        miles += min
    if miles < direct:
        return miles
    else:
        path.clear()
        path.append(destination)
        return direct

