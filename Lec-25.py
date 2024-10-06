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
#------------------------------------------------------------------------------------------------------------------------------------


        
