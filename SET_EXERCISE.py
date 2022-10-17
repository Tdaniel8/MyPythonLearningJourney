#Question 1
set1 = {1,2,3,4,5,6} #Set of integers
set1.add(7)
set1.add(8)
print(set1)

set3 = {2.5,3.6,8.9,1.2}
print(set3)
set7 = {10,20,30,40}
print(set7)

#Question 2
#remove, pop, popitem, del, discard
set1.remove(2)
print(set1)

#Question 3
set1.discard(10)
print(set1)

#Question 4
#INTERSECTION

print('set3: ', set3)
print('set7: ', set7)
print('intersection using & ',set3 & set7)
print('intersection using intersection funtion',set3.intersection(set7))

#Question 5
print(set3.issubset(set1))
