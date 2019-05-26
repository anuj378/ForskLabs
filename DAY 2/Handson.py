"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 
numbers=list(range(1,21))
numbers[0::2]
numbers[1::2]

"""
Hands On 2
"""
# Make a function to find whether a year is a leap year or no, return True or False 
def leapyear(x):
    
    
    
"""
Hands On 3
"""
# Make a function days_in_month to return the number of days in a specific month of a year
months={
        'Jan':31,
        'Feb':28,
        'Mar':31,
        'Apr':30,
        'May':31,
        'Jun':30,
        'Jul':31,
        'Aug':31,
        'Sep':30,
        'Oct':31,
        'Nov':30,
        'Dec':31
        }

def daysInMonth(x):
    print("Days in {} ={}".format(x,months[x]))
    
daysInMonth('May')
    


