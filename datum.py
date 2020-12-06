# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
from datetime import date
d, m = map(int, input().split())
today = date(2009, m, d)
day_of_week = int(today.weekday())
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(weekdays[day_of_week])