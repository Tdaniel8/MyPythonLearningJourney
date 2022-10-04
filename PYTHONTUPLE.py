tup1=(1,2,3,4,5) #tup of integers
print(tup1)
tup2=(1.2,2.3,2.6,5.0,1,9)#tup of floats
print(tup2)
tup3=(True,False)#tuple of boolean
print(tup3)
tup4= "1","2","7","5" #tup of strings
print (tup4)
tup5=(2,3,"7",True,2.3,False) #combinations of all tub above
print(tup5)


#INDEXING

print(tup5[0])#First index using the positive method
print(tup5[-6]) #first index using the negative method
print(tup5[5])#Last index using the positive method
print(tup5[-1])#last index using the negative method
print(tup5[4])#2nd to the last index using positive method
print(tup5[-2])#2nd to the last index using the negative method


#CONVERSION


tup6=(1,3,5.6,True,10)
print(type(tup6))#Printing out the type of variables
print(tuple("Hello"))#converting a string to a tuple
print(tuple({1:"one",3:"three"}))#converting a dictionary to a tuple
print(tuple[[10,20,24]])#converting a list to a tuple
print(tuple[{120,300,200}])#converting a set to a tuble


#ITERATE Tuple

tup7= ("john","happy","joy","faith")
for name in tup7:
    print(name)#printing out the names in tuple7

for ind in range (len(tup7)):
    print(tup7[ind])#using index to print all value in the tuple



print('tup7: ',tup7)
del tup7 #deleting the entire tuple


tup8= (1,2,3)
tup9=(4,5,6)
print (tup8+tup9)#combining tuple8 and tuple9
print(tup8*4)#multiplying tup8 by 4
print(tup8[0:2])#printing out tuple8
print(6 in tup8)#checking if 6 appears in tup8
print(6 not in tup8)#checking if 6 is not in tuple8






















































































