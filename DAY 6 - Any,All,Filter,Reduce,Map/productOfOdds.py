"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""

from functools import reduce
numbers=[10,2,30,4,50,6,5,3]
#numbers=[12,45,65,84,78,15,64,16,49,889,98,75]
product=reduce(lambda x,y: x*y,[i if i%2==1 else 1 for i in numbers])
print(product)