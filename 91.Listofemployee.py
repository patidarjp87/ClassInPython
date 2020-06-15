print("define a class Employee")
class Employee:
    def __init__(self,l):
        self.emplist=l
    def showEmployee(self):
        self.emplist.sort()
        print("list of employees is",self.emplist)
    def sortbysalary(self,d):
        l=[]
        d1={}
        for x in d.values():
            l.append(x)
        l.sort()
        i=0
        while i!=len(l):
            for x in d.keys():
                if d[x]==l[i]:
                    d1.update({x:l[i]})
                    i+=1
                    if i==len(l):
                        break
        print('sort by salary',d1)       
print('Enter list of employees')
l=eval(input())
d={}
for x in l:
    print("Enter salary of employee",x)
    s=eval(input())
    d.update({x:s})
s1=Employee(l)
s1.showEmployee()
s1.sortbysalary(d)
input()
