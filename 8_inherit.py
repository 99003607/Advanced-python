#private variables
'''
class Test():
    #constructor(double underscore in init)
    def __init__(self):
        print("in _init_:assing value");
        #public variables
        self.i=10;
        #private variables
        self.__j=99;
    def mod(self):
        self.i=99; 
    
    def display(self):
        print("i value=",self.i);
    
#Test obj1; not work
obj1= Test();
print(obj1.__dict__);
#accessing private variables
print(obj1.__dict__["_Test__j"]);
#print(obj1[j]);
'''

#inheritance
'''
class A():
    def display(self): 
        print("A.display");
    
class B(A):
    pass;
    
#MRO -> Method Resolution Order   
print(B.mro());
b = B();
b.display(); #here self is b
'''
#pro2
'''
class A():

    def set_val(self):
        self.i=100;
    def display(self): 
        print("A.display",self.i);
    
class B(A):
    def display(self): 
        print("B.display",self.i);
    
#MRO -> Method Resolution Order   
print(B.mro());
b = B();
b.set_val();
b.display(); #here self is b
'''

#mro
'''
class A():
    def __init__(self):
        self.i=100;
    def set_val(self):
        self.i=100;
    def display(self): 
        print("A.display",self.i);
    
class B(A):
    def __init__(self):
        super().__init__(); #calling constructor of imediate base class
    def display(self): 
        print("B.display",self.i);
    
#MRO -> Method Resolution Order   
print(B.mro());
b = B();
b.display(); #here self is b
'''