list1= [1,2,3,4,5] #List of integers
print (list1)
list2= [1.5,2.5,3.5,4.5,5.5]#List of floats
print (list2)
list3= [True , False] #list of boolean
print (list3)
list4= ["2","4","6","7"] #list of strings
print(list4)
list5= [2,4,2.5,True,"2","4","5.5",False] #combination of all lists above
print(list5)

#INDEXING

print(list5[0])#First index using the positive method
#print (len(list5))
print(list5[-8])#first index using the negative method
print(list5[7])#last index using the positive method
print(list5[-1])#last index using the negative method
print(list5[4]) #Middle index using the positive method
print(list5[-4])#Middle index using the negative method

#CONVERSION

list6=[23,2.4,6,True,5]
print (type(list6))#printing out the type of the variable
print(list("Hello"))#converting a string to a list
print(list({1:"one",2:"two"}))#converting a dictionary to a list
print(list((10,20,30)))#converting a tuple to a list
print(list({100,200,300}))#converting a set to a list


#ITERATELIST

list7= ["john","happy","joy","faith"]
for name in list7:
    print(name)#printing out the names in list7

for ind in range(len(list7)):
    print(list7[ind])#Using index to print all value in the list


#UPDATELIST

list7[0]="mark"
print(list7)#replacing john with mark in the list
list7[1]='sadness'
print(list7)#replacing happpy with with sadnesss in the list
list7[2]='tope'
print(list7)#replacing joy with tope in the list
list7[3]="daniel"
print(list7)#replacing faith with daniel in the list

list7.append('john')
print(list7)#adding john to the list


#REMOVEFROMALIST

print('list7: ',list7)
del list7[0]
print('list7 after deleting first index using del: ',list7)

list7.remove('sadness')
print('list7 after the removing sadness using remove: ',list7)

print (list7.pop(0))#printing pop items at index zero
print('list7 after poping first index using pop: ',list7)

print (list7.pop())#printing pop items at the last index 
print('list7 after poping last index using pop: ',list7)

list7.clear() #Emptying the entire list
print(list7)

del list7 #deleting the entire list

list8 = [1,2,3]
list9 = [4,5,6]
print (list8 + list9)#Combining of list8 and list9
print(list8*4)#Multiplying list8 by 4
print(list8[0:2])#printing out list8 
print(6 in list8)#checking if 6 appears in list8
print(6 not in list8)#checking if 6 is not in list8


#LISTMETHOD

list10 = list8.copy()#copying list8 to list10
print(list10) 
print(list10.count(2))#counting the amount of 2 in list10
list8.extend(list9)#extending list8 with list9
print(list8)


print(list8.index(4))#checking index 4 in list8
list10.insert(1,10)
print(list10)#Replacing index 1 with 10


list10.reverse()
print(list10)#Reversing list10 from the end to the begining

list10.sort()
print(list10)#Rearranging the list10

list10.sort(reverse=True)
print(list10)












































































































