class A():
	count =1;
	def __init__(self):
		self.i=10;
		#self.count=23;
	@classmethod
	def mod_count(self):
		self.count=self.count+99; #A.count=A.count+99;
		#cls.count=cls.count+99;
print(A.count);
a= A();
a.mod_count(); #a.mod_count(A)
print("count in a:",a.count);
print("A.count:",A.count);