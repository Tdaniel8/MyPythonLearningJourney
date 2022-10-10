#INTKEY

dict1= {1:1,2:2,3:3} #INTKEY : #INTVALUE
print(dict1)
dict2= {2:'two',3:'three',5:'five'} #INTKEY : #STRVALUE
print(dict2)
dict3= {3:('THREE','III'),4:('Four','IV'),5:('five','V')}#INTKEY : #TUPLEVALUE
print(dict3)
dict4= {10:['Ten','X'],9:['nine','IX'],11:['Eleven','XI']} #INTKEY : #LISTVALUE
print(dict4)
dict5= {4:{'Four','IV'},5:{'Five','V'},6:{'six','VI'}} #INTKEY : #SETVALUE
print(dict5)

#STRINGKEY

dict6= {"2":2,"5":5,"7":7} #STRKEY:#INTVALUE
print(dict6)
dict7= {'8':'VIII','9':'IX','20':'XX'} #STRKEY #STRVALUE
print(dict7)
dict8= {'10':('ten','X'),'5':('Five','V'),'7':('seven','VII')}#STRKEY #TUPLEVALUE
print(dict8)
dict9= {"4":["four","IV"],"6":["SIX","XI"],"9":["NINE","IX"]}#STRKEY #LISTVALUE
print(dict9)
dict10= {'10':{'Ten','X'},'11':{'eleven','XI'},'12':{'TWELVE','XII'}}#STRKEY #SETVALUE
print(dict10)
#FLOATKEY

dict11= {2.5:5,5.5:10,3.5:20}#FLOATKEY : #INTVALUE
print(dict11)
dict12= {1.5:'4',2.5:'5',3.5:'20'}#FLOATKEY : #STRVALUE
print(dict12)
dict13= {2.3:('4',),4.5:('10',),6.7:('10',)}#FLOATKEY :#TUPLEVALUE
print(dict13)
dict14= {1.7:['15'],2.0:['8'],4.7:['17']} #FLOATKEY : #LISTVALUE
print(dict14)
dict15= {3.2:{"15"},5.0:{"20"},4.5:{"19"}} #FLOATKEY : #SETVALUE
print(dict15)

#TUPLEKEY

dict16= {('2',):1,('10',):20,('5'):15}#TUPLEKEY : #INTVALUE
print(dict16)
dict17= {('5',):'10',('10',):'15',('20',):'50'} #TUPLEKEY : #INTVALUE
print(dict17)
dict18= {('2',):('10',),('5',):('20',),('7'):('25',)}#TUPLEKEY :#TUPLEVALUE
print(dict18)
dict19= {('4',):['10'],('5',):['15'],('6'):['20']}#TUPLEKEY : LISTVALUE
print(dict19)
dict20= {('5',):{'10'},('8'):{'15'},('9'):{'20'}}#TUPLEKEY : #SETVALUE
print(dict20)



dict21 = {} #empty dictionary using curly brackets
print("dict21: ",dict21)
dict22 = dict() #empty dictionary using the dict class
print('dict22: ',dict22)

dict23 = dict(two = ('David', 29), three = ("Daniel", 34))
print(dict23)

#multidimensional dictionary
dict24 ={"name":"Steve","age":25, "marks":60}
dict25 ={"name":"Anil","age":23, "marks":75}
dict26 ={"name":"Asha", "age":20, "marks":70}

dict27 = {1:dict24, 2:dict25, 3: dict26}
print(dict27)

#Accessing Dictionary
print(dict7['8']) #return the value for key 8

#iterate
for key in dict7:
    print("Key = "+key+" ,Value = "+dict7[key])

#update dictionary
print("dict 21 before update: ",dict21)
dict21['Daniel'] = 25
dict21['David'] = 22
print("dict 21 after update: ",dict21)

#dictionay methods

#get method
print(dict7.get('8')) #element in the list
print(dict7.get('2')) #element not in the list

#del python function
print('dict12 before del function: ', dict12)
del dict12[2.5]
print('dict12 after del function: ', dict12)

#pop method
print('dict12 before pop function: ', dict12)
dict12.pop(1.5)
print('dict12 after pop function: ', dict12)


#popitem method
print('dict13 before popitem function: ', dict13)
dict13.popitem()
print('dict13 after popitem function: ', dict13)

#keys method
print(dict9)
print('dict9 keys: ',dict9.keys())

#values method
print('dict9 values: ', dict9.values())

#items method
print('dict9 items: ', dict9.items())

# in operator
print('4' in dict9)
print('4' in dict9.keys())
print('4' in dict9.values())

# not in operator
print('4' not in dict9)
print('4' not in dict9.keys())
print('4' not in dict9.values())










