print('Enter name ,age,sem,branch respectively as a list')
n,a,s,b=eval(input())
class student :
    def setStudent(self,n,a,s,b):
        self.name=n
        self.age=a
        self.sem=s
        self.branch=b
    def showStudent(self):
        print("student data is \nname= ",self.name)
        print("Age= ",self.age,'\nsemester is ',self.sem,'and branch is ',self.branch)
s1=student()
s1.setStudent(n,a,s,b)
s1.showStudent()
input()
