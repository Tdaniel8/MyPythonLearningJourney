list1= [1,2,3,4,5] #List of integers

#Question 1

#method 1
print("Question-1(a): ",sum(list1))

#method 2
summer = 0
for num in list1:
    summer += num #summer = summer + num

print('Question-1(b): ',summer)

#Question 2
mulNum = 1
for num in list1:
    summer *= num #summer = summer + num

print('Question-2: ',summer)

#Question 3
print('Question-3: ',max(list1))

#Question 4
print('Question-4: ', min(list1))

#Question 5
list2 = ['abc', 'xyz', 'aba', '1221']
counter = 0
for strs in list2:
    if len(strs) >= 2:
        if strs[0] == strs[-1]:
            counter += 1

print('Question-5: ',counter)
