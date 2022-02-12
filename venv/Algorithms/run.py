# Algorithms.run.py
#   This is where the simulation happens. The arguments are the locations, the hashtable, the selected end time (if any),
# and the trucks that are used. The trucks are passed in and edited so that their info is reserved.
#   The hash table is converted into a list of packages objects to make searching for specific info easier.


from Algorithms.routing import *
from Algorithms.hub import *
from Objects.truck import *
from Objects.location import *
from Objects.package import *


def run(locationList, packageHash, endTime, trucks):
    # Import the hash table into a list of package objects. Sort. Then assign the corresponding locationID to each package.
    #>>> Time complexity: O(N^2) - N number of locations are searched for N number of packages
    #>>> Space complexity: O(N)
    packageList = newPackageList(packageHash)
    packageList.sort()
    for package in packageList:
        package.locationID = searchLocation(package.address, locationList)

    # Remaining packages is a copy of the all the packages, and once a package is packed from the hub it is removed
    # from the remainingPackages list. The trucks are initally loaded, and their paths are set.
    #>>> Time complexity: O(N^2) - setPath is O(N^2)
    #>>> Space complexity: O(1)
    remainingPackages = packageList.copy()
    hubLoad(trucks[0], remainingPackages, packageList, 0)
    hubLoad(trucks[1], remainingPackages, packageList, 0)
    setPath(trucks[0], locationList)
    setPath(trucks[1], locationList)

    # Time is managed in a for loop. The endTime is specified by the user. Each integer of time is equal to one minute.
    # If a truck travels 18MPH consistantly with no change in speed, then 18MPH / 60 minutes = .3 miles per minute.
    #>>> Time complexity: O(N^3) - N number of trucks are checked, setPath has N^2 complexity.
    #>>> Space complexity: O(N)
    for time in range(endTime):
        miles = time * .3

        for deliveryTruck in trucks:
            # Each truck is check to see if it has packages loaded on it. If it does, it checks to see if the total
            # mileage of the truck >= to the total miles determined by time in line 32. If the truck has driven the
            # specified amount of miles, then the package is set to delivered status and removed from truck. Then the
            # truck has it's next delivery path decided.
            # Note that packageList is updated. packageList is returned at the end of the simulation to report the status
            # of each package. remainingPackages is used only to determine if there are packages left at the hub.
            # >>> Time complexity: O(N^2) - setPath has complexity O(N^2)
            # >>> Space complexity: O(1)
            if len(deliveryTruck.packages) != 0:
                if miles >= deliveryTruck.mileage:
                    packageList[deliveryTruck.currentDelivery.packageID - 1].deliveryStatus = 'Delivered at: ' + convertTime(time)
                    deliveryTruck.deliver()
                    setPath(deliveryTruck, locationList)

            # If the truck doesn't have any packages on board, it checks to see if there are any packages back at the hub.
            # If there are, then it's path has already been determined back to the hub. If both the truck is at the hub
            # and the hub still has packages left, the truck is loaded and the path is set.
            # If the both trucks are empty and there are no packages remaining at the hub, it ends simulation and
            # returns the results of each package in packageList.
            # >>> Time complexity: O(N^2) - setPath has complexity O(N^2)
            # >>> Space complexity: O(N)
            else:
                if deliveryTruck.destinationID == 0 and len(remainingPackages) != 0 and miles >= deliveryTruck.mileage:
                    hubLoad(deliveryTruck, remainingPackages, packageList, time)
                    setPath(deliveryTruck, locationList)
                elif len(trucks[0].packages) == 0 and len(trucks[1].packages) == 0 and len(remainingPackages) == 0:
                    return packageList

    # If the endTime is reached, then the simulation for loop ends and the packageList results is returned.
    return packageList


# Converts time from minutes total to user readable time. Time is the amount of minutes since 8AM.
    #>>> Time complexity: O(1)
    #>>> Space complexity: O(1)
def convertTime(time):
    hour = str(int(time/60) + 8)
    minute = str(int(time%60))
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    return hour + ":" + minute