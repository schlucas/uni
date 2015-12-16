# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:14:52 2015

@author: lucas
"""

import random
import time


def bubblesort(array, lenght):
    #counter = 0    
    sortFinish = False
    while(not sortFinish):
        sortFinish = True
        for i in range(0, lenght-1):
            if(array[i] > array[i+1]):
                helper = array[i]
                array[i] = array[i+1]
                array[i+1] = helper
                sortFinish = False
        #counter = counter + 1
                
    return array
    
def shakersort(array, length):
    sortFinish = False
    while(not sortFinish):
        sortFinish = True
        for i in range(0, length-1):    #aufsteigend sortieren
            if(array[i] > array[i+1]):
                helper = array[i]
                array[i] = array[i+1]
                array[i+1] = helper
                sortFinish = False
        for i in range(length-1, 0, -1):    #absteigend sortieren
            if(array[i] < array[i-1]):
                helper = array[i]
                array[i] = array[i-1]
                array[i-1] = helper
                sortFinish = False
                
    return array


#Main:

numbers = 10000
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


#bubblesort
bubbleStart = time.clock()

bubbledArray = bubblesort(arr, arrLength)

bubbleStop = time.clock()
bubbleTime_sec = bubbleStop - bubbleStart
bubbleTime_us = round(bubbleTime_sec * 1000 * 1000)
bubbleString = "Bubblesort\tDauer: "+repr(bubbleTime_us)+"us"
print bubbleString
#for i in range(arrLength):
#    print(bubbledArray[i])
 
   
#shakersort
shakeStart = time.clock()

shakedArray = shakersort(arr, arrLength)

shakeStop = time.clock()
shakeTime_sec = shakeStop - shakeStart
shakeTime_us = round(shakeTime_sec * 1000 * 1000)
shakeString = "Shakersort\tDauer: "+repr(shakeTime_us)+"us"
print shakeString
#for i in range(arrLength):
#    print(shakedArray[i])


"""
results:

Arraylength: 100
Bubblesort	Dauer: 1449.0us
Shakersort	Dauer: 23.0us
Arraylength: 100
Bubblesort	Dauer: 1422.0us
Shakersort	Dauer: 27.0us
Arraylength: 100
Bubblesort	Dauer: 1512.0us
Shakersort	Dauer: 22.0us

Arraylength: 1000
Bubblesort	Dauer: 162283.0us
Shakersort	Dauer: 208.0us
Arraylength: 1000
Bubblesort	Dauer: 198434.0us
Shakersort	Dauer: 198.0us
Arraylength: 1000
Bubblesort	Dauer: 167177.0us
Shakersort	Dauer: 198.0us


"""               