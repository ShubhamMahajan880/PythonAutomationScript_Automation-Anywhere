class emp:
    count=0
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        return None

    def increase_count_for_emp(self):
        emp.count=emp.count+1
        return None
    def display_details(self):
        print(f'The name is: {self.name}\n The age is: {self.age}\n The Salary is: {self.salary}')
        return None

emp1=emp()
emp2=emp()

#print(dir(emp1))# Purpose of uding self as an argument is - if the object is calling it self then it will be replace at place of self

"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'display_details', 'get_name_age_salary', 'name', 'salary']
"""


emp1.get_name_age_salary('Shubham',22,1200000)
emp1.increase_count_for_emp()
emp2.get_name_age_salary('Jainish',21,1200000)
emp2.increase_count_for_emp()

print(emp.count)

emp1.display_details()
emp2.display_details()
print(emp.count)
emp.count=emp.count+1
print(emp.count)

