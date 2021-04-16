#python is both intepreter and compilers

i=100;
print(type(i));


#comments
'''' multiline comments 
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("text")
text
>>> i=10
>>> j=3
>>> i/j
3.3333333333333335
>>> i//j
3
>>> 2 **3
8
>>> 10 <2
False
>>> 10>2
True
'''

#arthmetic operators

# ** //

# // integer division

# 2**3 2 power 3

#relation operators
# <  >   !   !=
#results boolean


#strings

text= "python programming"
print(text);

print(text[0]);
#slicing
print(text[2:5]);

print(text[:5]);

print(text[5:]);

#length
print(len(text));

#increment

print(text[1:10:2]);

#negative index from last

print(text[-1:-5:-1]);

print(text[:-5:-1]);
#string reverse
print(text[-1::-1]);

#strings are mutable(not modifyable)
#cannot modify the string
#i=10; adress(i) ->1000
#i=i+1; adress(i)-> 2623  
#integers are assigned another address

i=10;
print(id(i));
i=i+10;
print(id(i));