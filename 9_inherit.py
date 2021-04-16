#single inheritance
'''
class A():
    def __init__(self):
        print("A__init__");
        self.i=100;
    
class B(A):
    def __init__(self):
        print("B__init__");
        super().__init__(); #calling constructor of imediate base class
        
    def display(self): 
        print("B.display",self.i);

class C(B):
    def __init__(self):
        super().__init__();
    
print(C.mro());
c= C();
c.display();
'''

#multiple inheritance
'''
class A():
    def __init__(self):
        print("A__init__");
        
    
class B():
    def __init__(self):
        print("B__init__");
        #super().__init__(); #calling constructor of imediate base class
        self.i=100;
    def display(self): 
        print("B.display",self.i);

class C(A,B):
    def __init__(self):
        print("C.__init__");
        super(C,self).__init__();
        super(A,self).__init__();
print(C.__mro__);
c= C();
c.display();
'''