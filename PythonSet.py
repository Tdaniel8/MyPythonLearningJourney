set1 = {1,2,3,4,5,6} #Set of integers
print(set1)
set2 = {2.5,3.6,1.0,5.5} #set of floats
print(set2)
set3 ={'2','4','7','8'} #set of stringgs
print(set3)
set4 ={True,False} #set of Boolean
print(set4)
set5 = {2, 2.0,True,'4',5} #set of different data types
print(set5)
set6 ={1,2,2,3,3,4,4} #set of duplicated values
print(set6)
set7 ={(23,2.5,5,'3'), 5.5,2.5,"2.5","2.3",5,9}#set of tuple,floats,integers and strings
print(set7)
set8 = set()#An empty set
print(type(set8))
set9 = set(('hello'))#converting a tuple to set
print(set9)
set10 = set([1,2,3,4,5])#converting a list to a set
print(set10)
set11 = set({1:'ONE',2:'TWO'})
print(set11)



#MODIFYSETELEMENT

set12 = set()

#add function
set12.add(10)
set12.add(20)
set12.add(30)
set12.add(40)
print(set12)


#UPDATE

set13 = {1,3,5,7}
set12.update(set13)
print(set12)

#REMOVE

set12.remove(20)
print(set12)

#UNION

set14 = {10,30,50,60,70}
print('set12: ', set12)
print('set14: ', set14)
print('union using |',set12 | set14)
print('union using |',set12 or set14)
print('union using union funtion',set12.union(set14))

#INTERSECTION

print('set12: ', set12)
print('set14: ', set14)
print('intersection using & ',set12 and set14)
print('intersection using intersection funtion',set12.intersection(set14))

#DIFFERENCE

print('set12: ', set12)
print('set14: ', set14)
print('difference using - ',set12 - set14)
print('difference using - ',set14 - set12)
print('difference using difference funtion',set12.difference(set14))
print('difference using difference funtion',set14.difference(set12))

#SYMMETRIC

print('set12: ', set12)
print('set14: ', set14)
print('symmetric_difference using ^ ',set12 ^ set14)
print('symmetric_difference using symmetric_difference funtion',set12.symmetric_difference(set14))

#CLEAR

set13.clear()
print (set13)

#COPY

set15 = set2.copy()
print(set15)

#ISSUBSET

set16 = {3,5,7}
print(set16.issubset(set12))

#INTERSECTIONUPDATE
set12.intersection_update(set14)
print('intersection update of set12 and set14: ',set12)
print('intersection update of set12 and set14: ',set14)

#DIFFERENCEUPDATE
set14.difference_update(set12)
print('diffrence update of set12 and set14: ',set12)
print('diffrence update of set12 and set14: ',set14)

#DISCARD

set14.discard(70)
print(set14)

#ISDISJOINT

print (set12.isdisjoint(set14))

#POP

print(set15.pop())
print(set15)

#SYMMENTRICDIFFERENCEUPDATE
set15.add(45.0)
set15.symmetric_difference_update(set2)
print(set15)























































































