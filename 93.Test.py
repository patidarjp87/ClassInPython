class test:
   def f(self):
       print('normal f')
   @classmethod
   def __init__(cls):
       print("init")
   def f1():
        print("hello")
   @classmethod
   def f2(cls):
       cls.a=9
       print(test.a)
   @staticmethod
   def f3():
       print('in static method')
       test.b=8
       print(test.b)
       
t=test()
test.__init__()
t.__init__()
t.f2()
test.f2()
t.f3()
test.f3()
t.f()
test.f(9)
t.x=7
print(t.x)
print(t.a)
print(t.b)
print(test.__dict__)
print(t.__dict__)
input()

