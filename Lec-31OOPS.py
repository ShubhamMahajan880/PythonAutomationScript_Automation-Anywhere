
"""
import os

def get_details_for_each_tomcat(server_xml):
    global tcf,th
    tcf=server_xml
    th=os.path.dirname(os.path.dirname(server_xml))
    return tcf,th

def display_details():
    print(f'The tomcat config file is: {tcf}\n The tomcat home is: {th}')
    return None
    

def main():
    tomcat7="/home/Automation/tomcat7/conf/server.xml"
    tomcat9="/home/Automation/tomcat9/conf/server.xml"
    get_details_for_each_tomcat(tomcat7)
    get_details_for_each_tomcat(tomcat9)

    display_details()
    display_details()
    
    return None

if __name__=="__main__":
    main()
"""    

#Output -     
"""
The tomcat config file is: /home/Automation/tomcat7/conf/server.xml
 The tomcat home is: /home/Automation/tomcat7
The tomcat config file is: /home/Automation/tomcat9/conf/server.xml
 The tomcat home is: /home/Automation/tomcat9
"""

#Ex - 2 : - 
#Whenever we define a variable inside the method then always use Self
import os
class Tomcat:
    def get_details_for_each_tomcat(self,server_xml):
        self.tcf=server_xml
        self.th=os.path.dirname(os.path.dirname(server_xml))
        return None
    
    def display_details(self):
        print(f'The tomcat config file is: {self.tcf}\n The tomcat home is: {self.th}')
        return None

        


def main():
    tomcat7=Tomcat()
    tomcat9=Tomcat()

    tomcat7.get_details_for_each_tomcat("/home/Automation/tomcat7/conf/server.xml")
    tomcat9.get_details_for_each_tomcat("/home/Automation/tomcat7/conf/server.xml")
    print(tomcat9.tcf)
    print(tomcat9.th)
    print(tomcat7.tcf)
    print(tomcat9.th) # this is the way how we can access the variables outside the class

#Output - 
"""
/home/Automation/tomcat7/conf/server.xml
/home/Automation/tomcat7
/home/Automation/tomcat7/conf/server.xml
/home/Automation/tomcat7
"""
##    tomcat7.display_details()
##    tomcat9.display_details()
##    return None

"""
so the difference between Function and OOP's that in Function we need to create
different functions and were passing formal parameters in that, But in OOp's
directly by creating a Class and using this class for different objects at a time
"""    

    
    

if __name__=="__main__":
    main()

#Note - If you are not good with OOP's then don't worry for Automation but if you are in Application then OOp's is a backbone
#------------------------------------------------------------------------------------------------------------------------------------

