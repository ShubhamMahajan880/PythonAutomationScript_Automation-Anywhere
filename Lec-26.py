
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

#------------------------------------------------------------------------------------------------------------------------------------
print("****************************************************************************")
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
#------------------------------------------------------------------------------------------------------------------------------------


