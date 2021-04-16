#set is a unordered sequence of elements without duplicates
#set can be modified
#hash algorithm is used to compare and remove duplicates
#hash works on mutable object(not modifyable) 
s=set();
print(type(s));

l=[1,2,3,4,54,1,3,5,6,23];

s=set(l);

print(s);

s.add(0);
s.add((1,2,3));
print(s);