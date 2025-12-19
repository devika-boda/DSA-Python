'''s={1,2.7,True,1+3J,"python"}
print(s)
print(type(s))'''

#it does not allow mutable data to be stored .so error comes
'''s={1,2.7,True,1+3J,"python",[10,20,30]}
print(s)
print(type(s))

print(hash(10))
print(hash([1,2,3,4]))'''#it gives erroe because mutable data is not allowed in set

'''s={23,67,89,54,92,1}
#s.add(90)
#s.remove(67)
#s.pop()
#s.discard(11)
s.update({2,5,7})
print(s)'''
#some useful methods of  a set
'''s1={1,2,3,4}
s2={3,4,5,6}
#s3=s1.union(s2)
s3=s1 | s2
s4=s1&s2
s5=s1-s2
s6=s1.symmetric_difference(s2)
s1.intersection_update(s2)
print(s1)
print(s3)
print(s4)
print(s5)
print(s6)'''


#set functions

'''s1={1,2,3,4,5,6}
s2={4,5,6}
print(s2<=s1)
print(s2.issubset(s1))
print(s1>=s2)
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))'''


#write a program to take programming names and remove all duplicates.
'''lst=input().split()
print(lst)
s=set(lst)
print(s)'''

#program to print the number of duplicates present in  a list

'''lst=input("enter a list of numbers: ").split()
l=list(map(int,lst))
s=set(l)
print("number of duplicates = ",len(l)-len(s))'''

# set comprehension
'''s={5,4,6,8,2}
s_c={i**2  if i%2==0 else i+i for i in s}
print(s_c)'''

#program to print whether the given string is a panagram or not
'''s=input("enter a string: ").upper()
s=set(s)
c=set()
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        c.add(i)
if len(c)==26:
    print("panagaram")
else:
    print("not a panagram")'''

# to check whether the given string is heterogram or not(means no letter is reated more than once)
'''s=input("enter a string:").upper()
lst=[]
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        lst.append(i)
c=set(lst)
if len(c)==len(lst):
    print("heterogram")
else:
    print("not a heterogram")'''

#frozen set
'''s=frozenset({1,2,3,4,5})
s1={3,4,5,6}
#s.pop()
print(s)# this will give error bcz frozen set is immutable
print(s|s1)'''




