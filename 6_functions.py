#functions
'''
def <functionname>([arguments]):
    statemants;
    return();
'''
'''
def display(x):
    print("in display:",x);

print("start");    
display(10);
print("end");
'''
'''
#addtion function
def add(a,b):
    #print("result=",(a+b));
    a=a+10;
    b=b+20;
    return(a+b)

print("start");   
i=20;
j=30; 
s=add(i,j);
print("result:",s);
print("i=",i);
print("j=",j);
print("end");
'''

'''
def add(a,b):
    #print("result=",(a+b));
    a=a+10;
    b=b+20;
    return(a+b);
    
def test(l):
    l.append(11);
    l.append(22);
    
    
l1=[1,2,3,4,5];
print(l1);
test(l1); # here l1 adress is passed(the real one,not duplicate);same thing for tuple,string,etc
print(l1);

# to send copy->pass by value test(l1[:]);

'''
#ex1
'''
def inc(a,b):
    #print("result=",(a+b));
    a=a+10;
    b=b+20;
    return(a,b);
    
i=10;
j=20;
print("before");
print("i:",i);
print("j:",j);
result=inc(i,j); 
print(result); # here result is tuple

x,y=inc(i,j);
print("after");
print("i:",i);
print("j:",j);
'''

#default arguments
'''

def inc(a,b=20):
    #print("result=",(a+b));
    a=a+10;
    b=b+20;
    return(a,b);
    
i=10;
j=20;
 
i,j=inc(a=i,b=j); #keyword evaluvators
print(i,j);
'''


#variable number of arguments
'''
def sum(*args):
	s=0;
	print(type(args));
	for ele in args:
		s=s+ele;
	return(s);
    
print(sum(10,20));
print(sum(10,20,30));
print(sum(10,20,30,40));
'''

#variable number of arguments with name
'''
def sum(**d):
    s=0;
    for ele in d.values():
        s=s+ele;
    return(s);
    
print(sum(a=10,b=20));
print(sum(x=10,y=20,z=30));
print(sum(a=10,b=20,x=30,y=40));
'''