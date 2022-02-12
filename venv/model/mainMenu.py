# Brandon Blackburn, StudentID #001015925
# mainMenu.py
#
# User interface to simulate the packages being delivered until a certain time.
# Will print packages and locations as well.

from Algorithms.run import run
from Objects.package import *
from Objects.truck import  *

# >>> Time complexity: O(1)
# >>> Space complexity: O(1)
def mainMenu(locationList, packageHash):

    # Trucks created here so that they don't need returned through a whole new function.
    truck1 = truck(1)
    truck2 = truck(2)
    trucks = [truck1, truck2]
    choice = 0

    print("###########################################")
    print("1) Print Packages")
    print("2) Print Locations")
    print("3) Run simulation until done")
    print("4) Run simulation until a time")
    print("5) Exit")
    print("###########################################\n")


    while(choice < 1 or choice > 5):
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 5:
            print("Invalid selection")


    # Selects each bucket from packageHash
    # The hash table has 4 packages per bucket
    # Prints each package per bucket.
    # >>> Time complexity: O(N^2)
    # >>> Space complexity: O(1)
    if choice == 1:
        for bucket in packageHash:
            for item in bucket:
                print(package(item[1]))


    #Prints each location.
    # >>> Time complexity: O(N)
    # >>> Space complexity: O(1)
    if choice == 2:
        for location in locationList:
            print(location)


    # Runs the whole simulation until there are no more packages to be delivered.
    # The max miles driven is 145. If trucks drive 18 MPH, the max time is 483.3 minutes
    # # >>> Time complexity: O(N^)  TODO
    # # >>> Space complexity: O(N).
    if choice == 3:
        results = run(locationList, packageHash, 483, trucks)
        printResults(results, trucks, locationList, 483)

    # Basic input syntax, prints about invalid input.
    # TODO
    while choice == 4:
        time = input("Until what time? (23:59): ")
        if time == 'quit':
            mainMenu(locationList, packageHash)
        elif len(time) != 5:
            print("Invalid input. Please use HH:MM (24-hour) format")
        elif time[2] != ':':
            print("Invalid input. Please use HH:MM (24-hour) format")
        elif int(time[0:2]) < 8 or int(time[0:2]) > 23:
            print("Invalid hour")
        elif int(time[3:-1]) < 0 or int(time[3:]) > 59:
            print("Invalid minute")
        else:
            # Converts the entered time specificed to minutes
            # Runs simulation with equalvient minutes.
            runTime = 0
            runTime += (int(time[0:2]) - 8) * 60
            runTime += int(time[3:])
            results = run(locationList, packageHash, runTime, trucks)
            printResults(results, trucks, locationList, runTime)
            choice = 0
    exit(1)



# Prints results of simulation. Since the trucks are passed in,
# the information is easily gathered.
# Since the trucks move at a constant 18 MPH, their mileage
# can be used to convert into minutes past.
# >>> Time complexity: O(N)
# >>> Space complexity: O(1)
def printResults(results, trucks, locationList, time):
    totalMiles = 0
    for truck in trucks:
        miles = round(truck.mileage, 1)
        totalMiles += round(miles, 1)

        # Set up time format for truck deliveries.
        endHour = (truck.mileage / 18) * 60
        endMinute = str(int((endHour) % 60))
        endHour = str(int(endHour / 60) +8)
        if len(endHour) == 1:
            endHour = '0' + endHour
        if len(endMinute) == 1:
            endMinute = '0' + endMinute

        # Current location
        # Next Delivery
        cl = locationList[truck.currentLocationID].address
        nd = str(truck.currentDelivery)


        # If the truck hasn't delivered it's next package yet,
        # it will be displayed as 'Next Delivery" instead.
        print("\nTruck #" + str(truck.truckID))
        print("Miles driven: " + str(miles))
        print("Current Location: " + cl)
        if time >= (truck.mileage /18) * 60:
            print("Last Delivery: " + endHour + ':' + endMinute)
        else:
            print("Next Delivery --  " + nd)


    # Lists all packages and their delivery status.
    # >>> Time complexity: O(N)
    # >>> Space complexity: O(1)
    print("\n\n****************************\n       Package List")
    for package in results:
         print(str(package))
    print("***************************\n")


    # Prints a summary of the simulation, proving that packages are delivered on time
    # and that the total mileage does not exceed 145.
    # >>> Time complexity: O(1)
    # >>> Space complexity: O(1)
    print("\n\nTotal miles driven: " + str(totalMiles))
    currentHour = str(int(time/60) + 8)
    currentMinute = str(int(time % 60))
    if len(currentHour) == 1:
        currentHour = '0' + currentHour
    if len(currentMinute) == 1:
        currentMinute = '0' + currentMinute
    print("CurrentTime: " + str(currentHour) + ":" + str(currentMinute))
