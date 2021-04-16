# exception handling
'''
print("before");
i=10;
j=0;

#here divsion by zero is not possible so it will give exception
k= i/j;
print("k value:",k);
print("after");
'''
'''
output=.
Traceback (most recent call last):
  File "11_exception_handle.py", line 6, in <module>
    k= i/j;
ZeroDivisionError: division by zero
'''
'''
1)name error
2)index error
3)zerodivision error
etc
'''


#syntax
'''
try:
    statement(s)
except ExceptionType:
    handle here
'''

#exception

i=10;
j=0; #put j=1; and run
l= [1,2,3,4];
try:
    print("before");
    i=i+x; # name error->no expection for name 
    l[10]=100; #index error
    k= i/j; #ZeroDivisionError
    #print("k value:",k);

except ZeroDivisionError as ex:
    print("ZeroDivisionError:",ex.args);

except IndexError as ex:
    print("IndexError",ex.args);

except Exception as ex:
    print("Main Exception",ex.args);
else:
    print("in else:no exception");#print if no expection
finally:
    print("program end"); #print after all ends
