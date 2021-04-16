#control structures
'''
if(condition):
    statement1;
    statement2;
elif(condition):
    statement;
    statement;
else:
    statement;
    statement;
 '''
n=-10;
if(n>0):
    print("positive");
elif(n<0):
    print("negative");
else:
    print("zero");

print("program end");


#loops
'''
while(conditions):
    statement;
  '''
  

print("while loops");
i=1;
while(i<10):
    print("i=",i);
    i=i+1;
   

#for loop
n=10;
for i in range(10):
	print(i);
	


#break -> to stop the loop
#continue -> to continue the loop
print("while loops->break");
i=1;
while(i<10):
    print("i=",i);
    if(i==5):
        break;
    i=i+1;
print("while loops->continue");
i=1;
while(i<10):
	if(i==5):
		i=i+1;
		continue;
	print("i=",i);
	i=i+1;
 

