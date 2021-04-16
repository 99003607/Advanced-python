#regular expressions

#string processiong

import re; #module for regular expressions

#syntax->    re.match("pattern","string")

print(re.match("the","the man"));
#output
'''
<re.Match object; span=(0, 3), match='the'>
'''

print(re.match("the","i am the man"));
#output
'''
None
'''

#search
print(re.search("the","i am the man"));
#output
'''
<re.Match object; span=(5, 8), match='the'>
'''

# symbols
'''
a-z A-Z
0-9
special charaters
1) . -> Mathches any single charater in the string  
'''
print(re.match(".....","Hello")); #checking 8 charaters are there or not

'''
2) ? -> preceeding character can repeat 0 or 1 time
'''
print(re.match("He?llo","Hello")); #e can repeat zero 0r 1 times

print(re.match("He?llo","Heello"));

'''
3) + -> preceeding character can repeat 1 or more time
'''
print(re.match("He+llo","Hello")); 

print(re.match("He+llo","Hllo")); 

'''
4) * -> preceeding character can repeat 0 or more time
'''
print(re.match("He*llo","Hello")); 

'''
[ ] -> matches any single character in the list
'''
print(re.match("[abc]","abc123def")); #either a or b or c

print(re.match("[abc]+","abc123def")); #either a or b or c

print(re.match("[a-z]+","abcdef123"));


print(re.match("[a-z1-24]+","abcdef123567def")); 
'''
output
<re.Match object; span=(0, 8), match='abcdef12'>
'''

print(re.match("[a-z0-9]+","abcdef123567def")); #matched everything

'''
[ ^] -> does matches any single character in the list
'''

print(re.match("[^0-9]+","abcdef123567def")); 
'''
output
<re.Match object; span=(0, 6), match='abcdef'>
'''

'''
^ -> strating with same character
'''
print(re.match("^H","HELLO")); 

'''
$ -> ending with same character
'''
print(re.match("....O$","HELLO")); 

'''
{N,M } -> minimun to maximum
'''
print(re.match("[a-z]{2,5}$","abcdef")); 

'''
( ) -> match in group
'''
print(re.match("(ab)?c","abc")); 

'''
| -> one or more conditions(or);
'''

print(re.match("[a-z]+ | [0-9]+","abc123def456")); 