#email id verification

import re;
print(re.match("[a-z]+@[a-z]+\.[a-z]+$","test@gmail.com")); 

print(re.match("[a-z]+@[a-z]+.[a-z]+$","testgmail.com")); 

print(re.match("[a-z]+@[a-z]+.[a-z]+$","test@gmailxcom")); 

print(re.match("[a-z.0-9]+@[a-z]+\.[a-z]$","test123.name@gmail.com"))

print(re.match("[a-z.0-9]+@[a-z]+\.[a-z]{2,3}$","test123.name@gmail.commmm"))

#numeric verification
#value=999.99

print(re.match("[0-9]+\.[0-9]{1,2}$","999.99"));

print(re.match("[+-]?[0-9]+\.[0-9]{1,2}$","+999.99"));