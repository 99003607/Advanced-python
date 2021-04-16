#dictionary-> key value pairs
'''
d={};
print(type(d));

d={"id":111,"name": "name1","role":"dev"};

print(d);

#accesing elements

print(d["role"]);
'''
#no repetations in keys
#here name1 is replace by name2
'''
d={"id":111,"name": "name1","role":"dev","name":"name2"};
print(d);

print(d.get("role"));
#returns none==NULL
print(d.get("role1"));
#returns 999
print(d.get("role1",999));


print(d);
d["role"]="test";
print(d);
d["role1"]="imp";
print(d);

#deleting  elements
print(d);
del(d["role1"]);
print(d);

value=d.pop("role");
print("value:",value);
print(d);
print(value);

#remove all elements
d.clear();
print(d);
'''

#travesing array
'''
d={"id":111,"name": "name1","role":"dev","name":"name2"};

keys=d.keys();

for key in keys:
    print(key,d[key]);
'''

 #to create dictionary   
 #dict take only list of items
d1=dict([("id",111),("name", "name1"),("role","dev")]);
print(d1);

print(d1.items());

for item in d1.items():
    print(item);
    
for key,value in d1.items():
    print(key,"=>",value);

#combining dictionary
d2={"id":222,"role2":"test"};

print(d1);
d1.update(d2);

print(d1);



