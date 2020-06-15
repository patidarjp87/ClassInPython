print("define a class Employee")
class Employee:
    def __init__(self,id,n,s):
        self.empid=id
        self.name=n
        self.salary=s
    def showEmployee(self):
        print("employee data is \nempid=",self.empid,'\nname =',self.name,'\nsalary =',self.salary)
print('Emter employee id,name and salary as a list respectively ')
id,n,s=eval(input())
s1=Employee(id,n,s)
s1.showEmployee()
input()