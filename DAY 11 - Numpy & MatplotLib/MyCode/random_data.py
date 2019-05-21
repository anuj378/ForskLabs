# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:59:06 2019

@author: King23
"""


"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""

import numpy as np 
#random.random(shape) – creates arrays with random floats over the interval [0,1].
array_numpy = np.random.randint(5,15,40)

def findMode(values):
    from collections import Counter
    count=Counter(values)

    for x in count:
        if count[x]==max(count.values()):
            mode=x
    return(mode)
print("Without Numpy =",findMode(array_numpy))