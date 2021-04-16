class Test():
    #constructor(double underscore in init)
    def __init__(self):
        print("in _init_:assing value");
        self.i=100;
    def set_value(self,value):
        self.i=value; #create variable with value 10 under object.i
        print("in set value");
    
    def display(self):
        print("i value=",self.i);
    
#Test obj1; not work
obj1= Test();

#obj1.set_value(100); #obj1.set_value( obj1, 100)
obj1.display();