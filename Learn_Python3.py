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
#------------------------------------------------------------------------------------------------------------------------------------






















































