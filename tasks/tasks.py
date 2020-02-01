# 01/02/2020

## 1 ##
# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done
# before, or after the addition.
#
# The binary number returned should be a string.
def add_binary(a,b):
    return bin(a + b)[2:]


## 2 ##
# Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of
# n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
#
# You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to
# build?
#
# The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return the
# integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.
def find_nb(m):
    sum, counter = 0, 1
    while True:
        sum += counter ** 3
        if   sum <  m: counter += 1; continue
        elif sum == m: return counter
        elif sum >  m: return -1


## 3 ##
# Number of people in the bus
#
# There is a bus moving in the city, and it takes and drop some people in each bus stop.
#
# You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which
# represent number of people get into bus (The first item) and number of people get off the bus (The second item)
# in a bus stop.
#
# Your task is to return number of people who are still in the bus after the last bus station (after the last array).
# Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably
# sleeping there :D
#
# Take a look on the test cases.
#
# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return
# integer can't be negative.
#
# The second value in the first integer array is 0, since the bus is empty in the first bus stop.
def number(bus_stops):
    return sum([stop[0] for stop in bus_stops]) - sum([stop[1] for stop in bus_stops])
