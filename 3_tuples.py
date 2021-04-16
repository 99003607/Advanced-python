#tuple

t=();
print(type(t));
#no modifications:t[1]=1;->error
print("creating tuple");
l=[1,2,3,4,5];
t=tuple(l);
print(t);

#slicing,traversing