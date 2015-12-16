# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:12:07 2015

@author: lucas
"""

import random
import time

def swapsort(array, length):
    index = 0
    while(index < length-1):
        count = 0
        for j in range(length):
            if(array[i] < array[j]):
                count = count+1
        helper = array[count]
        array[count] = array[i]
        array[i] = helper
        index = index+1
    
    return array
    
def swap_sort(array, length):
    index = 0
    while index < length-1:
        new_index = sum(x < array[index] for x in array)
        if index == new_index:
            index += 1
        else:
            array[index], array[new_index] = array[new_index], array[index]

    return array


#Main:

numbers = 20
print("") #newline


# Zufallszahlen für Array
arr = []
arr.append(0)
for i in range(1, numbers):
    x = random.randint(0, 100)
    arr.append(x)
    #print(arr[i])
print ""

arrLength = len(arr)
string0 = "Arraylength: " + repr(arrLength)
print(string0)


#swapsort
swappedArray = swap_sort(arr, arrLength)
for i in range(arrLength):
    print(swappedArray[i])
