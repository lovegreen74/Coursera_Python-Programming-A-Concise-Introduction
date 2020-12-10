# -StartPython.py *- coding: utf-8 -*-
"""
Spyder Editor

#%% starts a new cell. Use second green triangle to run just the cell that
your mouse has last clicked in (or Ctrl-Enter on a PC or Command-Return on a
Macintosh or Menu>Run>Run Cell)
"""
#%%
def hello():
    print("Hello, world!")


#%%
def myname():
    print("My name is Bill")
#%%
#%%
def ourschool():
    print("Coursera is our school")

#%%  
  
""" This will run forever. In this case Ctrl-C will stop it, but sometimes
that doesn't work. In that case, click away IP Console to stop; click yes to 
kill kernel. Open a new IPConsole on the Console menu to restart """
#%%
def forever():
    while True:
        pass
  
#%% 
def celsius_to_fahrenheit(temp):
    """ Converts Celsius temperature to Fahrenheit.
        Formula is 9/5 temp plus 32 """
    newtemp = (9/5)*temp+32
    print("The Celsius temperature",temp,"is equivalent to", newtemp, end='')
    print("degrees Fahrenheit")
#%%
def name():
    """ Input first and last, combine to one string and print
        Also, input the city and state and print. """ 
    fname = input("Enter your first name: ")
    lname = input ("Enter your last name: ")
    fullname = fname + " " + lname
    city = input ("Enter our city you live in: ")
    country = input ("Enter your country you live in: ")
    address = city + "," + country
    
    print('Your name is:',fullname, )
    print ('Your live in:', address)
#%%
def absolutevalue(type_):
    if type_ >=0:
        print(" The absolute value of ", type_, "is",type_)
    else:
        newtype = type_*-1
        print("The absolute value of", type_, "is ",newtype )
#%% 
def absolutevalue(num):
    if num >= 0:
        abs_num = num
    else:
        abs_num= -num
    print('The absolute value of',num,"is",abs_num)
#%%
def absolutevalue(type_):
    if type_ >=0:
        print(" The absolute value of ", type_, "is",type_)
    else:
        newtype = -type_
        print("The absolute value of", type_, "is ",newtype )
#%%
def inches_to_feet1(inches):
    feet=inches//12
    extra_inches=inches%12
    print(inches,'inches is ',feet,'feet ',extra_inches,'inches')
#%%
def count_down():
    ct=10
    while ct>=1:
        print(ct,end=" ")
        ct=ct-1
    print()
    print("BASTOFF!")
#%%
def cheer():
    for ct in range(10,0,-1):
        print(ct,end=" ")
    print()
    print("BLASTOFF!")
        
    
    