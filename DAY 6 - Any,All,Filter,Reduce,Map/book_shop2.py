"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
   Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
      
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
"""
items=[[1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)],
        [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],[3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
        [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)]]

'''final=[]
i=0
for x  in items:
    sum=0
    final.append([x[0]])
    for y in x:
        if type(y)==tuple:
            sum+=y[-1]*y[-2]
    final[i].append(sum)
    i+=1
print(final)
1

#4*9.99 +18*12.99 + 9* 44.95
'''
from functools import reduce
i=0
final=[]
for x in items:
    final.append([x[0]])
    total=reduce(lambda x,y:x+y,map(lambda q:q[-1]*q[-2],filter(lambda t:type(t)==tuple,x )))
    final[i].append(total)
    i=i+1
print(final)
    
