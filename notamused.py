# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
import sys
DAILY_RATE = .1
day = 0
currentDay = None
first = True
class Customer:
    def __init__(self, name):
        self.name = name
        self.status = "o"  #  i, in / o, out
        self.entered = 0
        self.admission = []

    def closeout(self, exit_time):
        self.admission.append((self.entered, exit_time))
        self.status = 'o'

class BusinessDay:
    def __init__(self, number):
        self.number = number
        self.customers = {}

    def billing(self, daynumber):
        global first
        if not first:
            print()
        print("Day {}".format(daynumber))
        for key, customer in sorted(self.customers.items()):
            total_price = 0
            first = False
            for (entry, exit) in customer.admission:
                total_price += (int(exit) - int(entry)) * DAILY_RATE
            print("{} ${:.2f}".format(customer.name, total_price))


log = sys.stdin.readlines()
#log = open("in.txt", "r").readlines()
for line in log:
    line = line.split()
    if line[0] == "OPEN":
        day += 1
        currentDay = BusinessDay(day)
    elif line[0] == "ENTER":
        name = line[1]
        entered = line[2]
        if name in currentDay.customers.keys():
            cust = currentDay.customers.get(name)
        else:
            cust = Customer(name)
        cust.entered = entered
        cust.status = 'i'
        currentDay.customers[name] = cust
    elif line[0] == "EXIT":
        name = line[1]
        exit = line[2]
        currentDay.customers.get(name).closeout(exit)
    elif line[0] == "CLOSE":
        currentDay.billing(currentDay.number)