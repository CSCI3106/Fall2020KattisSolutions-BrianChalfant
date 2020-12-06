# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
import math
def isPrime(n):

    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False

    return True
n = int(input())
while n!= 0:
    n_is_prime = isPrime(n)
    nextprime = 0
    for i in range(n*2,n*3):
        if isPrime(i):
            nextprime = i
            break
    if n_is_prime:
        print(nextprime)
    else:
        print("{} ({} is not prime)".format(nextprime, n))
    n = int(input())
