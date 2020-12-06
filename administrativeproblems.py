# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
import math
PENALTY = -10 ** 17

class Car:
    def __init__(self, car_name, catalog_price, pickup_cost, cost_per_km):
        self.name = car_name
        self.catalogPrice = catalog_price
        self.pickupCost = pickup_cost
        self.costPerKm = cost_per_km


class Spy:
    def __init__(self, spy_name):
        self.name = spy_name
        self.bill = 0
        self.vehicle = None
        self.status = "r"

    def getBill(self):
        if self.bill >= 0:  # No inconsistencies were found
            return str(int(self.bill))  # Print actual bill
        else:  # Inconsistencies were found
            return "INCONSISTENT"  # Print Inconsistent

    def pickupCar(self, vehicle: Car):
        if self.status == 'r':  # Last transaction spy had was returning a vehicle or initial spy value
            self.bill += vehicle.pickupCost  # add pick up cost to bill
            self.vehicle = vehicle  # put vehicle into spy's inventory
            self.status = 'p'  # set spy status to picked up
        else:
            self.bill = PENALTY  # Spy's status was 'a' or 'p' therefore ineligible to pick up car, set bill negative

    def returnCar(self, kilometers: int):
        if self.status == 'a' or self.status == 'p':   # last transaction was accident or pickup
            self.bill += self.vehicle.costPerKm * kilometers  # add Kilometers * cost per Kilometer to Bill
            self.vehicle = None  # remove vehicle from inventory
            self.status = 'r'  # set spy's status to return
        else:
            self.bill = PENALTY  # Spy's status was 'r' therefore ineligible to return a car

    def accident(self, severity: int):
        if self.status == 'p' or self.status == 'a':  # last transaction was pickup or accident
            self.bill += math.ceil(self.vehicle.catalogPrice * severity / 100.0)  #round up catalog price * percentage of damage
            self.status = 'a'  # set status to accident
        else:
            self.bill = PENALTY  # Spy's status was 'r' therefore ineligible to have an accident


class AdminSystem:
    def __init__(self):
        self.__spyInventory = {}  # Initialize Spy Inventory
        self.__carInventory = {}  # Initialize Car Inventory

    def printStatement(self):
        for key, spy in sorted(self.__spyInventory.items()):  # Sort the Spy Inventory Alphabetically
            print("{} {}".format(spy.name, spy.getBill()))  # Print the Spy Name and Spy Bill

    def addCar(self, car_name, catalog_price, pickup_cost, cost_per_km):
        self.__carInventory[car_name] = Car(car_name, catalog_price, pickup_cost, cost_per_km)

    def getCar(self, car_name):
        return self.__carInventory.get(car_name)

    def addSpy(self, spy_name):
        self.__spyInventory[spy_name] = Spy(spy_name)

    def getSpyList(self):
        return self.__spyInventory

    def getSpy(self, spy_name):
        return self.__spyInventory.get(spy_name)

    def processing(self):
        for key, spy in self.__spyInventory.items():
            if spy.status == 'p' or spy.status == 'a':  # Events are over, if Spy has a car out bill is inconsistent
                spy.bill = PENALTY  # Set bill Negative


n = int(input())
for _ in range(n):  # Loop Through Test Cases
    admin = AdminSystem()  # Initialize AdminSystem
    totalCars, totalEvents = map(int, input().split())
    for _ in range(totalCars):  # Car Loading Loop
        name, cp, puc, cpkm = input().split()
        cp, puc, cpkm = int(cp), int(puc), int(cpkm)  # Change Price, Pickup Cost and Cost Per KM to Integers
        admin.addCar(name, cp, puc, cpkm)  # Add the car to the AdminSystem Inventory
    for _ in range(totalEvents):  # Event Loop
        time, spyName, transaction, quantifier = input().split()
        if spyName not in admin.getSpyList().keys():  # If the Spy name isn't already in the inventory
            admin.addSpy(spyName)   # Add the spy
        currentSpy = admin.getSpy(spyName)  # Spy on the current Event
        if transaction == 'p':
            currentSpy.pickupCar(admin.getCar(quantifier))  # Spy picked up a car
        if transaction == 'a':
            currentSpy.accident(int(quantifier))  # Spy had an accident
        if transaction == 'r':
            currentSpy.returnCar(int(quantifier))  # Spy returned the Car
    admin.processing()  # Events are over, Check for inconsistencies
    admin.printStatement()  # Print Statements
