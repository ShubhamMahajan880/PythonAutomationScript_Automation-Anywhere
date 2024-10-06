
"""
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
"""            

# Outputs - 
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
#------------------------------------------------------------------------------------------------------------------------------------
"""
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
"""

#Output -
            
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
#------------------------------------------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------------------------------------
"""
sfile = "E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\Code Running and Notes.txt"#Source File
dfile = "E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python Automation Scripts\\Newrandom.txt" #Destination File
"""
# Now I want to  ask for desired locations of Source file and Destination File. Not wants to enter the destination manually in the code.

sfile = input("Enter your Source File here : ")
dfile = input("Enter your Destination File here : ")
#"E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Writtable File from Source File"
sfo = open(sfile,'r')#opening the Source file
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
#------------------------------------------------------------------------------------------------------------------------------------




























    
