"""
a=eval(input("Enter a's value - "))
b=eval(input("Enter b's value - "))
sum = a+b
print(f'The sum of {a} & {b} is {sum} and {type(sum)}')
"""

"""
Enter a's value - "hinjewadi"
Enter b's value - \"It park Pune"
The sum of hinjewadi & It park Pune is hinjewadiIt park Pune and <class 'str'>
"""

#Note - Kindly use evaluate function, eval so that we can take any value as input, if we take int then we bind to only take int to perform the sum or operation so by using eval function any kind of input can be taken and if we are taking string then use "" for correct syntax while eval function

"""
Enter a's value - 5.7
Enter b's value - 15
The sum of 5.7 & 15 is 20.7 and <class 'float'>
"""
#------------------------------------------------------------------------------------------------------------------------------------
import Learn_Python
print(Learn_Python.my_target)#Learn abour rest api
# On updating it will also update in this file
print(Learn_Python.my_target)#Get to Placed soon on the package of 12 LPAn Automation Anyewhere

import Trying
print(Trying.doing)#importing modules

import platform
print(platform.system())#Windows - it is a pre defined module(Platform) uses to check the OS of system

import datetime
print(datetime.datetime.today())#2024-10-04 14:35:02.118364 - there is pre defined module(datetime) uses for getting the current date and time

# there is a module for timing in which we can work at remote servers. It is not a Predefined or prenuilt module, it is a third-party module names as "Paramiko". You need to install this module using commad - pip install paramiko

import time
time.sleep(1)# it is a time module. time.sleep() inlcludes seconds after the compiler run again - here it is of 1 seconds.

#pip --help : - command for getting all help related ti install, delete or anything with pip in cmd.

#------------------------------------------------------------------------------------------------------------------------------------

my_name = 'Shubham Mahajan'
my_target = "To be Palced in Automation Anywhere"
my_achievement = """Finally, got 12 LPA Package, Thank you Universe """

print(f"my name is : {my_name} \nAlong with this my current target is : {my_target} \nnot only this i've done my achievemnt : {my_achievement}")
#Along with this my current target is : To be Palced in Automation Anywhere not only this i've done my achievemnt : Finally, got 12 LPA Package, Thank you Universe

"""
my_details = "I am Shubam Mahajan and
            I have a package of 12 LPA"
"""            
# at this time it is showuing error - so for continue statement as line wise in a paragtaph format then use """ (triple String format)

my_details = """I am Shubam Mahajan and
            I have a package of 12 LPA
            and i am really enjoting my corporate life"""
print(my_details) # when we want to print multiple lines of information the use tripple codes (""")
""" o/p - 
I am Shubam Mahajan and
            I have a package of 12 LPA
            and i am really enjoting my corporate life
"""

'Space is count as one character in python'
my_str = ''
my_new_str = ' '
print(f'{bool(my_str)}')#False - no space is count as 0 which is showuinf False through boolean
print(f'{bool(my_new_str)}')#True - Space is count as 1 character which is showing True

#* how to access elements fron string using index values (slicing of a string)-
my_current_target = "Automation Anywhere's 12 LPA Package"
print(my_current_target)#Automation Anywhere's 12 LPA Package
print(f'{my_current_target}')#Automation Anywhere's 12 LPA Package
print(my_current_target[0])#A - when I want to acess the very first character
print(my_current_target[-1])#e - For at last character
print(my_current_target[0:])#Automation Anywhere's 12 LPA Package - Printing from 0(begin) to last
print(my_current_target[0:25])#Automation Anywhere's 12
print(my_current_target[:37])#Automation Anywhere's 12 LPA Package - from by default begin to desired range

#* How to change or delete a string

my_current_target = "Placement Success Celeebration"
print(my_current_target)#Placement Success Celeebration

my_str_len = len(my_current_target)
print(my_str_len)#30 - simply by using inbuilt len() function
print(f'lenght of above string names as my_current_taarget is calculated as : {my_str_len}')#lenght of above string names as my_current_taarget is calculated as : 30
# So the length of string is 30 and for     POSITIVE INDEXING it will be 0:29, NEGATIVE INDEXING - -1:-30

'Simple String Concatenation operation'
my_str1 = "Automation"
my_str2 = "Anywhere"
"""my_str = " "
my_str3 = my_str1+my_str+my_str2
"""
my_str3 = my_str1+" "+my_str2
print(my_str3)#Automation Anywhere
#------------------------------------------------------------------------------------------------------------------------------------
my_string = "Automation Anywehere Shubham Mahajan"
print(my_string)#Automation Anywehere Shubham Mahajan

my_string_lower = my_string.lower()
print(my_string_lower)#automation anywehere shubham mahajan

my_string_upper = my_string.upper()
print(my_string_upper)#AUTOMATION ANYWEHERE SHUBHAM MAHAJAN

my_string_swapoperation = my_string.swapcase()
print(my_string_swapoperation)#aUTOMATION aNYWEHERE sHUBHAM mAHAJAN

new_string = "i got placed on 12 lPA buddy"
print(new_string.title())#I Got Placed On 12 Lpa Buddy

#To know all such Case Conversion Operation - in cmd,
"""
x = "String"
print(dir(string))
"""
#------------------------------------------------------------------------------------------------------------------------------------
"""
given_str = input("Enter the desired String\n")
print(given_str)# by using it .. it prints the string usually at LHS.

print(given_str.center(120))# by using it .. it print the string at distance of 120 from left and in the center

print(given_str.ljust(110))# by using it .. it print the string at distance of 110 from left
print(given_str.rjust(110))# by using it .. it print the string at distance of 110 from right

#Using OS commads for width Automatically. Please use Window Powershell to perform the operations

import os

t_w = os.get_terminal_size().columns

given_str = input("Enter the desired String\n")
print(given_str)# by using it .. it prints the string usually at LHS.

print(given_str.center(t_w).title())# by using it .. it print the string at distance as per the OS Columns and Rows from left and in the center in a title formaat

print(given_str.ljust(t_w).title())# by using it .. it print the string at distance from OS Columns and Rows from left in a title formaat
print(given_str.rjust(t_w).title())# by using it .. it print the string at distance from OS Columns and Rows from right in a title formaat
"""
#------------------------------------------------------------------------------------------------------------------------------------



