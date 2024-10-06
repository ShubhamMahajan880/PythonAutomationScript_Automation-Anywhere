print("Hellop Shubham how are you")
print("Shubham Mahajn got placed in Automation Anywhere")
print("Shubham is the only student who got highest placement among all 2025 batch students")
 

print("Print the condition to get the package :")

a=5;
b=10;
result = a+b

print("the adddition of {a} and {b} is ", result) # If i use this then instead of values of a & b there is directly written statemment {a} and {b}, so use format function before the sttatement and using this {}

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

"""
Note: Any datatype can be converted into boolean
using - bool(any)_data_type)= True OR False
        bool(empty) = False
        bool(non-empty) = True
Examples -         
"""

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
x="2.1.3.5.8"
print(x,type(x))#2.1.3.5.8 <class 'str'> # now here any number/datatype can be converted into string but any string cannot be converted into number or any datatype
# clearly  2.1.3.5.58 is  a string but a 2.103.5.8 is not a number

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









