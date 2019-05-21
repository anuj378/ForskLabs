# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:48:14 2019

@author: King23
"""

"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""
import numpy as np
numbers=input()
numbers=numbers.split(' ')
numbers_ndarray=np.array(numbers)
numbers_ndarray=numbers_ndarray.reshape(3,3)
print(numbers_ndarray)