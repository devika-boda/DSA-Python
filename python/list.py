import copy
'''lst=[10,20,30,40,30]
print(lst)
while 30 in lst:
    lst.remove(30)
print(lst)
lst.pop(0)
print(lst)'''
#lst=[1,2,3,4,5,6,7,8]
''' lst[3]
print(lst)
del lst[1:5]
del lst[::2]
del lst[-2:-7:-1]
print(lst)'''


#this is shallow copy() of a list         
'''1 =[[1,2],[3,4]]
lst2=list(lst1)
print(lst1)
print(lst2)
print(lst1 is lst2)
lst1.append([5,6])
print(lst1)
print(lst2)
lst1[1][0]=30
print(lst1)# change in list 1 will effect the list2
print(lst2)'''



#This is the deep copy of the list

lst1 =[[1,2],[3,4]]
lst2= copy.deepcopy(lst1)
print(lst1)
print(lst2)
print(lst1 is lst2)
lst1.append([5,6])
print(lst1)
print(lst2)
lst1[1][0]=30
print(lst1)# change in list 1 will not effect the list 2 
print(lst2)


 