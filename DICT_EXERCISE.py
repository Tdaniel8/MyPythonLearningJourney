#Question 1
list1 = [10,20,30,40,50]
list2 = ['Ten','Twenty','Thirty','Fourty','Fifty']

dict1 = {}
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]

print(dict1)

#Question 2
dict2 = {0: 10, 1: 20}
dict2[2] = 30
print(dict2)

#Question 3
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1.update(dict2)
dic1.update(dic3)
print(dic1)

#Question 4
print('7' in dict1)

#Question 5
print(sum(dic1.values()))
