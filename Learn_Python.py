import os

my_target = "Get to Placed soon on the package of 12 LPAn Automation Anyewhere"
print(my_target)

"""
t_w = os.get_terminal_size().columns

given_str = input("Enter the desired String\n")
print(given_str)# by using it .. it prints the string usually at LHS.

print(given_str.center(t_w))# by using it .. it print the string at distance of 120 from left and in the center

print(given_str.ljust(t_w))# by using it .. it print the string at distance of 110 from left
print(given_str.rjust(t_w))# by using it .. it print the string at distance of 110 from right
"""

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

 # Read a directory and identify all files and directory

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
#------------------------------------------------------------------------------------------------------------------------------------
















































