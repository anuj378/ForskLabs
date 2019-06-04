
"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
    
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

"""



#SOLUTION 1
'''
items= [[34587, 'Learning Python', 'Mark Lutz' , 4, 40.95],
    [98762, 'Programming Python', 'Mark Lutz', 5, 56.80],
    [77226, 'Head First Python', 'Paul Barry', 3, 32.95],
    [88112, 'Einführung in Python3', 'Bernd Klein' , 3 ,24.99]]

OrderSummary=[]
for item in items:
    product=item[-1]*item[-2];
    if product<100:
        product+=10
    OrderSummary.append((item[0],product))
print(OrderSummary)
'''

items= [[34587, 'Learning Python', 'Mark Lutz' , 4, 40.95],
    [98762, 'Programming Python', 'Mark Lutz', 5, 56.80],
    [77226, 'Head First Python', 'Paul Barry', 3, 32.95],
    [88112, 'Einführung in Python3', 'Bernd Klein' , 3 ,24.99]]

OrderSummary=list(map(lambda x:(x[0],x[-1]*x[-2]),list(filter(lambda x:(x[-1]*x[-2])>=100,items))))
temp=list(map(lambda x:(x[0],x[-1]*x[-2]+10),list(filter(lambda x:(x[-1]*x[-2])<100,items))))
for x in temp:
    OrderSummary.append(x)
print(OrderSummary)





