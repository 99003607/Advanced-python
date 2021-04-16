#data structures

#list -> order sequnce of elements

l = [1,2,3.6,"test", True];

print(type(l));

print(l);

print(l[3]);

print(len(l)); #len -> giving length of iterable object(string,lists,tuple)

l1=[1,2,3,4,5,6,7,8,9];
print(l1);
l1[1]=33;
print(l1);

print(l1[1:5]);

l1[1:4]=[11,22,33];

print(l1);

l1[1:4]=[11,22,33,44,55]; #it will expand

print(l1);

#u can have list in list


#methods

print("opeartions");
l=[];

l.append(10);

print(l);

l.append([12,13,14]);

print(l);
#extend will take iterable object
l.extend([22,33,44]);

print(l);
#insert

l.insert(3,'x');
print(l);

#deletion
del(l[1]);

print(l);

#pop ->return the value after deleting
value=l.pop(3);
print(l);
print(value);

value=l.pop();#remove last element
print(l);
print(value);

#travesing in the list
''''
for <element> in <iterable-object>:
    .....
 '''
print("l:",l);
for i in l:
    print(i,sep="--",end="");

