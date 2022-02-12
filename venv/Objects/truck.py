# Objects.truck.py
#
# A truck object that hold packages. The truckID, currentLocationID, and mileage are the accurate info at init.
# self.packages will be a list of packages, loaded on at the hub.
# self.currentDelivery(package) and self.destiniationID(int) are updated after each delivery is made.
# self.path is the current path they are taking to get to their destination.
# self.mileage is how far they drove. It is updated after the driver decides his path to the destination.
# >>> Time complexity: O(1)
# >>> Space complexity: O(1)

class truck:
    def __init__(self, truckID):
        self.truckID = truckID
        self.packages = []
        self.currentDelivery = 0
        self.destinationID = 0
        self.currentLocationID = 0
        self.path = []
        self.mileage = 0


    # Delivers package, removes it from the trucks list of packages.
    # >>> Time complexity: O(1)
    # >>> Space complexity: O(1)
    def deliver(self):
        if self.currentDelivery != 0:
            self.currentLocationID = self.currentDelivery.locationID
            self.packages.remove(self.currentDelivery)
        self.currentDelivery = 0

    def load(self, package):
        self.packages.append(package)

    def updateDestination(self, location):
        self.destinationID = location

