#Inheritance
#Single inheritance
''''
class Parent:
     def parentfunc(self):
          print("This is parent function")
class Child(Parent):
     def childfunc(self):
          print(" This is child function ")
ch = Child()
ch.parentfunc()
ch.childfunc()

#Multiple Inheritance
class Parent1:
   def parentfunc1(self):
        print("This function belongs to parent1")

class Parent2:
   def parentfunct2(self):
        print("This function belongs to parent 2")

class Child1(Parent1,Parent2):
    def childfunc(self):
        print("This function belongs to child")
 
ch1=Child1()
ch1.parentfunc1()
ch1.parentfunct2()
ch1.childfunc()
'''

class Parent: # Example of Multilevel Inheritance
      def parentfunct(self):
        print("This function belongs to parent ")
class Child1(Parent):
      def childfunc1(self):
          print("This function belongs to child 1")
class Child2(Child1):
      def childfunc2(self):
        print("This function belongs to child 2")
child2ob = Child2()
child2ob.parentfunct()
child2ob.childfunc1()
child2ob.childfunc2()

class Parent: # Example of Hierarchical
      def parentfunc(self):
          print("This function belongs to parent")
class Child1(Parent):
      def childfunc1(self):
          print("This function belongs to child 1")
class Child2(Parent):
      def childfunc2(self):
          print("This function belongs to child 2")
 
child1ob = Child1()
child1ob.parentfunc()
child1ob.childfunc1()
child2ob=Child2()
child2ob.parentfunc()
child2ob.childfunc2()
