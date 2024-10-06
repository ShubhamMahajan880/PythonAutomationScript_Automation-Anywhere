#1 - Python Scripting for Automation

python --version
pip --version

import platform
platform.system()
platform.windows()

Python is called independent language because same code can be run everywhere.

Python Automation Commands on Command Line

Creating a Directory from cmd
mkdir NAMEOFFOLDER
cd NAMEOFFOLDER
dir
------------------------------------------------------------------------------------------------------------------------------------
- Basic Syntax of Python - Syntax and hoe to print
- Indentation in Python - for looing statements
- Comments in python - For single line use # and for multiple lines use """ to """
- Special Character in Python
Write Special Characters only inside the quotes --> ''," "
\n - new line
\b - your Curson is going one step beck and deleting
\b\b - your Curson is going two step beck and deleting
\t - tab - Spacing
\(back Slash) - Specia Symbol
\a - Alert Sound

Code -
print("Hellop Shubham how are you")
print("Shubham Mahajn got placed in Automation Anywhere")
print("Shubham is the only student who got highest placement among all 2025 batch students")
 

print("Print the condition to get the package :")

a=5;
b=10;
result = a+b

print("the adddition of {a} and {b} is ", result)

#Comments in Python Programming

"""Today is 28-09-2024 and i am learning Python programming language because my next target is
a company named as Automation Anywhere and I have to crack it anyhow.
"""
#print("we are going to work with special charaacters of Python")
#print("This is a very important topic in Python Programmming")

print("now i waant to print above two statements in a single line instead of two lines")
print("we are going to work with special charaacters of Python. \nThis is a very important topic in Python Programmming")


print("Hello Word")
print("Hello \bWord")
print("Hello \b\b Word")
print("Hello \tWord")#Hello 	Word
print('Automation Anywhere')#Automation Anywhere
#print('Automation's Anywhere')# Error 
print("Automation's Anywhere")# Automation's Anywhere
print("Automation Anywhere is in Bengalurua and Vadodara")# Automation Anywhere is in Bengalurua and Vadodara
print("Automation Anywhere is in \"Bengalurua\" and Vadodara") # Automation Anywhere is in "Bengalurua" and Vadodara

print("E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts")
------------------------------------------------------------------------------------------------------------------------------------

- For windows if wants to open a Python file using CMD
python NAMEOFSCRIPT

- Intoduction to Variables in Pythn
Becuase of this properties python is called as Dynamically type langauge
- Redifing a variable's value
- Rules to define a variable -
1. It contains letters,numbers and underscore
2. It should not be a keyword
3. Can't contain spaces
4. it should not start with a number
5. It is Case sensitive - you can use small and capital letter for different values

Code  -
x = 4
print(x) #4
print('x')#x
y = 3.1416
print(y,type(y))#3.1416 <class 'float'>
print(type(x))#<class 'int'>
"""Becuase of this properties python is called as Dynamically type langauge"""
x =45
print(x)#45
#del x
print(x)# 'x' is not defined
my_name = "Shubham"
print(my_name)#Shubham
t = 45
T = 60
print(t,T)#45 60

x=6
print(x)#6
print(id(x))#140718781096904
print(type(x))#<class 'int'>
id_x=id(x)
print(id_x)#140718781096904
#this was a wAY TO STORE id of a datatype in a id
------------------------------------------------------------------------------------------------------------------------------------

- Datatypes aand Variable datataypes in Python -
1 -wAY TO STORE id of a datatype in a id
basic Datatypes of Python are  -
1. Numbers(int,float and complex)
2. Strings
3. Boolean

Code -

s=4
m=5.6
v=8+4j
print(s,type(s))#4 <class 'int'>
print(m,type(m))#5.6 <class 'float'>
print(v,type(v))#(8+4j) <class 'complex'>

lan_name='Shubham Is Revising Python'
print(lan_name)#Shubham Is Revising Python

my_surname = "Mahajan"
print(my_surname, type(my_surname))#Mahajan <class 'str'>


check_value = True
print(check_value,type(check_value))#True <class 'bool'>

simillarly_value = False
print(simillarly_value,type(simillarly_value))#False <class 'bool'>

#again_check_value = true
#print(again_check_value,type(again_check_value))
"""
NameError: name 'true' is not defined. Did you mean: 'True'?
It is clearly indicate that the Word True is boolean but not the word true and same for False
"""

#again_simillarly_check = false
#print(again_simillarly_check,type(again_simillarly_check))
"""
NameError: name 'false' is not defined. Did you mean: 'False'?
"""

NameError: name 'true' is not defined. Did you mean: 'True'?
It is clearly indicate that the Word True is boolean but not the word true and same for False

NameError: name 'false' is not defined. Did you mean: 'False'?
------------------------------------------------------------------------------------------------------------------------------------

- Typecasting or Type Conversoin in Python  -

"""
Note: Any datatype can be converted into boolean
using - bool(any)_data_type)= True OR False
        bool(empty) = False
        bool(non-empty) = True
Examples -         
"""
Code -

x = 60
print(x,type(x))

y=str(x)#60 <class 'int'>
print(y,type(y))#60 <class 'str'>

z=bool(x)
print(z,type(z))#True <class 'bool'>

p=0
print(p,type(p))#0 <class 'int'>

q=bool(p)
print(q,type(q))#False <class 'bool'>

bool(0)#False

x=""
bool(x)# False

None
bool(None)#False

bool({})#False

bool(())#False

bool([])#False

"""
Any datatype can be converted into  a string but reverse is not always true
Example - 
"""

Code -

x="2.1.3.5.8"
print(x,type(x))#2.1.3.5.8 <class 'str'>

x="2.1.3.5.8"
print(x,type(x))#2.1.3.5.8 <class 'str'> # now here any number/datatype can be converted into string but any string cannot be converted into number or any datatype
# clearly  2.1.3.5.58 is  a string but a 2.103.5.8 is not a number

------------------------------------------------------------------------------------------------------------------------------------

- using Multiple Var(s) and String(s)

"""
p=8
r = 3.5
site_name = "XNXX.COM"
print(p)#8
print(r)#3.5
print(site_name)#XNXX.COM
"""
#instead of mentioning variable one after another, in python we caan mention all vatiables at a time and can be print

p=8;r = 3.5;site_name = "XNXX.COM"
print(p,r,site_name)#8 3.5 XNXX.COM

#another way -
print("{} {} {}".format(p,r,site_name))#8 3.5 XNXX.COM
        
#if required then use new line character
print("{} \n{} \n{}".format(p,r,site_name))
"""
8
3.5 
XNXX.COM
"""

# Order can also be change
print("{} {} {}".format(r,site_name,p))#3.5 XNXX.COM 8

#if i want to print as - this value is this -
print("value of p is - {},value of r is - {},name of site is - {}".format(p,r,site_name))
#value of p is - 8,value of r is - 3.5,name of site is - XNXX.COM

#anothere way in a single word for whole value
final_value = ("value of p is - {},value of r is - {},name of site is - {}".format(p,r,site_name))
print(final_value)
#value of p is - 8,value of r is - 3.5,name of site is - XNXX.COM


------------------------------------------------------------------------------------------------------------------------------------

- Input and Output Statements in Python -

Code -
#using Format Function for specifying inputs

a = 4
b = 8
result = a+b
print("The addition of {a} and {b} is : ", result)#The addition of {a} and {b} is :  12
print(f'the addition of {a} and {b} is: {result}')# the addition of 4 and 8 is: 12
print('the addition of {a} and {b} is: {result}')#the addition of {a} and {b} is: {result}
""" So the above output shoes the importantce of FORMAT FUNCTION
whoose syntax can be use along with print as -
print(f'STATEMENT INSIDE SYNTAX')
"""

a=int(input("Enter a's value - "))
b=int(input("Enter b's value - "))
sum = a+b
print(f'The sum of {a} & {b} is {sum} and {type(sum)}')
"""
Enter a's value - 45
Enter b's value - 5
The sum of 45 & 5 is 50 and <class 'int'>
"""

Enter a's value - "hinjewadi"
Enter b's value - \"It Park"
sum = a+b
print(f'The combinatioon of {a} & {b} is {sum} which is in Pune ')


x = int(input("Enter X here : "))#Enter X here : 45
print(x,type(x))#45 <class 'int'>

x = bool(input("Enter your X here mr. Sex : "))#Enter your X here mr. Sex : 1
print(x,type(x))#True <class 'bool'>

x = (input("Enter your X here mr. Sex : "))#Enter your X here mr. Sex : hii
print(x,type(x))#hii <class 'str'>

x = eval(input("Enter your X here mr. Sex : "))#Enter your X here mr. Sex : "Hiii"
print(x,type(x))#Hiii <class 'str'>

# So when you are using eval function that is Evaluate then make sure to write insode string
# and when you are not specifying any kind of daattype then directly write the statement even w/o using strings

------------------------------------------------------------------------------------------------------------------------------------

- what is a module in python -
Import statement in python to be use one file's info into another file
A module is nothing but predefined python script
Predefined - modules/default modules - when we install python soiftware then some modules installed automativaaly are known as Pre defined Modules or Default modules
Third-party Modules

to see the installed modules use - python help() "modules"

Code -

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
time.sleep(4)# it is a time module. time.sleep() inlcludes seconds after the compiler run again - here it is of 4 seconds.

#pip --help : - command for getting all help related ti install, delete or anything with pip in cmd.
------------------------------------------------------------------------------------------------------------------------------------
# Strings in Python -
What is a String in Python -
1 - A string is a sequence of characters
2 - A character is simply a symbol. For Example, the English langauge has 26 characters
3 - Computer do not deal with characters, they dewal with only binary numbers
4 - This conversion of character to a number is called encoding, and the reverse process is called aas decoding. ASCII and Unicode chracter are some of the popoular encoding used.
5 - In python, String is sequence of unicode characters . Unicode was introdices to include every character in all langauges and bring unifomityy encoding.

* How to create a string - 
code -
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

* how to access elements fron string using index values (slicing of a string)-
Code - 
my_current_target = "Automation Anywhere's 12 LPA Package"
print(my_current_target)#Automation Anywhere's 12 LPA Package
print(f'{my_current_target}')#Automation Anywhere's 12 LPA Package
print(my_current_target[0])#A - when I want to acess the very first character
print(my_current_target[-1])#e - For at last character
print(my_current_target[0:])#Automation Anywhere's 12 LPA Package - Printing from 0(begin) to last
print(my_current_target[0:25])#Automation Anywhere's 12 - in the indexing always remember that start with lower value 
print(my_current_target[:37])#Automation Anywhere's 12 LPA Package - from by default begin to desired range

* How to change or delete a string

Deletion of a string is not possible because string is Immutable. yeah instread of delete we can assign a new value to the old used string name

my_current_target = "Placement Success Celeebration"
print(my_current_target)#Placement Success Celeebration

* How to find the length of a string -


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

------------------------------------------------------------------------------------------------------------------------------------
#Case Conversion Operations on String -
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
------------------------------------------------------------------------------------------------------------------------------------
#display string at Right/Left/Center of a line in title format

given_str = input("Enter the desired String\n")
print(given_str)
I created this syntax in a new file and opened the file in cmd, by using cmd in that folder and type NAMEOFFILE.py then use python NAMEOFFILE.py . it will perform the operation in cmd.
now by using mode command inn cmd it will give all necesssarty detauils of string.

E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts>mode

Status for device CON:
----------------------
    Lines:          30
    Columns:        120
    Keyboard rate:  31
    Keyboard delay: 1
    Code page:      437

Code -

given_str = input("Enter the desired String\n")
print(given_str)# by using it .. it prints the string usually at LHS.

print(given_str.center(120))# by using it .. it print the string at distance of 120 from left and in the center

print(given_str.ljust(110))# by using it .. it print the string at distance of 110 from left
print(given_str.rjust(110))# by using it .. it print the string at distance of 110 from right

In python, it can adjust the length as per the operating system. The length parameter we are using for left, right and center may be differ for Linux OS. so python automatically adjust it self.
As it is platfrom independent lamnguage. In cmd using some commads we can get the details of OS for No. of columns and lines.

In CMD - 
"""
>>> import os
>>> os.get_terminal_size()
os.terminal_size(columns=120, lines=30)
>>> os.get_terminal_size().columns
120
>>> os.get_terminal_size().lines
30
""""
By importing os, pythin will automatically manage the distance as per no. of columns

Code -
#Using OS commads for width Automatically. Please use Window Powershell to perform the operations

import os

t_w = os.get_terminal_size().columns

given_str = input("Enter the desired String\n")
print(given_str)# by using it .. it prints the string usually at LHS.

print(given_str.center(t_w).title())# by using it .. it print the string at distance as per the OS Columns and Rows from left and in the center in a title formaat

print(given_str.ljust(t_w).title())# by using it .. it print the string at distance from OS Columns and Rows from left in a title formaat first letter of each word in Capital Format
print(given_str.rjust(t_w).title())# by using it .. it print the string at distance from OS Columns and Rows from right in a title formaat
------------------------------------------------------------------------------------------------------------------------------------
# Read a directory and identify all files and directory

In CMD -
type NAMEOFFILE.py
python NAMEOFFILE.py
 Now paste directory and you will read anything inside this.
 
using For loop basic concept
for each in [1,2,3,4,5]:
    print("shubhan placed in Automation Anywhere")

"""
shubhan placed in Automation Anywhere
shubhan placed in Automation Anywhere
shubhan placed in Automation Anywhere
shubhan placed in Automation Anywhere
shubhan placed in Automation Anywhere
"""
print("before the loop")
for each in [2,3,4,5]:
    print("hii Shubh",each)

print("After the Loop")
"""
before the loop
hii Shubh 2
hii Shubh 3
hii Shubh 4
hii Shubh 5
After the Loop
"""

#idrectory and File Reading. 
import os
import sys
path=input("Enter your directory path: ")
if os.path.exists(path):
    df_l = os.listdir(path)
else:
    print("Please provide valid path")
    sys.exit()

list_of_Files_dir = os.listdir(path)
print("all files and dir are: ", list_of_Files_dir)

for each_file_or_dir in list_of_Files_dir:
    print(each_file_or_dir)

"""
Enter your directory path: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
all files and dir are:  ['.learn.py.swp', 'Basic Concepts 2.py', 'Basic Concepts.py', 'Basic Concepts3.py', 'Code Running and Notes.txt', 'Learn.py', 'Learn_Python.py', 'Operation OS with Python In Pwershell.png', 'Python Automation Script Notes.py', 'ReadytoPlaced', '__pycache__']
.learn.py.swp
Basic Concepts 2.py
Basic Concepts.py
Basic Concepts3.py
Code Running and Notes.txt
Learn.py
Learn_Python.py
Operation OS with Python In Pwershell.png
Python Automation Script Notes.py
ReadytoPlaced
__pycache__
"""
"""
Enter your directory path: E:\DarkBox\TMOTR\LOA Workshop
all files and dir are:  ['1.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '2.jpg', '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg', '29.jpg', '3.jpg', '30.jpg', '31.jpg', '32.jpg', '33.jpg', '34.jpg', '35.jpg', '36.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', 'BLOA.pdf', "BSR's LOA.txt", 'Law of Attraction Day 1.mp4', 'Law of Attraction Workshop Day -3 By CoachBSR.mp4', 'Mastering the Law of Attraction for a Life of Abundance and Fulfillment Day -2 By CoachBSR.mp4']
1.jpg
10.jpg
11.jpg
12.jpg
13.jpg
14.jpg
15.jpg
16.jpg
17.jpg
18.jpg
19.jpg
2.jpg
20.jpg
21.jpg
22.jpg
23.jpg
24.jpg
25.jpg
26.jpg
27.jpg
28.jpg
29.jpg
3.jpg
30.jpg
31.jpg
32.jpg
33.jpg
34.jpg
35.jpg
36.jpg
4.jpg
5.jpg
6.jpg
7.jpg
8.jpg
9.jpg
BLOA.pdf
BSR's LOA.txt
Law of Attraction Day 1.mp4
Law of Attraction Workshop Day -3 By CoachBSR.mp4
Mastering the Law of Attraction for a Life of Abundance and Fulfillment Day -2 By CoachBSR.mp4
"""


import os
import sys
path=input("Enter your directory path: ")
if os.path.exists(path):
    df_l = os.listdir(path)
else:
    print("Please provide valid path")
    sys.exit()

list_of_Files_dir = os.listdir(path)
print("all files and dir are: ", list_of_Files_dir)

for each_file_or_dir in list_of_Files_dir:
    f_d_p = os.path.join(path,each_file_or_dir)
    if os.path.isfile(f_d_p):
        print(f'{f_d_p} is a file')
    else:
        print(f'{f_d_p} is a directory')

"""
Enter your directory path: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
all files and dir are:  ['.learn.py.swp', 'Basic Concepts 2.py', 'Basic Concepts.py', 'Basic Concepts3.py', 'Code Running and Notes.txt', 'Learn.py', 'Learn_Python.py', 'Operation OS with Python In Pwershell.png', 'Python Automation Script Notes.py', 'ReadytoPlaced', '__pycache__']
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\.learn.py.swp is a file
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts 2.py is a file
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts.py is a file
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts3.py is a file
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Code Running and Notes.txt is a file
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn.py is a file
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn_Python.py is a file
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Operation OS with Python In Pwershell.png is a file
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Python Automation Script Notes.py is a file
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced is a directory
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\__pycache__ is a directory
"""
------------------------------------------------------------------------------------------------------------------------------------

# Find all files in a directory with extension .py/.sh/.log/.txt
Code -
import os
req_path = input("Enter your directory path: ")


if os.path.isfile(req_path):
    print(f"the given path {req_path} is a file.Please pass only directory path")
else:
    all_f_dir = os.listdir(req_path)
    if len(all_f_dir)==0:
        print(f"The Given path is {req_path} an empty path there is no file inside the directory")
    else:
        req_ex = input("Enter the required files extension .py/.sh/.log/.txt: ")
        req_files=[]
        for each_f in all_f_dir:
            if each_f.endswith(req_ex):
                req_files.append(each_f)
        if len(req_files)==0:
            print(f"there are no {req_ex} files in the location of {req_path}")
        else:
            print(f"There are {len(req_files)} files in the location of {req_path} woith an extension of {req_ex}")
            print(f"So, the files are: {req_files}")

# Note - Run the code in CMD for better response
"""
Enter your directory path: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
Enter the required files extension .py/.sh/.log/.txt: .py
The required files are: ['Basic Concepts 2.py', 'Basic Concepts.py', 'Basic Concepts3.py', 'Learn.py', 'Learn_Python.py', 'Learn_Python2.py', 'Python Automation Script Notes.py']
"""
"""
Enter your directory path: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
Enter the required files extension .py/.sh/.log/.txt: .txt
The required files are: ['Code Running and Notes.txt']
"""
"""
Enter your directory path: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced\Checking FIle Directories
The Given path is E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced\Checking FIle Directories an empty path there is no file inside the directory
"""
"""
Enter your directory path: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
Enter the required files extension .py/.sh/.log/.txt: .py
There are 7 files in the location of E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts woith an extension of .py
So, the files are: ['Basic Concepts 2.py', 'Basic Concepts.py', 'Basic Concepts3.py', 'Learn.py', 'Learn_Python.py', 'Learn_Python2.py', 'Python Automation Script Notes.py']
"""
------------------------------------------------------------------------------------------------------------------------------------

# Find all the files from directory using pythin script which are older than X days
Code - 
import os
import sys
import datetime
req_path = input("Enter Your Path: ")
age=3 # it is a age factore means file shouldn't be older than 3 days
if not os.path.exists(req_path):
    print("Please provide valid path ")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide directory path ")
    sys.exit(2)
    
today=datetime.datetime.now()

for each_file in os.listdir(req_path):
    each_file_path = os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
        file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        #print(each_file_path,datetime.datetime.fromtimestamp(os.path.getctime(each_file_path)))
        #print(dir(today-file_cre_date))
        dif_days = (today-file_cre_date).days
        if dif_days > age:
            print(each_file_path,dif_days)
""" Getting all files
Enter Your Path: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\.learn.py.swp
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts 2.py
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts.py
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts3.py
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Code Running and Notes.txt
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn.py
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn_Python.py
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn_Python2.py
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Operation OS with Python In Pwershell.png
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Python Automation Script Notes.py
"""
"""Finding all files with created date and time 
Enter Your Path: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\.learn.py.swp 2024-09-28 13:45:43.809754
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts 2.py 2024-09-28 17:38:07.081889
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts.py 2024-09-28 13:54:21.458758
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts3.py 2024-10-04 19:38:59.231490
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Code Running and Notes.txt 2024-10-04 19:48:36.897151
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn.py 2024-09-28 17:49:45.104752
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn_Python.py 2024-09-28 17:47:57.124169
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn_Python2.py 2024-10-05 12:03:05.341946
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Operation OS with Python In Pwershell.png 2024-10-04 19:02:26.100529
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Python Automation Script Notes.py 2024-09-27 22:58:37.122823
"""
""" it shows only those file which are created at leasst  before 3 days. It is not include the files which are new and created within 3 days
Enter Your Path: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\.learn.py.swp 6
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts 2.py 6
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts.py 6
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn.py 6
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn_Python.py 6
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Python Automation Script Notes.py 7
"""
------------------------------------------------------------------------------------------------------------------------------------

# os.walk(path) - used to generate directory and file names in a directory tree by walking.

os.walk is going to generate a list first. and inside the list there is tuple.

import os
path="E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts"
print(list(os.walk(path)))
print("_ _ - --____________________________________")

"""
[('E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts', ['ReadytoPlaced', '__pycache__'],
['.learn.py.swp', 'Basic Concepts 2.py', 'Basic Concepts.py', 'Basic Concepts3.py', 'Code Running and Notes.txt', 'Learn.py', 'Learn_Python.py',
'Learn_Python2.py', 'Operation OS with Python In Pwershell.png', 'Python Automation Script Notes.py']), ('E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\ReadytoPlaced',
['Checking FIle Directories'], ['Hello_word,py.py', 'Hello_word.py.py']), ('E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\ReadytoPlaced\\Checking FIle Directories', [], []),
('E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\__pycache__', [], ['Learn_Python.cpython-311.pyc', 'Trying.cpython-311.pyc'])]
"""

print("-----------")
for each in list(os.walk(path)):
    print(each)
print("_ _ - --____________________________________")    
    

"""
('E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts', ['ReadytoPlaced', '__pycache__'], ['.learn.py.swp', 'Basic Concepts 2.py', 'Basic Concepts.py', 'Basic Concepts3.py', 'Code Running and Notes.txt', 'Learn.py', 'Learn_Python.py', 'Learn_Python2.py', 'Operation OS with Python In Pwershell.png', 'Python Automation Script Notes.py'])
('E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\ReadytoPlaced', ['Checking FIle Directories'], ['Hello_word,py.py', 'Hello_word.py.py'])
('E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\ReadytoPlaced\\Checking FIle Directories', [], [])
('E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\__pycache__', [], ['Learn_Python.cpython-311.pyc', 'Trying.cpython-311.pyc'])
"""

""" Udnrstanding -
>>> x = [3,4,5]
>>> x
[3, 4, 5]
>>> x,y,z = [3,4,5]
>>> y
4
>>> z
5
>>> x
3
>>> Similarly for the directory i am gonna do for Root,Directory and Path
"""

for r,d,f in os.walk(path):
    print(r) # It will prints the roots only no any directory and no any file

"""
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced\Checking FIle Directories
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\__pycache__
"""
print("_ _ - --____________________________________")  
for r,d,f in os.walk(path):
    print(d)# it is printing only the directories(Folders) inside the root. Not printing the roots.
"""
['ReadytoPlaced', '__pycache__']
['Checking FIle Directories']
[]
[]
"""
print("_ _ - --____________________________________")
for r,d,f in os.walk(path):
    print(f)# it is printing the files only inside the directory(folder) which is inside the root
"""
['.learn.py.swp', 'Basic Concepts 2.py', 'Basic Concepts.py', 'Basic Concepts3.py', 'Code Running and Notes.txt', 'Learn.py', 'Learn_Python.py', 'Learn_Python2.py', 'Operation OS with Python In Pwershell.png', 'Python Automation Script Notes.py']
['Hello_word,py.py', 'Hello_word.py.py']
[]
['Learn_Python.cpython-311.pyc', 'Trying.cpython-311.pyc']
"""

print("_ _ - --____________________________________")
for r,d,f in os.walk(path):
    print(r,d)# it is printing the Root and Directory(Folder)
"""
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts ['ReadytoPlaced', '__pycache__']
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced ['Checking FIle Directories']
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced\Checking FIle Directories []
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\__pycache__ []
"""
print("_ _ - --____________________________________")
for r,d,f in os.walk(path):
    print(d,f)# Prints directory(folder) and files inside the folder
"""
['ReadytoPlaced', '__pycache__'] ['.learn.py.swp', 'Basic Concepts 2.py', 'Basic Concepts.py', 'Basic Concepts3.py', 'Code Running and Notes.txt', 'Learn.py', 'Learn_Python.py', 'Learn_Python2.py', 'Operation OS with Python In Pwershell.png', 'Python Automation Script Notes.py']
['Checking FIle Directories'] ['Hello_word,py.py', 'Hello_word.py.py']
[] []
[] ['Learn_Python.cpython-311.pyc', 'Trying.cpython-311.pyc']
"""
print("_ _ - --____________________________________")
for r,d,f in os.walk(path):
    print(r,f)# Prints Root and Files inside the whole root without printing Directory(Folder)
"""
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts ['.learn.py.swp', 'Basic Concepts 2.py', 'Basic Concepts.py', 'Basic Concepts3.py', 'Code Running and Notes.txt', 'Learn.py', 'Learn_Python.py', 'Learn_Python2.py', 'Operation OS with Python In Pwershell.png', 'Python Automation Script Notes.py']
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced ['Hello_word,py.py', 'Hello_word.py.py']
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced\Checking FIle Directories []
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\__pycache__ ['Learn_Python.cpython-311.pyc', 'Trying.cpython-311.pyc'
"""
print("_ _ - --____________________________________")
for r,d,f in os.walk(path):
    if len(f) != 0:
        print(r)
        print(f)
"""
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
['.learn.py.swp', 'Basic Concepts 2.py', 'Basic Concepts.py', 'Basic Concepts3.py', 'Code Running and Notes.txt', 'Learn.py', 'Learn_Python.py', 'Learn_Python2.py', 'Operation OS with Python In Pwershell.png', 'Python Automation Script Notes.py']
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced
['Hello_word,py.py', 'Hello_word.py.py']
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\__pycache__
['Learn_Python.cpython-311.pyc', 'Trying.cpython-311.pyc']
"""
print("_ _ - --____________________________________")
for r,d,f in os.walk(path):
    if len(f) != 0:
        print(r)
        for each_file in f:
            print(each_file)
"""
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
.learn.py.swp
Basic Concepts 2.py
Basic Concepts.py
Basic Concepts3.py
Code Running and Notes.txt
Learn.py
Learn_Python.py
Learn_Python2.py
Operation OS with Python In Pwershell.png
Python Automation Script Notes.py
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced
Hello_word,py.py
Hello_word.py.py
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\__pycache__
Learn_Python.cpython-311.pyc
Trying.cpython-311.pyc
"""

print("_ _ - --____________________________________")
for r,d,f in os.walk(path):
    if len(f) != 0:
        print(r)
        for each_file in f:
            print(os.path.join(r,each_file))
            print("________________________________")

"""
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\.learn.py.swp
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts 2.py
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts.py
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Basic Concepts3.py
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Code Running and Notes.txt
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn.py
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn_Python.py
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Learn_Python2.py
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Operation OS with Python In Pwershell.png
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\Python Automation Script Notes.py
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced\Hello_word,py.py
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced\Hello_word.py.py
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\__pycache__
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\__pycache__\Learn_Python.cpython-311.pyc
________________________________
E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\__pycache__\Trying.cpython-311.pyc
"""
------------------------------------------------------------------------------------------------------------------------------------
# How to copy a file into another file using python - copy the content of a file into another file

- It uses the basic concept for transforming all content from one file to another file using Reading a File and usign Writing into another file

"""
sfile = "E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\Code Running and Notes.txt"#Source File
dfile = "E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\Newrandom.txt" #Destination File
"""
# Now I want to  ask for desired locations of Source file and Destination File. Not wants to enter the destination manually in the code.

sfile = input("Enter your Source File here : ")
dfile = input("Enter your Destination File here : ")
#"E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Writtable File from Source File"
sfo = open(sfile,'r')#opening the Source file, by default any file is always in reading mode
print(sfo.mode)
content = sfo.read()#Reading the Source File
sfo.close()#Closing the Source File

print(content)
"""
Code Running and Notes
Basic concepts - 1 
basic Concepts - 2 
Learn_Python
"""

dfo = open(dfile,'w')
dfo.write(content)
dfo.close()

"""
Enter your Source File here : E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\Code Running and Notes.txt
Enter your Destination File here : E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Writtable File from Source File
Code Running and Notes
Basic concepts - 1 
basic Concepts - 2 
Learn_Python
"""
#Note - It worked Successfully. File Opened Read it and Write at desired location by creating a file with the same Source file Content.
------------------------------------------------------------------------------------------------------------------------------------

# Working with CSV Files using Python - reading CSV Files

- What is CSV -
CSV --> Comma Seperated value
- It is a simple file format used to store tabular data, such as a Spreadsheet/Excel or database.

I am storing data in notepad using , operator and .csv extension.
E_no,S_name,Package,Company,Location
4088,Shubham_Mahajan,12LPA,Automation_Anywhere,Bangalore
7009,Krishil_Shah,12LPA,Automation_Anywhere,vadodara
7012,Jainish_Shah,12LPA,Automation_Anywhere,Bangalore

I can also use | with .csv extension 
E_no|S_name|Package|Company|Location
4149|Aditya_Raj|12LPA|Automation_Anywhere|Vadodara
4154|Aditya_Singh|12LPA|Automation_Anywhere|Vadodara
4102|mayank_Patidar|12LPA|Automation_Anywhere|Vadodara
# now when i used pipeline | operaator then data stored in a singe column. - By using delemeter data can distuinguish in different columns

import csv
req_file="E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\PlacedStudents.csv"

fo = open(req_file)
content = fo.readlines()
fo.close()

for each in content:
    print(each.strip("\n"))
    
""" output - It is reading the lines of CSV files successfully
E_no,S_name,Package,Company,Location
4088,Shubham_Mahajan,12LPA,Automation_Anywhere,Bangalore
7009,Krishil_Shah,12LPA,Automation_Anywhere,vadodara
7012,Jainish_Shah,12LPA,Automation_Anywhere,Bangalore
"""
# we are in CSV so wants to take/read data as in table, row-column format, so by using -
print("_____________")
fo = open(req_file)
data=csv.reader(fo)

for each in data:
    print(each)
fo.close()
""" Output - in Table Format
['E_no', 'S_name', 'Package', 'Company', 'Location']
['4088', 'Shubham_Mahajan', '12LPA', 'Automation_Anywhere', 'Bangalore']
['7009', 'Krishil_Shah', '12LPA', 'Automation_Anywhere', 'vadodara']
['7012', 'Jainish_Shah', '12LPA', 'Automation_Anywhere', 'Bangalore']
"""
#Seperate the output using comma -
print("________")
fo = open(req_file)
content = csv.reader(fo)
for each in content:
    print(each)

fo.close()
"""
['E_no', 'S_name', 'Package', 'Company', 'Location']
['4088', 'Shubham_Mahajan', '12LPA', 'Automation_Anywhere', 'Bangalore']
['7009', 'Krishil_Shah', '12LPA', 'Automation_Anywhere', 'vadodara']
['7012', 'Jainish_Shah', '12LPA', 'Automation_Anywhere', 'Bangalore']
"""

# Now for another data in whch we use | fo storing by using .csv

import csv
req_file="E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\Placedin2ndround.csv"
print("________")
fo = open(req_file)
content = csv.reader(fo)
for each in content:
    print(each)

fo.close()
"""
['E_no|S_name|Package|Company|Location']
['4149|Aditya_Raj|12LPA|Automation_Anywhere|Vadodara']
['4154|Aditya_Singh|12LPA|Automation_Anywhere|Vadodara']
['4102|mayank_Patidar|12LPA|Automation_Anywhere|Vadodara']
"""
print("________")
fo = open(req_file)
content = csv.reader(fo,delimiter="|")# For better practice use Delimiter always in data and csv 
for each in content:
    print(each)

fo.close()
""" using delimiter pipelin | changed to comma ,
['E_no', 'S_name', 'Package', 'Company', 'Location']
['4149', 'Aditya_Raj', '12LPA', 'Automation_Anywhere', 'Vadodara']
['4154', 'Aditya_Singh', '12LPA', 'Automation_Anywhere', 'Vadodara']
['4102', 'mayank_Patidar', '12LPA', 'Automation_Anywhere', 'Vadodara']
"""
------------------------------------------------------------------------------------------------------------------------------------

# Functions of Python programming -

- A function is a block of code for some sspecific operation
- Function code is Re-usable
- A function executes only when it is called

import os
import time
import platform

"""
print("Please wait. Cleaning the Screen.....")
time.sleep(2)
os.system("cls")
print("Please wait finding the list of directories and files")
time.sleep(2)
os.system("dir")
"""
#Output - 
""" use cmd to run the code and outout as following - 
Please wait finding the list of directories and files
 Volume in drive E is Freebies
 Volume Serial Number is 14A2-9E79

 Directory of E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts

05-Oct-24  03:32 PM    <DIR>          .
05-Oct-24  02:43 PM    <DIR>          ..
04-Oct-24  07:38 PM             6,991 Basic Concepts 2.py
04-Oct-24  12:32 PM             6,380 Basic Concepts.py
04-Oct-24  07:45 PM                79 Basic Concepts3.py
04-Oct-24  07:48 PM                78 Code Running and Notes.txt
04-Oct-24  12:43 PM               182 Learn.py
05-Oct-24  12:02 PM             5,880 Learn_Python.py
05-Oct-24  02:45 PM            19,951 Learn_Python2.py
05-Oct-24  03:32 PM             2,801 Learn_Python3.py
05-Oct-24  03:33 PM               204 Learn_Python4.py
04-Oct-24  07:02 PM            67,784 Operation OS with Python In Pwershell.png
05-Oct-24  03:10 PM               200 Placedin2ndround.csv
05-Oct-24  03:00 PM               205 PlacedStudents.csv
05-Oct-24  02:59 PM               205 PlacedStudents.txt
05-Oct-24  03:26 PM            48,078 Python Automation Script Notes.py
05-Oct-24  12:30 PM    <DIR>          ReadytoPlaced
04-Oct-24  07:35 PM    <DIR>          __pycache__
              14 File(s)        159,018 bytes
               4 Dir(s)  33,963,794,432 bytes free
"""               

#note - This cls for clear Screen and dir for Directory commands is workingg only for windows and we want ti create this program as platform independent, so for Other os's commands are -


"""
if platform.system()=="Windows":
    print("Please wait. Cleaning the Screen.....")
    time.sleep(2)
    os.system("cls")
    print("Please wait finding the list of directories and files")
    time.sleep(2)
    os.system("dir")
else:
    print("Please wait. Cleaning the Screen.....")
    time.sleep(2)
    os.system("clear")
    print("Please wait finding the list of directories and files")
    time.sleep(2)
    os.system("ls -lrt")
"""    

#Now i am using the same logic 2 times for different os but it can be used 100 times,50 times as per the need .... so using function for the same program

def mycode(cmd1,cmd2):
    print("Please wait. Cleaning the Screen.....")
    time.sleep(2)
    os.system(cmd1)
    print("Please wait finding the list of directories and files")
    time.sleep(2)
    os.system(cmd2)

if platform.system()=="Windows":
    mycode("cls","dir")
else:
    mycode("clear","ls -lrt")

# this reusability technique is called as function and values which are actually given  are Actual Arguement whoile customized as per need are Formal Arguement
------------------------------------------------------------------------------------------------------------------------------------

# How to change Current Working Directory in Python
import os
req_path = input("Enter path to change working dir: ")
print("The current working dir is: ",os.getcwd())
try:
    os.chdir(req_path)
    print("Now your new working idr is: ",os.getcwd())
except FileNotFoundError:
    print("Given path is not a valid path. So can't change working directory")
except NotADirectoryError:
    print("Given path is a file path. So can't change Woprking Directory")
except PermissionError:
    print("Sorry you don;t have access fie the given path. So can't change the working directory")
except Exception as e:
    print(e)
    
    
"""
Enter path to change working dir: E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced
The current working dir is:  E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts
Now your new working idr is:  E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python Automation Scripts\ReadytoPlaced
"""
# In the above code,we can see changing the directory is easier to perform but during the directory change what exception you will get isn;t confirmed, so ready with all exception by trying and yuse all in the code
#using the function -
def main():
    req_path = input("Enter path to change working dir: ")
    print("The current working dir is: ",os.getcwd())
    try:
        os.chdir(req_path)
        print("Now your new working idr is: ",os.getcwd())
    except FileNotFoundError:
        print("Given path is not a valid path. So can't change working directory")
    except NotADirectoryError:
        print("Given path is a file path. So can't change Woprking Directory")
    except PermissionError:
        print("Sorry you don;t have access fie the given path. So can't change the working directory")
    except Exception as e:
        print(e)



if __name__=="__main__":
    main()

#Note - Build a habit to wriote the code inside main function by creating a main function sothat the logic can be used easily anywhere if rwuired.
------------------------------------------------------------------------------------------------------------------------------------

# Python Regular Expression(Re Module) Concept -
- What is a Regular Expression(RegEx)
the regex is  aprocedure in any language to look for a specified pattern in a given text.
- What is a Pattern ?
It is a sequence of characters,which represents miltiple strings.
Ex: 'i[st]' --> is it
    'python[23]' --> python2,python3
- In RE we have some different operations -
match()
search()
findall()
finditer()
sub()
split()
compile()
------------------------------------------------------------------------------------------------------------------------------------
#Rules to create a pattern in Python regular Expression -
- re is the module to perform regex in python.(use import re in scripts)
- There are different operations in re like: Search,match,finditer,findall,spli,sub

-Syntax -
re.search(pattern,text)
re.match(pattern,text)
re.finditer(pattern,text)
re.findall(pattern,text)

how to use findall?
import re
print(re.findall(pattern,text))

- Rules to create a pattern
basic Rules

1) a,X,9 - ordinary characters that match themselves
[abc] - Matches a OR b OR C {this is a string but can work for any matching character either a OR b OR c}
[a-c] - Matches a or b or c

[a-zA-Z0-9] - Matches any letter from (a to z) OR (A to Z) OR (0 to 9)

\w - Matches any singal letter, digit or underscore, includes [a-z],[A-Z],[0-9],[_]
\w\w - Matches with all possible combinations of \w in a pair. Ex. - aa,ab,a5,9z,p_,_o etc
\w\w\w - looking for the group of 3 characters of string which comes under \w category. aaa,a2_,___,_21,_m9,9_A etc

\W(capital W) - Matches any character not part of \w(small w)
\W\W(capital W) - Matches any character not part of \w(small w) in pair of 2
\W\W\W(capital W) - Matches any character not part of \w(small w) in pair of 3

\d - Matches decimal digit 0-9 (only for numbers,digits)

. - Matches any single character except newline character
.. - #Matching for any 2 symbols 
... - #Matching for any 3 symbols

\. uses for matching of . with . only so using \ skiping other characters

Code -

""">>> my_str = "Python is simple and it easy"
>>> my_str.split("is")
['Python ', ' simple and it easy']
>>> my_str.split("it")
['Python is simple and ', ' easy']
# now if i want to split is and it both at a time, then using normal string operations it is not possible, so by using Regular Exprfesseion re module concepts -
>>> import re
>>> re.split("i[st]",my_str)
['Python ', ' simple and ', ' easy']
"""
#------------------------------------------------------------------------------------------------------------------------------------
import re
text = "This is python2. language and 4 it is .  45 very @easy -to_learn_ @ python3"
my_rem_word = "is"
print(re.findall(my_rem_word,text))#['is', 'is', 'is'] # So in this re module findall it is searching for is and matching with every letter combination of every word and on matching it returns it and remove from the writter string
print(len(re.findall(my_rem_word,text)))#3 For getting the lenght of removing word how many times it is -

my_word = "i[ts]"# kind of re module which will remove word it and is
print(re.findall(my_word,text))#['is', 'is', 'it', 'is']

your_word = "a"
print(re.findall(your_word,text))#['a', 'a', 'a', 'a', 'a']

another_word = "9"
print(re.findall(another_word,text))#[]#trying to matching 9 but till it was not in the string so emty list

my_remove = "@"
print(re.findall(my_remove,text))#['@']

onemore_word = "[@as]" #looking for either @ OR a OR s
print(re.findall(onemore_word,text))#['s', 's', 'a', 'a', 'a', 's', '@', 'a', 's', 'a', '@']

my_money = "[abcd]"
print(re.findall(my_money,text))#['a', 'a', 'a', 'd', 'a', 'a'] # From the above string we want to match a OR b OR c OR d. But from the text string there were only a AND d, so it matches with only available strings from the text


my_money = "[a-d]"
print(re.findall(my_money,text))#['a', 'a', 'a', 'd', 'a', 'a'] # it can also be written as [a-d] contain all letter from a to d

#------------------------------------------------------------------------------------------------------------------------------------

#for small w

new_word = "\w"
print(re.findall(new_word,text))
"""
['T', 'h', 'i', 's', 'i', 's', 'p', 'y', 't', 'h', 'o', 'n', '2', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', 'a', 'n', 'd', '4', 'i', 't', 'i', 's', '4', '5', 'v', 'e', 'r', 'y', 'e', 'a', 's', 'y', 't', 'o', '_', 'l', 'e', 'a', 'r', 'n', '_', 'p', 'y', 't', 'h', 'o', 'n', '3']
""" # so space, @ are not comes under \w. it only includes - singal letter, digit or underscore


latest_word = "\w\w" 
print(re.findall(latest_word,text))#\w\w - Matches with all possible combinations of \w in a pair. Ex. - aa,ab,a5,9z,p_,_o

"""
['Th', 'is', 'is', 'py', 'th', 'on', 'la', 'ng', 'ua', 'ge', 'an', 'it', 'is', '45', 've', 'ry', 'ea', 'sy', 'to', '_l', 'ea', 'rn', 'py', 'th', 'on']
"""

print("___________")
latest_word = "\w\w\w"
print(re.findall(latest_word,text))#\w\w\w - looking for the group of 3 characters of string which comes under \w category. aaa,a2_,___,_21,_m9,9_A etc

"""
['Thi', 'pyt', 'hon', 'lan', 'gua', 'and', 'ver', 'eas', 'to_', 'lea', 'rn_', 'pyt', 'hon']
"""
#------------------------------------------------------------------------------------------------------------------------------------

#fro capital W

new_word = "\W"
print(re.findall(new_word,text))

"""
[' ', ' ', '.', ' ', ' ', ' ', ' ', ' ', ' ', '.', ' ', ' ', ' ', ' ', '@', ' ', '-', ' ', '@', ' ']
"""


latest_word = "\W\W" 
print(re.findall(latest_word,text))

"""
['. ', ' .', '  ', ' @', ' -', ' @']
"""


latest_word = "\W\W\W"
print(re.findall(latest_word,text))

"""
[' . ', ' @ ']
"""
#------------------------------------------------------------------------------------------------------------------------------------



print("___________")
number_word = "\d"
print(re.findall(number_word,text))#['2', '4', '3']# \d only for single digits


word="python\d"
print(re.findall(word,text))#['python2', 'python3']


print("___________")
numerical_word = "\d\d"
print(re.findall(numerical_word,text))#['45']## \d\d only for two digit numbers

#------------------------------------------------------------------------------------------------------------------------------------


print("___________")
yup_word = "."
print(re.findall(yup_word,text))
"""
['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'p', 'y', 't', 'h', 'o', 'n', '2', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', '
', 'a', 'n', 'd', ' ', '4', ' ', 'i', 't', ' ', 'i', 's', ' ', '4', '5', ' ', 'v', 'e', 'r', 'y', ' ', '@', 'e', 'a', 's',
'y', ' ', '-', 't', 'o', '_', 'l', 'e', 'a', 'r', 'n', '_', ' ', '@', ' ', 'p', 'y', 't', 'h', 'o', 'n', '3']
"""#. - Matches any single character except newline character - It including evrything even spaces, Special characters also 

print("___________")
yup_word2 = ".."
print(re.findall(yup_word2,text))
"""
['Th', 'is', ' i', 's ', 'py', 'th', 'on', '2 ', 'la', 'ng', 'ua', 'ge', ' a', 'nd', ' 4', ' i', 't ', 'is', ' 4', '5 ', 've', 'ry', ' @', 'ea', 'sy', ' -', 'to', '_l', 'ea', 'rn', '_ ', '@ ', 'py', 'th', 'on']
"""#Matching for any 2 symbols 

print("___________")
yup_word3 = "..."
print(re.findall(yup_word3,text))
"""
['Thi', 's i', 's p', 'yth', 'on2', ' la', 'ngu', 'age', ' an', 'd 4', ' it', ' is', ' 45', ' ve', 'ry ', '@ea', 'sy ', '-to', '_le', 'arn', '_ @', ' py', 'tho']
"""#Matching for any 3 symbols


print("___________")
my_try = "\."
print(re.findall(my_try,text)) #['.', '.'] #\. uses for matching of . with . only so using \ skiping other characters

#------------------------------------------------------------------------------------------------------------------------------------


print("___________")
text = "This is my ip of a db server : 255.100.102.103"
pat="\d\d"
print(re.findall(pat,text))#['25', '10', '10', '10']

print("___________")
pat2="\d\d\d"
print(re.findall(pat2,text))#['255', '100', '102', '103']

print("___________")
pat3="\d\d\d.\d\d\d.\d\d\d.\d\d\d"
print(re.findall(pat3,text))#['255.100.102.103']# now it's owrking perfectly for ip address kind of strings

#------------------------------------------------------------------------------------------------------------------------------------


print("___________")
text = "This is my ip of a db server : 255.100.102.103 ShubhamMahajanisPlacedin AutomationAnywhereatPackageof12LPAhavingchoiceofVarodara/Bengaluru"
pat4="\w\w\w.\w\w\w.\w\w\w.\w\w\w"
print(re.findall(pat4,text))
"""
['255.100.102.103', 'ShubhamMahajani', 'lacedin Automat', 'ionAnywhereatPa', 'ckageof12LPAhav', 'ingchoiceofVaro']
"""

print("___________")
text = "This is my ip of a db server : 255.100.102.103 9826410840966999988096699998819981665430992669161494794051669009406006 "
pat5="\d\d\d.\d\d\d.\d\d\d.\d\d\d"
print(re.findall(pat5,text))# if wants to match . with . exactly use \. at the place of . as per the string. yaha ip addrsss me 3 digit k baad . he to vaha exactly 3 digit ke baad . laane k liye \d\d\d ke baad \. use kre
"""
['255.100.102.103', '982641084096699', '998809669999881', '998166543099266', '916149479405166']
"""

print("___________")
text = "This is my ip of a db server : 255.100.102.103 9826410840966999988096699998819981665430992669161494794051669009406006 "
pat5="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
print(re.findall(pat5,text))#['255.100.102.103']

------------------------------------------------------------------------------------------------------------------------------------

# Compile Operation of re module

Code -
import re
my_str = "This is about python Python is easy to learn and we have two major versions: pythin2 and python3"
my_pat = r'\bPython[23]?\b'

print(re.findall(my_pat,my_str,flags=re.I))#['python', 'Python', 'python3']
# flags used here for case sensitiveness for both cases of Capital & Small
#? used here because 2 or 3 is optional with word python. So for using both with the word

print(re.search(my_pat,my_str))
#<re.Match object; span=(21, 27), match='Python'>
print(re.split(my_pat,my_str))
#['This is about python ', ' is easy to learn and we have two major versions: pythin2 and python3']

pat_ob=re.compile(my_pat,flags=re.I)
print(pat_ob) #re.compile('\\bPython[23]?\\b', re.IGNORECASE)
print(pat_ob.search(my_str)) #<re.Match object; span=(14, 20), match='python'>
print(pat_ob.findall(my_str)) #['python', 'Python', 'python3']

#re.findall(my_pat,my_str)==> re.compile(my_pat).findall(my_str)

------------------------------------------------------------------------------------------------------------------------------------
# Working with Remote Linux Server from Linux/Windows using paramiko of Python

Possible Combinations of Servers
Local Server         Remote Servers

Windows                 Windows
Windows                 Linux
Linux                   Linux
Linux                   Windows

Currently working for - Local Server is : Linux/Windows and remote Server is : Linux
------------------------------------------------------------------------------------------------------------------------------------
# Transfer a file from Local Server to Remote Server and Viceversa using Paramiko of Python

------------------------------------------------------------------------------------------------------------------------------------

#What is an OOps -

It is about Class,Object,Inheritance,Polymorphism,Data Abstraction and Data Encapsulation
- What is an Object -
Object could be anything which exists in Real-Time, like Human,Fan,Car,Email, Any Application, jenkinsWeblogic,Tomcat,Apache etc
. Each Object has characterisitcsand Functions -
Ex - Person/Human;
So Characteristics are  - Name,Age,Address
and Functions are  - Walking,Talking,Running, all other activities

Why OOP's ?
To group related Functions(Methods)
To create a template/blueprint
Oop's is a concept where charaacteristics and functions of a real-life object is packaged as single entity in the code.

------------------------------------------------------------------------------------------------------------------------------------

#Note - If you are not good with OOP's then don't worry for Automation but if you are in Application then OOp's is a backbone

# Class & Object Attributes in OOp's in Python programming-
- What is a Class -
. Class is a template/blueprint to create an object
. Class is the combination of attributes and methods
. We can define attribuites for Class and Objects










































\



























































------------------------------------------------------------------------------------------------------------------------------------
To be remember some points -
* for access the value from defined variable use {} in print statement.
  for access characters from a string use [] brackets

* in CMD, if i want to open and see the code so open that directory in cmd & use command type NAMEOFFILE.py
  Similarly if i want to run the code in cmd so open that directory in cmd & use command python NAMEOFFILE.py
  

Ask for help inn Python  -
..>import os
   dir(os.path)
   
-->python
   help()

For a particular variable -
..>print(dir(emp1))

   
                                                                                                                                                             







