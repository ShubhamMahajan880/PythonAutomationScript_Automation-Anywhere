#lec- 24
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
#------------------------------------------------------------------------------------------------------------------------------------


    
    
































