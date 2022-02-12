# Algorithms.hub.py
#
# This algorithm is the loading process at the Hub. It loads the packages with notes first (if approriate),
# and then loads packages based on their deadlines. Finally, it  pops the remainingPackages (from the end) with
# no order in particular.

from Objects.package import *
from Objects.truck import *

# Package IDs with notes, grouped into lists of the same kind.
truck2Packages = [2, 11, 36, 38]
deliverTogether = [13, 15, 19]
after9_05 = [6, 25, 28, 32]
maxLoad = 16

# Agruments take in one truck, the remainingPackages for what packages still need delivered, packageList so the
# package delivery status can be updated, and time for packages that cannot be loaded until a certain time.
# >>> Time complexity: O(N)
# >>> Space complexity: O(N) because of a priority list.
def hubLoad(truck, remainingPackages, packageList, time):
    priority = []

    # Checks to see if any packages have been removed yet. If it's full, then it takes out the packages that are in
    # any one of the note lists. They are removed from remainingPackages, but are not updated and still say "At Hub" until
    # one of the trucks loads them up.
    # >>> Time complexity: O(N)
    # >>> Space complexity: O(1)
    if len(remainingPackages) == len(packageList):
        for id in truck2Packages:
            remainingPackages.remove(packageList[id - 1])
        for id in deliverTogether:
            remainingPackages.remove(packageList[id - 1])
        for id in after9_05:
            remainingPackages.remove(packageList[id - 1])

    # If there are remainingPackages and a truck has less than 12 packages, then load a package onto the truck.
    # I chose 12, because it helps optimize how quickly the trucks deliver all of their packages
    #>>> Time complexity: O(N)
    #>>> Space complexity: O(N)
    while(len(truck.packages) < 12 and len(remainingPackages) > 0):

        # Note list packages are loaded if truck loaded is truck 2.
        if len(truck2Packages) > 0 and truck.truckID == 2:
            packageList[truck2Packages[-1] - 1].deliveryStatus = 'In route'
            truck.load(packageList[truck2Packages.pop() - 1])

        # List for packages that need delivered all together are now loaded if the truck has room.
        elif len(deliverTogether) > 0 and maxLoad - len(truck.packages) > len(deliverTogether):
            packageList[deliverTogether[-1] - 1].deliveryStatus = 'In route'
            truck.load(packageList[deliverTogether.pop() - 1])

        # List for packages that arrive after 9:05 (65 minutes after start) are now loaded
        elif len(after9_05) > 0 and time > 65:
            packageList[after9_05[-1] - 1].deliveryStatus = 'In route'
            truck.load(packageList[after9_05.pop() - 1])

        # If the note lists are empty or cannot be loaded onto the truck, prioritize packages that have deadlines.
        # Deadline packages are placed into a priority list. If there are no deadline items, it loads from the rest of the packages.
        # >>> Time complexity: O(N)
        # >>> Space complexity: O(N)
        else:
            priority.clear()
            for package in remainingPackages:
                if package.deadline != 'EOD':
                    priority.append(package)
            if len(priority) != 0:
                pick = priority[0]
                for package in priority:
                    if package.convertTime() < pick.convertTime():
                        pick = package
                truck.load(pick)
                priority.remove(pick)
                remainingPackages.remove(pick)
            else:
                packageList[remainingPackages[-1].packageID - 1].deliveryStatus = 'In route'
                truck.load(remainingPackages.pop())
