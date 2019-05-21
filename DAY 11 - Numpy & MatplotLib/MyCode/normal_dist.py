# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:50:22 2019

@author: King23
"""

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""
import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(150.0,20.0,10000)


plt.hist(data, bins=100)
print("Variance ={} SD ={}".format( np.var(data)   ,  np.std(data)  ))


