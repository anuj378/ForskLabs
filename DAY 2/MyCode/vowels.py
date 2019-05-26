"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels=['a','A','e','E','i','I','o','O','u','U']

for name in state_name:
    for letter in name:
        if letter in vowels:
            
