#object level variables => i,j
'''
class A():
	def __init__(self):
		self.i=10;
		
	def set_val(self):
		self.j=99;
	
	def display(self):
		print(self.i,"=>",self.j);
		
a =A();
print(a.__dict__);
a2= A();

a2.set_val();
print(a2.__dict__);
'''

#class level variables => 
'''
class A():
    count=1; #class level variables-> created before object creation
    def __init__(self):
        self.i=10;
        self.count=9999;
		
    def set_val(self):
        self.j=99;
	
    def display(self):
        print(self.i,"=>",self.j);
		
print(A.count);
obj= A();
print("obj.count:",obj.count);
'''