# File: testing.py
# Author: Nicholas Louie (nlouie@bu.edu), Jennifer Tsui (jgtsui@bu.edu), Benjamin Owens (bsowens@bu.edu)
# Date: 3/31/16
# Boston University Computer Science Spring 2016
# CS330 Assignment 5 Question 4 (c)
# Description: This tests the Karmarkar-Karp implementation and the pseudopolynomial implementation



import pseudo
import kk
import random
import time
import math

#Generates a list of random integers in the range [1,r] of length n
def randList(r, n):
    return [random.randint(1,r) for i in range(n)]

def testp():
    # Parameter here is 10^x
    for x in range(3,13):
        start = time.time()
        pseudo.partition(randList(math.pow(10,x),100))
        print("Partitioning list of range of 10^",x," successful")
        total_time = time.time() - start 
        print("    It took",total_time,"seconds")
        

def testkk():
    # Parameter here is 10^x
    for x in range(3,13):
        start = time.time()
        kk.karmarkar_karp(randList(math.pow(10,x),100))
        print("Residue of list of range of 10^",x," successful")
        total_time = time.time() - start 
        print("    It took",total_time,"seconds")


'''

The Karmarkar-Karp implementation takes the same amount of time as you increase the range of random
numbers. Each test takes ~ .12 seconds.

Our pseudo-polynomial implementation time increases by a factor for 10 when you increase the
range, i.e.:
10^3 = 1.2 seconds
10^4 = 12 seconds
10^5 = 120 seconds
10^6 = 1200 seconds
beyond this point it becomes unreasonable to test and we were not able to test it for
larger ranges

'''




