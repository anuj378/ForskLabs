# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:21:58 2019

@author: King23
"""


# Code Challenge 

# Find the mean, median, mode, and range for the following list of values:
# 13, 18, 13, 14, 13, 16, 14, 21, 13


#Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8

values=[13, 18, 13, 14, 13, 16, 14, 21, 13]
values.sort()


mean=(sum(values)/len(values))
print("Mean =",mean)



def findMedian(values):
    if(len(values)%2==0):
        median=( (values[int(len(values)/2)]) +(values[int((len(values)/2))+1] ) )/2
    else:
        median=(values[int(len(values)/2)])
    return median
print("Median ={}".format(findMedian(values)))



def findMode(values):
    from collections import Counter
    count=Counter(values)

    for x in count:
        if count[x]==max(count.values()):
            mode=x
    return(mode)
print("Mode ={}".format(findMode(values)))

range=max(values)-min(values)
print("Range =",range)

     
        

        

  


