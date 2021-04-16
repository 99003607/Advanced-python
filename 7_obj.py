#object oriented programming
'''
class <classname>([base classes]):
    instance/object methods
    class level methods
    class level variables
'''
#classes and objects
'''
pass; #do nothing creating class;self is compulsary for function arguments which is adress of object
class Test():
    def display(self):
        print("self type:", type(self));
        self.i=10; #create variable with value 10 under object.i
        print("in test.display()");
    
#Test obj1; not work
obj1= Test();

print(type(obj1));
obj1.display(); #t1.display(t1); passing adress of obj1

obj2= Test();

obj2.display();
'''

#multiple objects
'''
class Test():
    def set_value(self):
        self.i=10; #create variable with value 10 under object.i
        print("in set value");
    
    def display(self):
        print("i value=",self.i);
    
#Test obj1; not work
obj1= Test();

obj1.set_value();
obj1.display();


obj2= Test();
obj2.set_value();
obj2.display();
'''
#passing arguments
'''
class Test():
    def set_value(self,value):
        self.i=value; #create variable with value 10 under object.i
        print("in set value");
    
    def display(self):
        print("i value=",self.i);
    
#Test obj1; not work
obj1= Test();

obj1.set_value(100); #obj1.set_value( obj1, 100)
obj1.display();


obj2= Test();
obj2.set_value(200); #obj2.set_value( obj2, 200)
obj2.display();
'''
#defining variables inside class
'''
class Test():
    #constructor(double underscore in init)
    def __init__(self,val):
        print("in _init_:assing value");
        self.i=val;
    def set_value(self,value):
        self.i=value; #create variable with value 10 under object.i
        print("in set value");
    
    def display(self):
        print("i value=",self.i);
    
#Test obj1; not work
obj1= Test(200);

#obj1.set_value(100); #obj1.set_value( obj1, 100)
obj1.display();
'''